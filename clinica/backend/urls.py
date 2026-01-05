from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from backend.views.consulta import ConsultaView
from rest_framework.routers import DefaultRouter
from backend.views.paciente import PacienteView
from backend.views.auth import LoginView, LogoutView
from backend.views.especialidade import EspecialidadeView
from backend.views.profisssional import ProfissionalView

router = DefaultRouter()
router.register(r'especialidade', EspecialidadeView, basename='especialidade')
router.register(r'consulta', ConsultaView, basename='consulta')
router.register(r'paciente', PacienteView, basename='paciente')
router.register(r'profissional', ProfissionalView, basename='profissional')


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
] 
urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)