
graph_size = int(input())
graph = []

for i in range(graph_size):
    graph.append(list(map(int, input().split(' '))))

print(graph[1])