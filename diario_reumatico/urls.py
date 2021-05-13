from django.urls import path
from rest_framework import routers
from .views import DorView, HumorView,RemediosView,RigidezView
from .models import Dor, Humor, Remedios, Rigidez
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

router = routers.DefaultRouter()
router.register('dor',DorView,basename='Dor')
router.register('humor',HumorView,basename='Humor')
router.register('remedios',RemediosView,basename='Remedios')
router.register('rigidez',RigidezView,basename='Rigidez')


urlpatterns = [
    path('api-token/', TokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),
]

urlpatterns=router.urls