import socket
import random
import time
from datetime import datetime
import statistics

# 服务器配置
SERVER_HOST = 'localhost'
SERVER_PORT = 8002

# 创建一个TCP套接字
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))
client_socket.settimeout(1)  # 设置接收确认消息的超时时间

# 设置要发送的数据包数量
num_packets = int(input("请输入要发送的数据包数量: "))
client_socket.sendall(str(num_packets).encode())

packet_loss_count = 0
rtt_times = []

# 发送数据包到服务器
for i in range(num_packets):
    # 为数据包生成一个序列号
    sequence_number = str(i)

    # 发送数据包
    client_socket.sendall(sequence_number.encode())
    print("发送数据包，序列号:", sequence_number)

    try:
        # 启动计时器
        start_time = datetime.now()

        # 接收确认消息
        ack = client_socket.recv(1024)

        # 停止计时器
        end_time = datetime.now()

        # 记录接收到确认消息的时间
        rtt = (end_time - start_time).total_seconds()
        rtt_times.append(rtt)

        print("接收到确认消息:", ack.decode())
    except socket.timeout:
        print("超时，重新发送数据包，序列号:", sequence_number)
        packet_loss_count += 1

# 计算丢包率和平均RTT
packet_loss_rate = packet_loss_count / num_packets
if len(rtt_times) > 0:
    avg_rtt = statistics.mean(rtt_times)
else:
    avg_rtt = 0
    print("Error")

# 打印统计信息
print("\n----- 统计信息 -----")
print("丢包率:", packet_loss_rate)
print("平均RTT:", avg_rtt, "秒")

# 关闭套接字
client_socket.close()
