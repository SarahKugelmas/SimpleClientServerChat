import socket
import os
from _thread import *

# create socket
Server_sock = socket.socket()

# initialize server ip and port
host_IP = "127.0.0.1"
host_port = 63365

# bind using server info and check for socket connection error
try:
    Server_sock.bind((host_IP,host_port))
except socket.error as err:
    print(str(err))

# confirms server is running and listening
print("Listening...")
Server_sock.listen(5)

# client connections
def multi_thread_client(connection):
    # confirms client is connected
    connection.send(str.encode("Server is listening..."))
    # receive and send back response from client
    while True:
        message = connection.recv(2048)
        response = message.decode('utf-8')
        if not message:
            break
        connection.sendall(str.encode(response))
    connection.close()

# continue accepting clients in socket
while True:
    Client, address = Server_sock.accept()
    print("Connected to IP " + address[0] + " at port number " + str(address[1]))
    start_new_thread(multi_thread_client,(Client, ))

Server_sock.close()
