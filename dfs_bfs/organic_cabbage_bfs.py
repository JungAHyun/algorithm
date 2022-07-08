from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)  

test = int(input())
result = []
dx, dy = [-1,1,0,0,], [0,0,-1,1]


def bfs(y,x):
    q.append((y,x))
    while q:
        y,x = q.popleft()
        while i in range(4):
            nx = x +dx[i]
            ny = y + dy[i]

            if 0<=nx<width and 0<=ny<length and graph[ny][nx] ==1:
                graph[ny][nx] = 0
                q.append((ny, nx))



for __ in range(test):
    width, length, position = map(int, input().split(' '))
    graph = [[0 for _ in range(width)]] * length
    
    for _ in range(position):
        x,y = map(int, input().split(' '))
        graph[y][x] = 1  

    cnt = 0
    q = deque()
    for i in range(length):
        for j in range(width):
            if graph[y][x] == 1:
                bfs(i,j)
                cnt+1

    result.append(cnt)

print(result)