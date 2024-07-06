from rest_framework_json_api import serializers as json_api_serializers
from .models import User, Product

class UserSerializer(json_api_serializers.ModelSerializer):
    class Meta:
        model = User
        resource_name = 'users'
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'phone_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ProductSerializer(json_api_serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'created_at', 'updated_at')
