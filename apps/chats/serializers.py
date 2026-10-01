from rest_framework import serializers
from .models import Threads,Messages


class ThreadsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Threads
        fields=['id', 'created_at', 'members']
        read_only_fields =['id','created_at']

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields= '__all__'
        read_only_fields=['id','created_at','sender']
