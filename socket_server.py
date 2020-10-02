import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket.AF_INET -to use IPv4 and SOCK_STREAM - to use TCP -> TCP/IP

# server_socket.bind(("0.0.0.0", 8081) # 0.0.0.0 - to coonect to all IP addresses

server_socket.bind(("127.0.0.1", 8081))

server_socket.listen()

print("Waiting for connection");

connection_socket, address = server_socket.accept()

print("Client connected")
