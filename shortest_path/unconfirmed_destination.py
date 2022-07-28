
# g, h 두 지점을 지나 목적지 후보로 가능 경로가 최단경로인 것을 찾는 문제라고 생각.

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)


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


test_case= int(input())
result = [[] for _ in range(test_case)]

for i in range(test_case):
    n,m,t = map(int, input().split(' '))        #n: 정점의 개수(교차로), m: 간선의 개수(도로) t:목적지후보의 개수
    s,g,h = map(int, input().split(' '))      #s: 출발지, g,h: 반드시 거쳐야 하는 두 정점
    
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split(' '))
        graph[a].append((b,c))
        graph[b].append((a,c))
    

    #목적지 후보 리스트
    des = [] 
    for _ in range(t):
        des.append(int(input()))

    shortest_dis_s = shortest_path(s)     #s과 다른 정점과의 최소 거리 리스트
    shortest_dis_g = shortest_path(g)    #g과 다른 정점과의 최소 거리 리스트
    shortest_dis_h = shortest_path(h)    #h와 다른 정점과의 최소 거리 리스트
    

    #목적지 j로 가는 최소거리 구하기
    for d in des:
        result_1 = shortest_dis_s[g] + shortest_dis_g[h] + shortest_dis_h[d]  
        result_2 = shortest_dis_s[h] + shortest_dis_h[g] + shortest_dis_g[d]
        
        #g, h를 거쳐가는 경로가 목적지 후보로 가는 최소 거리인 경우 
        if result_1 == shortest_dis_s[d] or result_2 == shortest_dis_s[d]:
            result[i].append(d)

    result[i].sort()

for i in range(test_case):
    for j in range(len(result[i])):
        print(result[i][j], end = ' ')
    print()


        
        






