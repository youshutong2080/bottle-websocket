# encoding: utf-8

from bottle import Bottle, run
from bottle.ext.websocket import GeventWebSocketServer
from bottle.ext.websocket import websocket


app = Bottle()


users = set()

@app.get('/websocket/', apply=websocket)
def websocket(ws):
    print ws
    users.add(ws)
    while True:
        msg = ws.receive()
        if msg:
            for u in users:
                u.send(msg)
                print u, msg
        else:
            break
    users.remove(ws)

run(app, host='0.0.0.0', port=8080, server=GeventWebSocketServer)