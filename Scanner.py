#imported the socket module
import socket

#Storing the ip and port in a variable
ip = "127.0.0.1"
port = 80

#created a TCP(AF_INET) socket using ipv4(sock_stram)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(1)  #timeout after reaching out to the port

#connect_ex tries to connect the socket to the host and port
result = s.connect_ex((ip,port))

if result == 0:
    print("open")
else :
    print("close")

#closed connection
s.close()
