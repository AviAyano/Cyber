import socket ,time, random


def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("0.0.0.0", 8820)

    server_socket.bind(server_address)

    server_socket.listen()
    print("Server is up and running")

    (client_socket, client_address) = server_socket.accept()
    print("Client connected")
    data = client_socket.recv(1024).decode()
    print("Client sent :", data, sep=" ")


    flag = True
    while (flag):
        if (data == "Quit"):
            data = "\n Bye Bye!"
            client_socket.send(data.encode())
            data = client_socket.recv(1024).decode()
            print("Client sent :", data, sep=" ")
            client_socket.close()
            flag = False
        elif (data == "NAME"):
            name = "SuperServer"
            data = "\nThe server name is :" + name
            client_socket.send(data.encode())
            data = client_socket.recv(1024).decode()
            print("Client sent :", data, sep=" ")

        elif (data == "TIME"):
            t = time.localtime()
            data = time.strftime("%H:%M:%S", t)
            client_socket.send(data.encode())
            data = client_socket.recv(1024).decode()
            print("Client sent :", data, sep=" ")

        elif (data == "RAND"):
            data = str(random.randrange(1, 10))
            client_socket.send(data.encode())
            data = client_socket.recv(1024).decode()
            print("Client sent :", data, sep=" ")


        elif ("What's up ?"):
            data = data + "\nEverything is good ?? \n;) pay attention to the menu ! "
            client_socket.send(data.encode())
            data = client_socket.recv(1024).decode()
            print("Client sent :", data, sep=" ")

    server_socket.close()


if __name__ == '__main__':
    run()
