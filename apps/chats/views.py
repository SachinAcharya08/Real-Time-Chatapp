from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Threads,Messages
from .serializers import ThreadsSerializer,MessagesSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination



class ThreadViewset(viewsets.ViewSet):
    def list(self,request):
        qs=Threads.objects.all().order_by('created_at')
        serializer=ThreadsSerializer(qs,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer=ThreadsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    def retrieve(self,request,pk=None):
        qs=Threads.objects.all()
        Thread=get_object_or_404(qs,pk=pk)
        serializer=ThreadsSerializer(Thread)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def update(self,request,pk=None):
        qs=Threads.objects.all()
        Thread=get_object_or_404(qs,pk=pk)
        serializer=ThreadsSerializer(Thread,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    def partial_update(self,request,pk=None):
        qs=Threads.objects.all()
        Thread=get_object_or_404(qs,pk=pk)
        serializer=ThreadsSerializer(Thread,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    def destroy(self,request,pk=None):
        qs=Threads.objects.all()
        Thread=get_object_or_404(qs,pk=pk)
        Thread.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MessageViewset(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self,request):
        thread_id=request.query_params.get('thread')
        qs = Messages.objects.filter(thread__members=request.user)
        
        if thread_id:
            qs=qs.filter(thread=thread_id).order_by('created_at')
        

        paginator=PageNumberPagination()
        paginator.page_size=100
        paginated_qs=paginator.paginate_queryset(qs,request)

        serializer=MessagesSerializer(paginated_qs,many=True)
        return paginator.get_paginated_response(serializer.data)
    
    def create(self,request):
        serializer=MessagesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(sender=request.user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    def retrieve(self,request,pk=None):
        qs=Messages.objects.all()
        Message=get_object_or_404(qs,pk=pk)
        serializer=MessagesSerializer(Message)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def update(self,request,pk=None):
        qs=Messages.objects.all()
        Message=get_object_or_404(qs,pk=pk)
        serializer=MessagesSerializer(Message,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    def partial_update(self,request,pk=None):
        qs=Messages.objects.all()
        Message=get_object_or_404(qs,pk=pk)
        serializer=MessagesSerializer(Message,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    def destroy(self,request,pk=None):
        qs=Messages.objects.all()
        Message=get_object_or_404(qs,pk=pk)
        Message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)