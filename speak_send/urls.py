from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

router = DefaultRouter()
router.register(r'message', views.MessageModelViewSet)

urlpatterns += router.urls
