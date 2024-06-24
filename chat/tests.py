# tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from .models import ChatRoom, Message

class ChatRoomModelTest(TestCase):
    def setUp(self):
        # Set up initial data
        self.chatroom = ChatRoom.objects.create(name="Test Room")

    def test_chatroom_creation(self):
        self.assertEqual(self.chatroom.name, "Test Room")
        self.assertIsInstance(self.chatroom.created_at, datetime)
        self.assertIsInstance(self.chatroom.updated_at, datetime)

    def test_chatroom_str_method(self):
        self.assertEqual(str(self.chatroom), "Test Room")

class MessageModelTest(TestCase):
    def setUp(self):
        # Set up initial data
        self.chatroom = ChatRoom.objects.create(name="Test Room")
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.message = Message.objects.create(text="Hello, World!", ChatRoom=self.chatroom, user=self.user)

    def test_message_creation(self):
        self.assertEqual(self.message.text, "Hello, World!")
        self.assertEqual(self.message.ChatRoom, self.chatroom)
        self.assertEqual(self.message.user, self.user)
        self.assertIsInstance(self.message.created_at, datetime)
        self.assertIsInstance(self.message.updated_at, datetime)

    def test_message_str_method(self):
        expected_string = "Hello, World!-testuser"
        self.assertEqual(str(self.message), expected_string)
