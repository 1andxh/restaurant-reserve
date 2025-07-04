from django.shortcuts import render
from rest_framework import generics, permissions, status
from .serializers import CreateReservationSerializer
from rest_framework.response import Response
from .models import Restaurant
from django.shortcuts import get_object_or_404
class CreateReservation(generics.CreateAPIView):
    serializer_class = CreateReservationSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        try: 
            restaurant_id = self.kwargs.get('restaurant_id')
            restaurant = get_object_or_404(Restaurant, id=restaurant_id)
            try:
                if not restaurant_id:
                    return Response({
                        'error' : 'Restaurant_id not provided',
                    },
                    status=status.HTTP_400_BAD_REQUEST
                    )
            except Restaurant.DoesNotExist:
                return Response({
                    'error' : 'Restaurant not found'
                },
                status=status.HTTP_404_NOT_FOUND
                )
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            reservation = serializer.save(restaurant=restaurant)
            return Response({
                'message' : 'Reservation created successfully, proceed to check booking status.',
                'reservation' : serializer.data,
                'reservation_id' : reservation.id
            },
            status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response({
                'error' : 'An error occured while creating reservation',
                'details' : str(e)
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