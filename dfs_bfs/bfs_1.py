import sys
from collections import deque


def bfs(start):
    q = deque()
    visited[start] = 1
    q.append(start)
    cnt = 1
    result[start] = cnt
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                cnt += 1
                visited[i] = 1
                q.append(i)
                result[i] = cnt


n, m, R = map(int, sys.stdin.readline().split(' '))

visited = [0] * (n + 1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split(' '))
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

result = [0] * (n + 1)
bfs(R)

for i in result[1:]:
    print(i)