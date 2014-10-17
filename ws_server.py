#!/usr/bin/env python3
#
# example from http://aaugustin.github.io/websockets/

import asyncio
import websockets


@asyncio.coroutine
def hello(websocket, path):
    name = yield from websocket.recv()
    print("< {}".format(name))
    greeting = "Hello {}!".format(name)
    yield from websocket.send(greeting)
    print("> {}".format(greeting))

# Normally websockets go over regular HTTP(S) ports (80/443), but we want
# to be able to run this example as non-root, so we use a high-numbered port.
start_server = websockets.serve(hello, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
