import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ("127.0.0.1", 8820)
client_socket.connect(server_address)

def client(the_client_chose):
    print("The client send : ", the_client_chose, sep=" ")

    client_socket.send(the_client_chose.encode())
    data = client_socket.recv(1024).decode()
    print("The server sent :", data, sep=" ")


do_continue = True
while do_continue:
    client_input = input("\nPlease enter your choice [number]:\n 1. What's up ping \n 2. Time \n 3. Rand \n 4. Name \n 5. Quit \n")
    if client_input == '1':
        the_client_chose = "What's up ?"
        client(the_client_chose)
    elif client_input == '2':
        the_client_chose = "TIME"
        client(the_client_chose)
    elif client_input == '3':
        the_client_chose = "RAND"
        client(the_client_chose)
    elif client_input == '4':
        the_client_chose = "NAME"
        client(the_client_chose)
    elif client_input == '5':
        the_client_chose = "Quit"
        print("The client sent : ", the_client_chose, sep=" ")
        client_socket.send(the_client_chose.encode())
        do_continue = False
        client_socket.close()
