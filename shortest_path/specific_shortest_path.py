
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split(' '))  #n: 정점의 개수, m: 간선의 개수
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split(' '))
    graph[a].append((b,c))
    graph[b].append((a,c))

v1, v2 =  map(int, input().split(' '))  #반드시 거쳐야 하는 두 정점

def shortest_path(start):
    shortest_dis = [INF]*(n+1)
    q = []

    heapq.heappush(q, (0,start))
    shortest_dis[start] = 0
    
    while(q):
        dis, now = heapq.heappop(q)

        #지금 노드에 있는 거리가 더 짧으면 넘어감.
        if shortest_dis[now] < dis :
            continue
        
        # now 노드와 연결된 노드들 확인
        for i in graph[now]:
            cost = dis + i[1]
            # now 노드를 거쳐 가는 거리가 짧은 경우 변경
            if shortest_dis[i[0]] > cost:
                shortest_dis[i[0]] = cost

                #거리 변경된 사항 힙에 저장
                heapq.heappush(q,(cost, i[0]))

    
    return shortest_dis


shortest_dis_0 = shortest_path(1)     #1과 다른 정점과의 최소 거리
shortest_dis_1 = shortest_path(v1)    #v1과 다른 정점과의 최소 거리
shortest_dis_2 = shortest_path(v2)    #v2와 다른 정점과의 최소 거리


print(shortest_dis_0)
print(shortest_dis_1)
print(shortest_dis_0)

result_1 = shortest_dis_0[v1] + shortest_dis_1[v2] + shortest_dis_2[n]
result_2 = shortest_dis_0[v2] + shortest_dis_1[v2] + shortest_dis_1[n]

result = min(result_1,result_2)

if result >= 100000000:
    result = -1

print(result)





