from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)  # 재귀 허용 깊이를 수동으로 늘려주는 코드

def bfs(start):
    global cnt
    q = deque()
    visited[start] = 1
    q.append(start)
    result[start] = cnt
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                cnt += 1
                visited[i] = 1
                q.append(i)
                result[i] = cnt


n = int(input())
m = int(input())

visited = [0] * (n + 1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

result = [0] * (n + 1)

cnt = 0
bfs(1)

print(cnt)