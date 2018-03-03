# from channels import Group
#
#
# def ws_connect(message):
#     Group('users').add(message.reply_channel)
#
#
# def ws_disconnect(message):
#     Group('users').discard(message.reply_channel)


from channels.consumer import SyncConsumer
from channels.generic.websocket import WebsocketConsumer


class EchoConsumer(SyncConsumer):

    def websocket_connect(self, event):
        self.send({
            "type": "websocket.accept",
        })

    def websocket_receive(self, event):
        self.send({
            "type": "websocket.send",
            "text": event["text"],
        })


class MyConsumer(WebsocketConsumer):
    groups = ["broadcast"]

    def connect(self):
        # Called on connection. Either call
        self.accept()
        # Or to reject the connection, call
        # self.close()

    def receive(self, text_data=None, bytes_data=None):
        # Called with either text_data or bytes_data for each frame
        # You can call:
        self.send(text_data="Hello world!")
        # Or, to send a binary frame:
        # self.send(bytes_data="Hello world!")
        # Want to force-close the connection? Call:
        # self.close()
        # Or add a custom WebSocket error code!
        # self.close(code=4123)

    def disconnect(self, close_code):
        a = 1
