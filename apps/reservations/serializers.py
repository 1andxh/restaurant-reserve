from rest_framework import serializers
from .models import Reservations
from datetime import date

class CreateReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservations
        fields = [
            'id',
            'guest_name',
            'guest_phone',
            'guest_email',
            'party_size',
            'reservation_date',
            'reservation_time',
            'special_note',
            'status',
            'created_at' ,
            'updated_at'      
        ]
        read_only_fields = [
            'id',
            'created_at',
            'updated_at'
        ]

    def validate_part_size(self, value):
        if value < 1:
            raise serializers.ValidationError ('Party size must be at least 1')
        if value > 20 :
            raise serializers.ValidationError('Party cannot exceed 20 people')
        return value
    
    def validate_reservation_date(self, value):
        if not value:
            raise serializers.ValidationError('Date cannot be empty!')
        if value < date.today():
            raise serializers.ValidationError('Date must be current or future')
        return value

    def create(self, validated_data):
        if 'status' not in validated_data:
            validated_data['status'] = 'Pending'

        reservation = Reservations.objects.create(**validated_data)
        return reservation
        

        