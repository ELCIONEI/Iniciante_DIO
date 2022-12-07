

from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tcc/', views.cadastro_usuarios),
    path('Chamados/',views.chamados),
    path('Cadastro/',views.cadastro_usuarios),
    path('login/', views.login_usuario.html)
]
