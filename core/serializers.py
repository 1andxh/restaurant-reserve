from rest_framework import serializers
from core.models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            'id',
            'name', 
            'address', 
            'contact', 
            'email', 
            'date_opened', 
            'working_hours', 
            'type',
            'created_at',
            'updated_at'
        ]
        read_only_feilds = ['id', 'created_at']


class UpdateRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            'name', 
            'address', 
            'contact', 
            'email', 
            'working_hours', 
            'type'
        ]
        