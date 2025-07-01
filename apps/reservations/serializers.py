from rest_framework import serializers
from reservations.models import Reservations

class CreateReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservations
        fields = [
            'id',
            'guest_name',
            'guest_phone',
            'guest_email',
            'guest_size'
            'reservation_date',
            'reservation_time',
            'special_note',
            'status',
            'created_at' 
            'updated_at'      
        ]
        read_only_fields = [
            'id',
            'created_at',
            'updated_at'
        ]
        extra_kwargs = {
            'guest_name': {'required' : True},
            'guest_phone': {'required' : True},
            'guest_size': {'required' : True},
            'reservation_date' : {'required' : True},
            'reservation_time' : {'required' : True}
        }
    def validate_guest_size(self, value):
        if value <= 0:
            raise serializers.ValidationError('Cannot make reservation with no guests!')
        return value
    

        