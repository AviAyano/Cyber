
if __name__ == '__main__':

    import socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ("0.0.0.0", 8820)

server_socket.bind(server_address)

server_socket.listen()
print("Server is up and running")

(client_socket, client_address) = server_socket.accept()
print("Client connected")

data = client_socket.recv(1024).decode()
print("Client sent:",data,sep=" ")
data = data + "\nEverything is good !!! ... how are you? "
client_socket.send(data.upper().encode())
client_socket.close()
server_socket.close()


