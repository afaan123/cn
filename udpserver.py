# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 13:07:49 2022

@author: afaan
"""

import socket
server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

localhost = '127.0.0.1'
localport = 20001
buffer_size = 4096
server_socket.bind((localhost,localport))

while True:
    data,addr = server_socket.recvfrom(buffer_size)
    print(str(data))
    msg = "Hello UDP Client".encode('utf-8')
    server_socket.sendto(msg,addr)