# encoding=utf-8
import websocket
import subprocess

ws = websocket.create_connection("ws://localhost:8080/websocket/")

def tailLog(filepath):
    cmd = "/usr/bin/tail -f {filepath}".format(filepath=filepath)
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    while True:
        line = popen.stdout.readline().strip()
        if line:
            ws.send(line)
            print line


if __name__ == '__main__':
    filepath="/usr/local/var/log/nginx/access.log"
    tailLog(filepath)
