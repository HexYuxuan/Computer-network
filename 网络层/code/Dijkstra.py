import heapq

def dijkstra_algorithm(graph, start):
    # 初始化距离列表,路径列表
    num_nodes = len(graph)
    distances = [float('inf')] * num_nodes
    distances[start] = 0
    visited = [False] * num_nodes
    paths = [[] for _ in range(num_nodes)]
    paths[start] = [start]

    # 利用heap判断节点是否都加入
    heap = [(0, start)]
    while heap:
        current_distance, current_node = heapq.heappop(heap)
        visited[current_node] = True

        for neighbor, weight in graph[current_node]:
            if not visited[neighbor]:
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    paths[neighbor] = paths[current_node] + [neighbor]
                    heapq.heappush(heap, (new_distance, neighbor))

    return distances, paths

# 测试图结构和起始节点
graph = [
    [(1, 1), (3, 6)],
    [(0, 1), (2, 3), (3, 4)],
    [(1, 3), (3, 2), (4, 6)],
    [(0, 6), (1, 4), (2, 2), (4, 9), (5, 2)],
    [(2, 6), (3, 9)],
    [(3, 2)]
]
print("请输入初始节点：")
start_node = input()
start_node = int(start_node)

# 使用Dijkstra算法计算最短路径和距离
distances, paths = dijkstra_algorithm(graph, start_node)

# 打印最短路径和距离
print("最短距离表：")
for i, distance in enumerate(distances):
    print(f"节点 {start_node} 到节点 {i} 的最短距离为：{distance}")

print("最短路径表：")
for i, distance in enumerate(distances):
    print(f"节点 {start_node} 到节点 {i} 的最短路径为：{paths[i]}")
