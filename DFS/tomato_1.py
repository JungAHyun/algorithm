from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)  # 재귀 허용 깊이를 수동으로 늘려주는 코드

def bfs():
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            x2 = dx[i] + x
            y2 = dy[i] + y

            if 0 <= x2 and x2 < width and 0 <= y2 and y2 < length and graph[x2][y2] == 0:

                graph[x2][y2] = graph[x][y] + 1
                q.append([x2, y2])


width, length = map(int, input().split(' '))
graph = []
cnt = 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]              #방향 리스트
q = deque([])

for i in range(length):
    tomato = list(map(int, input().split(' ')))
    graph.append(tomato)

#토마토 있는 위치를 큐에 저장
for i in range(length):
    for j in range(width):
        if  graph[i][j] == 1:   
            q.append([i , j])

bfs()
for i in graph:
    for j in i:
        # 다 찾아봤는데 토마토를 익히지 못했다면 -1 출력
        if j == 0:
            print(-1)
            exit(0) 
    cnt = max(cnt, max(i))

# 처음 시작을 1로 표현했으니 1을 빼준다.
print(cnt - 1)
