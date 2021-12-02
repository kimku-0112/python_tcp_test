
import socket 
import string
from _thread import *

HOST = '127.0.0.1'
PORT = 9999

def threaded(client_socket, addr): 
    print('Connected', addr[0], ':', addr[1]) 
    while True: 
        try:
            data = client_socket.recv(1024).decode()
            if not data: 
                print('Disconnected')
                break

            print(data)
            data_list = data.split()
            try:
                print('cmd : ' + data_list[0])
                print('param name : ' + data_list[1])
                print('depallet : ' + data_list[2])
                print('mirrored : ' + data_list[3])
                print('mixed : ' + data_list[4])
                print('object type : ' + data_list[5])
                print('object size : ' + data_list[6] + '/' + data_list[7] + '/' + data_list[8] )
                print('pallet size : ' + data_list[9] + '/' + data_list[10] + '/' + data_list[11])
                print('pallet pose : ' + data_list[12] + '/' + data_list[13] + '/' + data_list[14])
                print('box Quantity : ' + data_list[15] + '/' + data_list[16] + '/' + data_list[17])
            except:
                print("packet parsing error")
            client_socket.send(data.encode()) 
            try:
                client_socket.send(('   cmd : ' + data_list[0]).encode())
                client_socket.send(('   param name : ' + data_list[1]).encode())
                client_socket.send(('   depallet : ' + data_list[2]).encode())
                client_socket.send(('   mirrored : ' + data_list[3]).encode())
                client_socket.send(('   mixed : ' + data_list[4]).encode())
                client_socket.send(('   object type : ' + data_list[5]).encode())
                data_list[8] = str(int(data_list[8])+500)
                client_socket.send(('   object size : ' + data_list[6] + '/' + data_list[7] + '/' + data_list[8] ).encode())
                client_socket.send(('   pallet size : ' + data_list[9] + '/' + data_list[10] + '/' + data_list[11]).encode())
                client_socket.send(('   pallet pose : ' + data_list[12] + '/' + data_list[13] + '/' + data_list[14]).encode())
                client_socket.send(('   box Quantity : ' + data_list[15] + '/' + data_list[16] + '/' + data_list[17]).encode())
                
            except:
                print("packet parsing error")

        except ConnectionResetError as e:
            print('Disconnected')
            break
             
    client_socket.close() 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT)) 
server_socket.listen() 

print('server start')

while True: 

    print('wait')
    client_socket, addr = server_socket.accept() 
    start_new_thread(threaded, (client_socket, addr)) 

server_socket.close()