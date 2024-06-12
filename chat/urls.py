from mailbox import Message
from rest_framework.routers import DefaultRouter
from chat.viewsets import ChatRoomViewSet, MessageViewSet

router = DefaultRouter()
router.register('chatrooms', ChatRoomViewSet, basename = 'chatroom')
router.register('messages', MessageViewSet, basename = 'message')
urlpatterns = router.urls