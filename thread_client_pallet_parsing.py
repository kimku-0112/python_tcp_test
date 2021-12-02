import socket
import time
from _thread import *

HOST = '127.0.0.1'  
PORT = 9999       

def thread(clientsocket): 
    while True:
        data = clientsocket.recv(1024)
        if not data: 
            print('Disconnected')
            break
        print('Received', repr(data.decode()))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
start_new_thread(thread, (client_socket,)) 
while True:
    client_socket.sendall('palletizing test 0 1 1 box 10 20 30 40 50 60 70 80 90 100 110 120'.encode())
    time.sleep(1)

client_socket.close()