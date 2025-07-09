from django.shortcuts import render
from rest_framework import generics, permissions, status
from .permissions import IsRestaurantOwner
from .serializers import CreateReservationSerializer, UpdateReservationStatusSerializer, ViewReservationSerializer
from rest_framework.response import Response
from .models import Restaurant
from django.shortcuts import get_object_or_404
from django.db import transaction
from models import Reservations 
import traceback
class CreateReservation(generics.CreateAPIView):
    serializer_class = CreateReservationSerializer
    permission_classes = [permissions.AllowAny]

    @transaction.atomic()
    def create(self, request, *args, **kwargs):
        restaurant_id = self.kwargs.get('restaurant_id')
        try: 
            Restaurant.objects.get(id=restaurant_id)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            reservation = serializer.save(restaurant_id=restaurant_id)
            return Response({
                'message' : 'Reservation created successfully, proceed to check booking status.',
                'reservation' : serializer.data,
                'reservation_id' : reservation.id
            },
            status=status.HTTP_201_CREATED
            )
        except Restaurant.DoesNotExist:
            return Response({
                'error' : 'Not found'
            },
            status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response({
                'error' : 'An error occured while creating reservation',
                'details' : f'{str(e)} : \ntraceback {traceback.print_exc()}'
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UpdateReservationStatus(generics.RetrieveUpdateAPIView):
    """
        restaurant admins -- this view allows users update reservation status once 
        reservation has been made
    """
    serializer_class = UpdateReservationStatusSerializer
    permission_classes = [permissions.IsAuthenticated, IsRestaurantOwner]

    """
    inheriting BasePermissions--has_object_permission(self, request, view, object,) will allow the user make changes to a specific model instance
    --but how do i implement this...
    """
    def get_queryset(self):
        restaurant_id = self.kwargs.get('restaurant_id')
        return Reservations.objects.filter(
            restaurant_id=restaurant_id,
            restaurant__owner=self.request.user
            )
  
    def perform_update(self, serializer):
        serializer.save()


class ViewReservation(generics.ListAPIView):
    """
    once visitors hit this end point it should display their reservation with an updated status choice
    they can check on their reservation by doing a lookup on the reservations associated with their phone_number
    """
    serializer_class = ViewReservationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly|IsRestaurantOwner]

    
    
"""
also once the status is changed to cancelled it must be deleted from the db; TODO
"""





# TODO : 
'''
-- once you make a reservation, it goes to pending since the admin hasn't approved it yet, 
guest check their bookings to confirm if the reservation was cancelled or approved
-- i think the status should be in the booking part, the completed part should only be on the admin side
-- a reservation is completed only when that day has passed
-- views restaurants to able to make reservations

-- to get bookings, that endpoint will reference the owner and list all reservations associated with
-- implement sms/email notifications after successful reservation (on both ends)
'''