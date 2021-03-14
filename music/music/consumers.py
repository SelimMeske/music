from channels.consumer import SyncConsumer
from asgiref.sync import async_to_sync

class EchoCosnumer(SyncConsumer):


    def websocket_connect(self, event):
        self.send({
            "type": "websocket.accept",
            "text": "hi from server"
        })
        async_to_sync(self.channel_layer.group_add)("notify", self.channel_name)


    def websocket_disconnect(self, event):
        print('bye')

    def websocket_receive(self, event):
        self.send({
            "type": "websocket.send",
            "text": event['text']
        })

    def connect(self):
        print('connected')
        async_to_sync(self.channel_layer.group_add)("test", self.channel_name)

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)("test", self.channel_name)