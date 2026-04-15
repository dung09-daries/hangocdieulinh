from flask import Flask
from threading import Thread
import os
import requests
import time

app = Flask('')

@app.route('/')
def main():
    return "Bot đang sống và tự ping!"

def run():
    # Render sẽ cấp một cổng qua biến PORT, mặc định là 8080 nếu chạy local
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

# Hàm tự gửi tín hiệu đến chính nó để Render không tắt bot
def self_ping():
    while True:
        try:
            # Dũng thay link này bằng link Web Service trên Render của bạn nhé
            # Ví dụ: https://hangocdieulinh.onrender.com
            requests.get("https://hangocdieulinh.onrender.com") 
            print("Đã tự ping để giữ bot tỉnh táo!")
        except Exception as e:
            print(f"Lỗi ping: {e}")
        
        time.sleep(300) # Nghỉ 5 phút (300 giây) rồi ping tiếp

def keep_alive():
    # Chạy Web Server
    server = Thread(target=run)
    server.start()
    
    # Chạy vòng lặp tự ping
    ping_thread = Thread(target=self_ping)
    ping_thread.start()
