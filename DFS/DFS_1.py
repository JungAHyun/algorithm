

import sys
sys.setrecursionlimit(10**7)

n, m, r = map(int, input().split(' '))
graph=[[] for _ in range(n+1)]

# for i in range(m):
#     graph.append(list(map(int, input().split(' '))))

#연결된 노드 입력 받기
for i in range(m):
    u,v = map(int, input().split(' '))
    graph[u].append(v)
    graph[v].append(u)

#오름차순 정리
for i in range(n+1):
    graph[i].sort()

visited = [0]*(n+1)
cnt = 1

def dfs(graph, visited, v):   
    global cnt    
    
    visited[v] = cnt;                   
    for i in graph[v]:                        
        if visited[i]==0:
            #순차 증가
            cnt+=1
            #dfs 실행
            dfs(graph,visited,i)

dfs(graph, visited, r)


for i in range(n+1):
    if i!=0:
        print(visited[i])
