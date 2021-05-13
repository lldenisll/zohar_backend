from django.urls import path
from rest_framework import routers
from .views import MyUserView
from .models import MyUser

router = routers.DefaultRouter()
router.register('users',MyUserView,basename='Users')



urlpatterns=router.urls