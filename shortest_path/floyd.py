#플로이드 워셜 알고리즘 사용하는 문제라고 생각

import sys
input = sys.stdin.readline
INF = int(1e9)


n = int(input())  #도시의 개수
m = int(input())  #버스의 개수

graph = [[INF]*(n+1) for _ in range(n+1)]

#자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split(' '))  #a:출발도시, b: 도착도시 c: 비용
    graph[a][b] = min(c, graph[a][b])

for k in range(1,n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b]==INF:
            graph[a][b]=0
        print(graph[a][b], end=' ')
    print()