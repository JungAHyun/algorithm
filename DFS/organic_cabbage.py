from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)  

def dfs(y,x):
    if x <= -1 or x >= width or y <= -1 or y >= length: 
        return False

    if graph[y][x] == 1: 
        graph[y][x] = 0 
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
        graph[y][x] = 1  

        cnt = 0

        for i in range(length):
            for j in range(width):
                if dfs(i, j)  == True:   
                    cnt+=1

    result.append(cnt)
    
for i in result:
    print(i)