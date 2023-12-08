# SimpleClientServerChat - Client
# Author: Sarah Kugelmas

import socket

# create socket
Client_sock = socket.socket()

# server info
host_IP = "127.0.0.1"
host_port = 63365

# confirms that client is running and accepting input messages
print("Waiting for response...")

# try to connect to socket, catch connection errors
try:
    Client_sock.connect((host_IP,host_port))
except socket.error as err:
    print(str(err))

response = Client_sock.recv(1024)
while True:
    # wait for user input and send to server
    Input = input("> ")
    Client_sock.send(str.encode(Input))
    response = Client_sock.recv(1024)
    print(response.decode('utf-8'))

Client_sock.close()
