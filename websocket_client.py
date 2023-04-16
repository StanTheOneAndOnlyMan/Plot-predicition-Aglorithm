import websocket
from enum import Enum
import json

from helpers.websocket_helper import WebSocketResult
from main import simanneal_calculation
from main import mlrose_calculation
import helpers.matplot_tools as mplt
from helpers.converter import format_input


class WebSocketActions(Enum):
    SIMANNEAL_CALCULATE = 1
    MLROSE_CALCULATE = 2

def unpackMessage(message):
    json_object = json.loads(message)
    plot = json_object["corners"]
    obstacle = json_object["obstacle"]
    if("algorithm" in str(json_object)):
        return WebSocketActions(json_object["algorithm"]), plot, obstacle
    else:
        return 0, plot, obstacle


def switch(action, plot, obstacle):
    if action != WebSocketActions.MLROSE_CALCULATE:
        simanneal_calculation(plot, obstacle)
    if action != WebSocketActions.SIMANNEAL_CALCULATE:
        mlrose_calculation(plot, obstacle)

websocket.enableTrace(True)

# Connecting to websocket
ws = websocket.create_connection("ws://localhost:8083/prediction", header={"client": "algorithm"})

# # Sending some message
# ws.send("Hello there")

while True:
    print("Receiving data: ")
    algo, plot, obstacle = unpackMessage(ws.recv())
    switch(algo, plot, obstacle)