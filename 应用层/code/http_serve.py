import socket
import os


def handle_request(client_socket):
    # 接收HTTP请求
    request = client_socket.recv(1024).decode()
    # 查找请求文件名
    file_name = request.split()[1][1:]
    # 查看文件是否存在
    if os.path.isfile(file_name):
        # 查询文件内容
        with open(file_name, 'rb') as file:
            file_data = file.read()
        # 创建回应信息
        response = b'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n' + file_data
    else:
        # 如果文件不存在，返回“404 NOT Found”的信息
        response = b'HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n404File Not Found'
    # 返回回应
    client_socket.sendall(response)
    # 关闭连接
    client_socket.close()


def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(1)
    print('Server listening on port 8080...')
    while True:
        client_socket, address = server_socket.accept()
        print('Received connection from:', address)
        handle_request(client_socket)


run_server()
