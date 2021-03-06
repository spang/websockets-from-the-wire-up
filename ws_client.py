#!/usr/bin/env python
#
# example from http://aaugustin.github.io/websockets/

import asyncio
import websockets


@asyncio.coroutine
def hello():
    websocket = yield from websockets.connect('ws://localhost:8765/')
    name = input("What's your name? ")
    yield from websocket.send(name)
    print("> {}".format(name))
    greeting = yield from websocket.recv()
    print("< {}".format(greeting))
    # let proper cleanup happen before exiting
    yield from asyncio.sleep(0.1)

asyncio.get_event_loop().run_until_complete(hello())
