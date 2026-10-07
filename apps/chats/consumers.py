from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.db import database_sync_to_async
from apps.chats.models import Threads,Messages

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user=self.scope['user']
        self.thread_id=self.scope['url_route']['kwargs']['thread_id']
        self.thread_name=f"thread_{self.thread_id}"


        if not self.user.is_authenticated:
            await self.close(code=4401)
            return

        if not await self.is_member():
            await self.close(code=4403)
            return

        await self.channel_layer.group_add(
            self.thread_name,
            self.channel_name
        )
        await self.accept()
       
    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.thread_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data=json.loads(text_data)
        message=data['content']

        saved_message = await self.save_message(message)

        
        await self.channel_layer.group_send(
            self.thread_name,
            {
                "type":"chat_message",
                "message": message,
                "sender_id": self.user.id,
                "sender_name":self.user.get_username(),
                "created_at":saved_message.created_at.isoformat(),
            }
        )
        
    async def chat_message(self,event):
        await self.send(text_data=json.dumps(
            {
                "content":event["message"],
                "sender_id":event["sender_id"],
                "sender_name":event["sender_name"],
                "created_at":event["created_at"]
            }

        ))

    @database_sync_to_async
    def is_member(self):
        return Threads.objects.filter(id=self.thread_id,members=self.user).exists()

    @database_sync_to_async
    def save_message(self,message):
        return Messages.objects.create(
            sender=self.user,
            thread_id=self.thread_id,
            content=message
        )


            