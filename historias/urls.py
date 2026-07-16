from django.urls import path
from .views import EnviarHistoriaView, ListarHistoriasView, CambiarEstadoView, LoginView, LogoutView, RegistroView

urlpatterns = [
    path('historias/enviar/', EnviarHistoriaView.as_view(), name='enviar-historia'),
    path('historias/', ListarHistoriasView.as_view(), name='listar-historias'),
    path('historias/<int:pk>/estado/', CambiarEstadoView.as_view(), name='cambiar-estado'),
    path('auth/registro/', RegistroView.as_view(), name='registro'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
]
