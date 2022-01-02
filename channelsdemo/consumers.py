import json
import random
from time import sleep

from channels.generic.websocket import WebsocketConsumer


class NumberGenerator(WebsocketConsumer):

    def connect(self):
        self.accept()

        while True:
            data = {
                'number': random.randint(1, 1000)
            }

            self.send(json.dumps(data))

            sleep(1)

    def disconnect(self, code):
        print("Socket disconnected with code", code)
