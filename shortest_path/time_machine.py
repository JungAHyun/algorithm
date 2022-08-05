

import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

city, bus = map(int, input().split(' '))

graph= [[] for _ in range(city+1)]
shortest_time  = [INF]* (city+1)  

for _ in range(bus):
    a, b, c = map(int, input().split(' '))  #a:출발도시, b: 도착도시 c: 시간
    graph[a].append((b,c))


def shortest_path(start):
    q = []
    shortest_time[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        now_time, now_node = heapq.heappop(q)

        if now_time < 0:
            shortest_time[now_node] = -1
            break

        if now_time == 0:
            shortest_time[now_node] = 0

        # 현재 노드에 저장된 시간이 더 짧으면 넘긴다.
        if now_time > shortest_time[now_node]:
            continue
        
        #현재 노드와 연결된 다른 노드로 가는 시간 확인한다.
        for g in graph[now_node]:
            time = now_time + g[1]
            #저장된 시간보다 현재 노드를 거쳐가는 시간이 더 짧은경우 값 변경
            if time < shortest_time[g[0]]:
                shortest_time[g[0]] = time
                heapq.heappush(q, (time, g[0])) 
            


shortest_path(1)

if  -1 in shortest_time :
    print('-1')
else:
    for i in range(2, city+1):
        if shortest_time[i]>=100000000:
            print('-1')
        else:
            print(shortest_time[i])



