from django.conf.urls import url, include
from rest_framework import routers
from . import viewsets

router = routers.DefaultRouter()
router.register(r'to-do', viewsets.TodoViewSet)

urlpatterns = [
    url(r'^viewsets/', include(router.urls))
]