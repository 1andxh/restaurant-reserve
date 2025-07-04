from django.shortcuts import render
from rest_framework import generics, permissions, status
from reservations.serializers import CreateReservationSerializer
from rest_framework.response import Response

class CreateReservation(generics.CreateAPIView):
    serializer_class = CreateReservationSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        try: 
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            reservation = serializer.save()
            return Response({
                'message' : 'Reservation created successfully, proceed to "bookings" to check status.',
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

'''