import torch
import time
import sys
import socketio
from flask import Flask, render_template
from flask_socketio import SocketIO, emit, Namespace
from transformers import T5ForConditionalGeneration, T5Tokenizer, LogitsWarper

app = Flask(__name__)
app.config["SOCKET_KEY"] = 'secret'
socketio = SocketIO(app, cors_allowed_origins="*")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class CallbackLogitsWarper(LogitsWarper):
    def __init__(self, tokenizer, callback, sid):
        self.tokenizer = tokenizer
        self.callback = callback
        self.sid = sid
        self.tokens = []
    
    def __call__(self, input_ids: torch.Tensor, scores: torch.Tensor) -> torch.FloatTensor:
        self.tokens.append(input_ids[0][-1])
        result = self.tokenizer.decode(input_ids[0][-1], skip_special_tokens=True)
        self.callback(result, self.sid)
        return scores

def callback(result):
    socketio.emit("response", result)


def load_model(model="google/flan-t5-xl"):
    tokenizer = T5Tokenizer.from_pretrained(model)
    model = T5ForConditionalGeneration.from_pretrained(model, device_map="auto")
    return model, tokenizer


class CustomNamespace(Namespace):
    def on_connect(self):
        print("Client Connected")
    
    def on_disconnect(self):
        print("Clinet Disconnected")
    
    def predict(self, sid, prompt, model, tokenizer):
        t1 = time.time()
        input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(device)
        result = model.generate(input_ids, 
                                 max_new_tokens=256,
                                 logits_processor=[CallbackLogitsWarper(tokenizer, callback, sid)])
        t2 = time.time()
        print(f"Time taken: {t2-t1}")

    def on_get_result(self, data):
        prompt = data.get("prompt")
        sid = data.get('sid')
        self.emit('response', '<end>')

socketio.on_namespace(CustomNamespace('/'))

if __name__=="__main__":
    model = load_model()
    app.debug = True
    socketio.run(app)

