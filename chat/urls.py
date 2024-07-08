from chat.viewsets import ChatRoomViewSets,MessageViewSets
from rest_framework.routers import DefaultRouter
from chat.views import sumNumbers
from django.urls import path
from chat.views import sumNumbersView
from chat.viewsets import ChatRoomViewSets, MessageViewSets

router = DefaultRouter()
router.register(r'chatroom', ChatRoomViewSets, basename = 'chatroom')
router.register(r'message', MessageViewSets, basename = 'message')
urlpatterns = router.urls
urlpatterns += [
    path('sum_numbers/', sumNumbersView, name='sum_numbers'),
]