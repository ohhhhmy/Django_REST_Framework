from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from mystorage import views

router = DefaultRouter()
router.register('essay', views.PostViewSet)
router.register('album', views.ImageViewSet)
router.register('files', views.FileViewSet)


urlpatterns = [
    path('', include(router.urls)),
]