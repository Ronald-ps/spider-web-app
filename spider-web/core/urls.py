from django.urls import include, path
from rest_framework import routers

from core import views, viewsets

router = routers.DefaultRouter()
router.register(r"documents", viewsets.DocumentViewSet)
router.register(r"external-documents", viewsets.DocumentViewSet)
#  isso deve ficar acima de urlpatterns


urlpatterns = [path("hello/", views.hello), path("", include(router.urls))]
