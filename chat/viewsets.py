
from rest_framework import viewsets
from .models import ChatRoom
from .serializers import ChatRoomSerializer

class ChatRoomViewSet(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer