from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Historia
from .serializers import HistoriaPublicaSerializer, HistoriaSerializer, EstadoSerializer


class EnviarHistoriaView(generics.CreateAPIView):
    queryset = Historia.objects.all()
    serializer_class = HistoriaPublicaSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'mensaje': 'Historia enviada con éxito. ¡Gracias por compartirla!'},
            status=status.HTTP_201_CREATED
        )


class ListarHistoriasView(generics.ListAPIView):
    serializer_class = HistoriaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        estado = self.request.query_params.get('estado')
        qs = Historia.objects.all()
        if estado and estado != 'todos':
            qs = qs.filter(estado=estado)
        return qs


class CambiarEstadoView(generics.UpdateAPIView):
    queryset = Historia.objects.all()
    serializer_class = EstadoSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['patch']


class RegistroView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username', '').strip()
        password = request.data.get('password', '')
        email = request.data.get('email', '').strip()

        if not username or not password:
            return Response(
                {'error': 'Usuario y contraseña requeridos'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if User.objects.filter(username=username).exists():
            return Response(
                {'error': 'Ese nombre de usuario ya está en uso'},
                status=status.HTTP_400_BAD_REQUEST
            )

        User.objects.create_user(username=username, password=password, email=email, is_staff=False)
        return Response(
            {'mensaje': 'Cuenta creada. Un administrador debe aprobarla antes de que puedas ingresar.'},
            status=status.HTTP_201_CREATED
        )


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response(
                {'error': 'Usuario y contraseña requeridos'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(username=username, password=password)
        if not user:
            return Response(
                {'error': 'Credenciales incorrectas'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        if not user.is_staff:
            return Response(
                {'error': 'Tu cuenta aún no fue aprobada por un administrador'},
                status=status.HTTP_403_FORBIDDEN
            )

        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'username': user.username})


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({'mensaje': 'Sesión cerrada'})
