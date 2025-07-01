from django.shortcuts import render
from rest_framework import generics

class CreateReservation(generics.CreateAPIView):
    pass


'''
- once you make a reservation, it goes to pending since the admin hasn't approved it yet, 
guest check their bookings to confirm if the reservation was cancelled or approved
- i think the status should be in the booking part, the completed part should only be on the admin side
- a reservation is completed only when that day has passed

'''