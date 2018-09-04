from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('', views.LoginView.as_view(), name = 'index'),
    path('esqueci_senha/', views.EsqueciSenhaView.as_view(), name = 'esqueci_senha'),
]