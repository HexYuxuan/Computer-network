import socket

server_host = 'localhost'
server_port = 8973

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_host, server_port))

filename = input("Enter the filename: ")
client_socket.send(filename.encode())

response = client_socket.recv(1024)

if response[:5] != b"Error":
    with open(filename, 'wb') as file:
        file.write(response)
    print(f"File '{filename}' received")
else:
    print(response.decode())

client_socket.close()