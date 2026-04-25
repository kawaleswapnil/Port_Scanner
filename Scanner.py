#imported the socket module
import socket

#Storing the ip and port in a variable
ip = input("Enter the target ip : ")
s_port = int(input("Enter the Starting port : "))
end_port = int(input("Enter the end port : "))
open_count = 0

print(f"Scanning {ip} from {s_port} to {end_port}")

for port in range(s_port, end_port,+1):
        #created a TCP(AF_INET) socket using ipv4(sock_stram)
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(0.5)  #timeout after reaching out to the port

        #connect_ex tries to connect the socket to the host and port
        result = s.connect_ex((ip,port))

        if result == 0:
                print(f"Port {port} is open")
                open_count += 1

        #closed connection
        s.close()

print(f"Total open ports : {open_count}")
