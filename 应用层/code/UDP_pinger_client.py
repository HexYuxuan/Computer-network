import socket
import time
import random
server_host = 'localhost'
server_port = 9865

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 设置等待时间
client_socket.settimeout(1)

# 设置发送数量
ping_count = 10
# 为了模拟出错，这里设置一个出错率
error_rate = 0.3
for sequence_number in range(1, ping_count + 1):
    send_time = time.time()
    message = f'Ping {sequence_number} {send_time}'

    # 创建一个随机数，将它与出错率比较
    if random.random() < error_rate:
        # 如果随机数比出错率小，那么这条信息就会被模拟为出错
        message += ' (Error)'

    try:
        client_socket.sendto(message.encode(), (server_host, server_port))
        response, server_address = client_socket.recvfrom(1024)
        receive_time = time.time()
        rtt = receive_time - send_time
        print(f'Response : {response.decode()}')
        print(f'RTT: {rtt:.6f} seconds')
    except socket.timeout:
        print(f'Request timed out for Ping {sequence_number}')

client_socket.close()