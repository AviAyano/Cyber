import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ("127.0.0.1", 8820)
client_socket.connect(server_address)

client_socket.send("Whats up ?".encode())

data = client_socket.recv(1024).decode()
print("The server sent ", data, sep=" ")
client_socket.close()