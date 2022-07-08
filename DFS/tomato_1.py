from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)  # 재귀 허용 깊이를 수동으로 늘려주는 코드

def dfs(y,x):
    if x <= -1 or x >= width or y <= -1 or y >= length: # 범위에 벗어난다면 제외
        return False
    if graph[y][x] == 1: # 배추가 심어진 부분이라면
        graph[y][x] = 0 # 방문처리
        # 상하좌우로 탐색
        dfs(y-1, x)
        dfs(y, x-1)
        dfs(y+1,x)
        dfs(y,x+1)
        return True
    return False


test = int(input())
result = []
for __ in range(test):
    width, length, position = map(int, input().split(' '))
    graph = [[0 for _ in range(width)]] * length

    for _ in range(position):
        x,y = map(int, input().split(' '))
        graph[y][x] = 1  #배추있음읕 표시

        cnt = 0

        for i in range(length):
            for j in range(width):
                if dfs(i, j)  == 1:   
                    cnt+=1
    result.append(cnt)
    
for i in result:
    print(i)