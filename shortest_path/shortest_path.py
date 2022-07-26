
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m =  map(int, input().split(' '))  #n: 정점의 개수, m:간선의 개수
start = int(input())

graph = [[] for _ in range(n+1)]
distance  = [INF]* (n+1)   

for _ in range(m):
    a, b, c = map(int, input().split(' '))  #a에서 b로가는 가중치 c
    graph[a].append((b,c))


def shortest_path(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while(q):
        dis, now = heapq.heappop(q)

        if distance[now] < dis:
            continue
        for i in graph[now]:
            cost = dis + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


shortest_path(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])




