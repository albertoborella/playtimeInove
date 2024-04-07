from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.authentication import (BasicAuthentication, TokenAuthentication)
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from stock.models import Formula,Articulo
from stock.api.serializers import UserLoginSerializer,TokenSerializer,FormulaSerializer


class LoginAPIView(APIView):
    '''
    Vista de API personalizada para recibir peticiones post
    Esquema de entrada:
    {"username": "admin2", "password": "admin123"}
    '''

    parser_classes = [JSONParser]
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        user_login_serializer = UserLoginSerializer(data=request.data)

        if user_login_serializer.is_valid():
            _username = request.data.get('username')
            _password = request.data.get('password')
            _account = authenticate(username=_username, password=_password)
            if _account:

                _token, _created = Token.objects.get_or_create(user=_account)
                return Response(
                    data=TokenSerializer(instance=_token, many=False).data,
                    status=status.HTTP_200_OK
                )
            return Response(
                data={'error': 'Invalid Credentials.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            data=user_login_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class FormulaProductoList(ListAPIView):
    serializer_class = FormulaSerializer
    
    def get_queryset(self):
        queryset = Formula.objects.all()
        producto = self.request.query_params.get('producto')
        if producto is not None:
            queryset = queryset.filter(producto=producto)
        return queryset