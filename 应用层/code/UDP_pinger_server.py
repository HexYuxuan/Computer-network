import socket

server_host = 'localhost'  # Change this to the server IP or hostname
server_port = 9865  # Change this to the server port

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_host, server_port))

print(f'Server listening on {server_host}:{server_port}...')

while True:
    message, client_address = server_socket.recvfrom(1024)
    response = f'Pong {message.decode()}'
    server_socket.sendto(response.encode(), client_address)