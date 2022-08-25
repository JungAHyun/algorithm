import sys
input = sys.stdin.readline

INF = int(1e9)
n,m = map(int, input().split(' ')) #n:마을 m: 도로



graph = [[INF]*(n+1) for _ in range(n+1)]


for _ in range(m):
    a,b,c = map(int, input().split(' '))
    graph[a][b] = c


for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0


for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

min_dist = INF

for a in range(1, n+1):
    for b in range(1 , n+1):
        if a==b:
            continue
        if min_dist > graph[a][b] + graph[b][a]:
            min_dist = graph[a][b] + graph[b][a]


if min_dist >= INF:
    print('-1')
else:
    print(min_dist)
