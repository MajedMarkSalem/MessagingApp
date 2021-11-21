from rest_framework import viewsets

from .serializers import MessageSerializer
from .models import Message

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .messagingServices import UpdateIsRead, DeleteMessage, GetMessage, GetMessagesList, GetUnreadMessages


@api_view(['GET', 'POST'])
def NewMessagesList(request):

    if request.method == 'GET':
        messages = GetUnreadMessages()
        for item in messages:
            UpdateIsRead(item.pk)
        
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','DELETE'])
def MessageObject(request, pk):
    try:
        message = GetMessage(pk)
    except Message.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MessageSerializer(message, many=True)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        DeleteMessage(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def AllMessages(request):
    if request.method == 'GET':
        mesList = GetMessagesList()
        serializer = MessageSerializer(mesList, many=True)
        return Response(serializer.data)
