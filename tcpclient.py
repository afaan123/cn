# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 13:08:33 2022

@author: afaan
"""

from pydoc import cli
import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
localhost='127.0.0.1'
port=20001
buffer_size=4096
client.connect((localhost,port))

message=input('Enter Message: ')
client.send(bytes(message,'utf-8'))
data=client.recv(buffer_size)
data=data.decode('utf-8')
print(data)
client.close()