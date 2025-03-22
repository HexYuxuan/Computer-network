import socket
import os

server_host = 'localhost'
server_port = 8973
file_directory = 'files/'

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_host, server_port))
server_socket.listen(1)

# 验证连接
print(f"Server listening on {server_host}:{server_port}...")

while True:
    connection_socket, client_address = server_socket.accept()

    filename = connection_socket.recv(1024).decode()
    filepath = file_directory + filename

    # 查询文件存在与否，存在就返回文件，不存在就返回不存在的信息
    if os.path.isfile(filepath):
        with open(filepath, 'rb') as file:
            file_data = file.read()
            connection_socket.send(file_data)
        print(f"File '{filename}' sent to {client_address[0]}")
    else:
        error_message = f"Error: File '{filename}' not found"
        connection_socket.send(error_message.encode())
        print(f"{error_message} sent to {client_address[0]}")

    connection_socket.close()