from rest_framework import routers
from django.urls import path, include

from .views import HududAPIView, QurilishTashkilotiAPIView, QurilishAPIView

router = routers.SimpleRouter()
router.register('hudud', HududAPIView)
router.register('qurilish-tashkiloti', QurilishTashkilotiAPIView)
router.register('qurilish', QurilishAPIView)


urlpatterns = [
    path('v1/', include(router.urls))
]
