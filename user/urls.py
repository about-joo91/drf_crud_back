from django.urls import path
from . import views
urlpatterns = [
    path('create', views.UserCreateView.as_view()),
    path('control', views.UserControlView.as_view())
]
