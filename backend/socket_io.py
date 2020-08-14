import socketio
from tools import get_all_info
from discover import  discover_handler
from flask import Flask
import json

sio=socketio.Server(async_mode='threading',cors_allowed_origins='*')
app=Flask(__name__)
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app,)


@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def devices(sid,data):
    devices=get_all_info()
    sio.emit('devices_response ',{"data":devices})
@sio.event
def discover(sid,data):
    ip =data['subnet']
    devices=discover_handler(ip)
    sio.emit('discover_response',{"data":json.loads(devices)})

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    app.run(threaded = True)



