#플로이드 워셜 알고리즘 사용하는 문제

import sys
input = sys.stdin.readline
INF = int(1e9)


n = int(input())  #도시의 개수
m = int(input())  #버스의 개수

cost = [[INF]*(n+1) for _ in range(n+1)]

#자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            cost[a][b] = 0

#버스에 대한 정보를 받고 비용 초기화
for _ in range(m):
    a, b, c = map(int, input().split(' '))  #a:출발도시, b: 도착도시 c: 비용
    cost[a][b] = min(c, cost[a][b])

#a에서 b로 바로 가는 비용과 k를 거쳐가는 비용 중 더 적은 비용으로  cost값 변경
for k in range(1,n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            cost[a][b] = min(cost[a][b], cost[a][k] + cost[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if cost[a][b]==INF:
            cost[a][b]=0
        print(cost[a][b], end=' ')
    print()