from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',views.chat_view,name='index'),
    path('login',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout',LoginView.as_view(),name='logout')
]
