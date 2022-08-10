from rest_framework import serializers

from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password', 'location', 'phone')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        return user


class UserLoginSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=150, allow_null=False, required=True)
    password = serializers.CharField(max_length=255, allow_null=False, required=True)

