import socket
import random

# 服务器配置
SERVER_HOST = 'localhost'
SERVER_PORT = 8002

PACKET_LOSS_RATE = float(input("请输入丢包率: "))


# 创建一个TCP套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)

print("服务器已启动。监听 {}:{}".format(SERVER_HOST, SERVER_PORT))

while True:
    # 等待客户端连接
    client_socket, client_address = server_socket.accept()
    print("客户端已连接:", client_address)

    packet_loss_count = 0

    # 接收要发送的数据包数量
    num_packets = int(client_socket.recv(1024).decode())
    print("要发送的数据包数量:", num_packets)

    for i in range(num_packets):
        try:
            # 接收消息
            message = client_socket.recv(1024)

            if message:
                print("接收到来自客户端的消息:", message.decode())

                # 模拟丢包
                if random.random() < PACKET_LOSS_RATE:
                    print("数据包丢失，序列号:", message.decode())
                    packet_loss_count += 1
                else:
                    # 发送确认消息
                    client_socket.sendall(message)
                    print("发送确认消息:", message.decode())

            else:
                # 客户端关闭连接
                print("客户端已断开连接:", client_address)
                break

        except socket.error as e:
            print("接收消息时发生错误:", e)
            break

    # 计算丢包率
    packet_loss_rate = packet_loss_count / num_packets

    # 发送丢包率给客户端
    client_socket.sendall(str(packet_loss_rate).encode())

    # 关闭连接
    client_socket.close()

# 关闭套接字
client_socket.close()
server_socket.close()