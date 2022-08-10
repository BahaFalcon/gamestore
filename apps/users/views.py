from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema

from .serializers import UserLoginSerializer, UserRegistrationSerializer

User = get_user_model()


class UserRegistrationAPIView(APIView):
    serializer_class = UserRegistrationSerializer

    @swagger_auto_schema(
        operation_summary='Create new user',
        request_body=UserRegistrationSerializer(many=False),
        responses={
            '201': 'Created'
        },
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user=user)

        return Response(data={'token': token.key},
                        status=status.HTTP_201_CREATED)


class LoginUserAPIView(APIView):
    serializer_class = UserLoginSerializer

    @swagger_auto_schema(
        operation_summary='Login user',
        request_body=UserLoginSerializer(many=False),
        responses={
            '200': UserLoginSerializer,
            '400': 'Bad request'
        },
    )
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)  # {'username': 'bakyt007', 'password': 'akjlsdf'}
        serializer.is_valid(raise_exception=True)
        try:
            user = User.objects.get(username=serializer.validated_data['username'])
        except User.DoesNotExist:
            return Response(data={'detail': 'Не существует такого пользователя'},
                            status=status.HTTP_400_BAD_REQUEST)
        is_correct = user.check_password(serializer.validated_data['password'])
        if is_correct:
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            # token, is_created = Token.objects.get_or_create(user=user)  # альтернатива
            return Response(data={'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response(data={'detail': 'Не существует такого пользователя'},
                            status=status.HTTP_400_BAD_REQUEST)
