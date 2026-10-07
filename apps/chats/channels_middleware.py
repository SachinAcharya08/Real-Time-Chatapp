from channels.middleware import BaseMiddleware
from urllib.parse import parse_qs
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import TokenError
from channels.db import DatabaseSyncToAsync
from django.contrib.auth import get_user_model


@DatabaseSyncToAsync
def get_user(user_id):
    User=get_user_model()
    return User.objects.get(id=user_id)

class JWTWebSocketMiddleware(BaseMiddleware):
    def __init__(self, inner):
        self.inner=inner

    async def __call__(self, scope, receive, send):
        query_string=scope['query_string'].decode()
        query_params=parse_qs(query_string)
        token=query_params.get("token",[None])[0]
        if token is None:
            await send({
                "type":"websocket.close",
                "code":4001,
            })
            return

        try:
            access_token=AccessToken(token)

        except TokenError:
            await send({
                "type":"websocket.close",
                "code":4001,
            })
            return
        user_id = access_token['user_id']
        user=await get_user(user_id)
        scope['user']=user

        await self.inner(scope,receive,send)

