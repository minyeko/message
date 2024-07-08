from chat.models import ChatRoom, Message
from chat.serializers import ChatRoomSerializer,MessageSerializer
from rest_framework import viewsets


class ChatRoomViewSets(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

class MessageViewSets(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer