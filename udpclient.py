# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 13:06:41 2022

@author: afaan
"""

import socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
localhost = '127.0.0.1'
localport = 20001
buffer_size = 4096
msg = 'Hello UDP Server'
client_socket.sendto(msg.encode("utf-8"),(localhost,localport))
data,addr = client_socket.recvfrom(buffer_size)
print('Server: '+str(data))
client_socket.close()