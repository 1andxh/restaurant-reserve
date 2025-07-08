from django.shortcuts import render
from rest_framework import generics, permissions, status
from .serializers import CreateReservationSerializer
from rest_framework.response import Response
from .models import Restaurant
from django.shortcuts import get_object_or_404
from django.db import transaction 
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
        

class ViewReservation(generics.CreateAPIView):

    pass
    

# TODO : 
'''
- once you make a reservation, it goes to pending since the admin hasn't approved it yet, 
guest check their bookings to confirm if the reservation was cancelled or approved
- i think the status should be in the booking part, the completed part should only be on the admin side
- a reservation is completed only when that day has passed
-- views restaurants to able to make reservations
'''