from .models import Message
from rest_framework import serializers

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['recv_uid', 'type', 'text', 'url']