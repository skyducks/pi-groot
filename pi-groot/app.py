#!/usr/bin/env python
from flask import Flask, render_template, send_file
from picamera import PiCamera
import time

app = Flask(__name__)

@app.route('/')
def index():
    """Video streaming"""
    return render_template('index.html')

@app.route('/camera_capture')
def camera_capture():
    pic_path = '/tmp/captured.jpg'
    while True:
        try:
            with PiCamera() as camera:
                camera.start_preview()
                time.sleep(2)
                camera.capture(pic_path)
        except picamera.exc.PiCameraMMALError:
            time.sleep(10)
            continue
        break
    return send_file(pic_path, mimetype='image/jpg')

if __name__ == '__main__':
    app.run()