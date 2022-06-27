from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView
from . import views
urlpatterns = [
    path('create', views.UserCreateView.as_view()),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('follow', views.FollowView.as_view()),
    path('follow/<int:target_id>', views.FollowView.as_view()),
]