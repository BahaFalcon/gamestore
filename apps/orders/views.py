from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrderSerializer
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


class CreateOrder(APIView):
    serializer_class = OrderSerializer

    @swagger_auto_schema(
        operation_summary='Create new order',
        request_body=OrderSerializer(many=False),
        responses={
            '201': OrderSerializer,
            '400': 'Bad request'
        },
    )
    def post(self, request):

        serializer = OrderSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)







