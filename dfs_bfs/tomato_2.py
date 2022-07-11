from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)  # 재귀 허용 깊이를 수동으로 늘려주는 코드

def bfs():
    while q:
        z, y, x = q.popleft()

        for i in range(6):
            z2 = z + dz[i] 
            x2 = x + dx[i] 
            y2 = y + dy[i] 

            if (0 <= x2 and x2 < width) and (0 <= y2 and y2 < length) and (0 <= z2 and z2 < height) and graph3D[z2][y2][x2] == 0:
                graph3D[z2][y2][x2] = graph3D[z][y][x] + 1
                q.append([z2,y2, x2])


width, length, height = map(int, input().split(' '))
graph3D= [[] for _ in range(height)]
cnt = 0
dx, dy, dz= [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]             #방향 리스트
q = deque()

for h in range(height):
    graph = []
    for len in range(length):
        graph.append(list(map(int, input().split(' '))))
    graph3D[h] = graph


print(graph3D)

#토마토 있는 위치를 큐에 저장
for z in range(height):
    for y in range(length):
        for x in range(width):
            if  graph3D[z][y][x] == 1:   
                q.append([z,y,x])

bfs()

for i in graph3D:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        cnt = max(cnt, max(j))
        print(cnt)

print(cnt - 1)
