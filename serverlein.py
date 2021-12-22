#!/usr/bin/env python3
#Krajina Luka
# serverlein
import socket

HOST = '' 
PORT = 8080    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    while True: #Client loop
        conn, addr = s.accept()
        with conn:
            print('Verbunden mit: ', addr)
            data = conn.recv(1024)  #GET / HTTP/1.1\r\nHost: localhost\r\n\r\n
            outdata = "HTTP/1.1 200 OK\r\n\r\n<html><body><h1>Hi BULME</h1></body></html>"
            outdataEncoded = outdata.encode()   #Nimmt standardmäßig utf-8 wenn nichts in encode() eingeschrieben wird
            print(outdataEncoded)
            conn.sendall(outdataEncoded)
            conn.close()