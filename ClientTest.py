#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = '192.168.0.19'       # Get local machine name
port = 11111                # Reserve a port for your service.

s.connect((host, port))

print ("Connected to server")

while True:
  msg = input("CLIENT >> ")
  s.send(msg.encode())
  msg = s.recv(1024)
  print ("SERVER >> ", msg.decode())
