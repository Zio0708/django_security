# from channels.routing import ProtocolTypeRouter

# application = ProtocolTypeRouter({
#     # Empty for now (http->django views is added by default)
# })

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.conf.urls import url

from alert.consumers import MyConsumer, EchoConsumer

application = ProtocolTypeRouter({

    # WebSocket chat handler
    "websocket": AuthMiddlewareStack(
        URLRouter([
            # url("socket/alert/", MyConsumer),
            url("socket/alert/", EchoConsumer),
        ])
    ),

    # # Using the third-party project frequensgi, which provides an APRS protocol
    # "aprs": APRSNewsConsumer,

})
