from django.shortcuts import render
from django.http import HttpResponse
from .serializers import MessageSerializer
from .models import Message
from rest_framework.viewsets import ModelViewSet

class MessageModelViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the speak_send index.")