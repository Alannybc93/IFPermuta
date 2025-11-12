from django.urls import path
from . import views  # <- o ponto indica importar do mesmo diretório

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.dashboard, name='dashboard'),
]
