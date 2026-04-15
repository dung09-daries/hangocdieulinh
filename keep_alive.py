from flask import Flask
from threading import Thread
import os

app = Flask('')

@app.route('/')
def main():
    return "Bot đang sống!"

def run():
    # Render sẽ cấp một cổng ngẫu nhiên qua biến PORT
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

def keep_alive():
    server = Thread(target=run)
    server.start()