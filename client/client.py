import socketio
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--prompt", type=str, required=True, help="Enter the prompt for model")
args = parser.parse_args()

sio = socketio.Client()

@sio.event
def connect():
    sid = sio.sid
    print(f"Connected : {sid}")

@sio.event
def response(data):
    print(f"Data: {data}")
    if data == "<end>":
        sio.disconnect()

sio.connect("http://localhost:8000")
sio.emit('get_result', {'prompt': args.prompt})
sio.wait()

