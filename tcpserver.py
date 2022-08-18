# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 13:08:54 2022

@author: afaan
"""

import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
localhost='127.0.0.1'
port=20001
buffer_size=4096
server.bind((localhost,port))
server.listen(5)

while True:
    client,addr=server.accept()
    print('Connection Established ',addr[0],":",addr[1])
    message=client.recv(buffer_size)
    message=message.decode('utf-8')
    message=message.upper()
    message=message.encode('utf-8')
    client.send(message)
    client.close()