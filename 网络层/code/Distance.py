import numpy as np

# 初始化路由表
def initialize_routing_table(topology, start_node):
    num_nodes = len(topology)
    inf = float('inf')

    routing_table = np.zeros((num_nodes, 2))
    routing_table[:, 0] = start_node
    routing_table[:, 1] = inf
    routing_table[start_node, 1] = 0

    return routing_table

# 利用距离矢量算法计获取路由表
def distance_vector_iteration(topology, routing_table):
    num_nodes = len(topology)
    inf = float('inf')

    distance_vector = routing_table[:, 1]

    # 检验是否收敛，如不收敛则需要更新
    convergence = False
    while not convergence:
        convergence = True
        for node in range(num_nodes):
            min_distance = inf
            min_neighbor = None
            for neighbor in range(num_nodes):
                if neighbor != node and topology[node][neighbor] + distance_vector[neighbor] < min_distance:
                    min_distance = topology[node][neighbor] + distance_vector[neighbor]
                    min_neighbor = neighbor
            if min_distance < distance_vector[node]:
                distance_vector[node] = min_distance
                routing_table[node, 0] = min_neighbor
                routing_table[node, 1] = min_distance
                convergence = False

    return routing_table

# 获取最短路由路径
def get_distance_and_path(routing_table, start_node):
    num_nodes = len(routing_table)
    distance_list = routing_table[:, 1]
    path_list = []

    for i in range(num_nodes):
        if i != start_node:
            distance = distance_list[i]
            path = [i]
            while path[-1] != start_node:
                next_hop = int(routing_table[path[-1], 0])
                path.append(next_hop)
            path_list.append((distance, path[::-1]))



    return distance_list, path_list

# 获取拓扑表和初始节点
topology = [
    [0, 1, float('inf'), 3, float('inf'), float('inf')],
    [1, 0, 3, 4, float('inf'), float('inf')],
    [float('inf'), 3, 0, 2, 6, float('inf')],
    [6, 4, 2, 0, 9, 2],
    [float('inf'), float('inf'), 6, 9, 0, float('inf')],
    [float('inf'), float('inf'), float('inf'), 2, float('inf'), 0]
]
print("请输入初始节点:")
start_node = input()
start_node = int(start_node)

# 初始化路由表
routing_table = initialize_routing_table(topology, start_node)

# 进行距离向量迭代
routing_table = distance_vector_iteration(topology, routing_table)

# 输出指定节点到其他节点的距离列表和路径
distance_list, path_list = get_distance_and_path(routing_table, start_node)

# 打印距离列表和路径
print(f"节点 {start_node} 到其他节点的距离列表：")
for i in range(len(distance_list)):
    print(f"到节点 {i} 的距离：{distance_list[i]}")

print(f"\n节点 {start_node} 到其他节点的路径：")
for i in range(len(path_list)):
    distance, path = path_list[i]
    print(f"到节点 {i} 的距离：{distance}，路径：{path}")