import sys
input = sys.stdin.readline

INF = int(1e9)
n,m = map(int, input().split(' ')) #n:마을 m: 도로

dist = [[INF] for _ in range(n)]    #최단거리 테이블
edge =  [[] * 3 for _ in range(n)]  #간선의 정보를 저장하는 리스트

for i in range(m):
    a, b, c  = map(int, input().split(' '))
    edge[i][0].append(a)
    edge[i][1].append(b)
    edge[i][2].append(c)
    

def bf(start):
    dist[start] = 0

    for i in range(n):
        for j in range(m):
            node = edge[j][0]
            next_node = edge[j][1]
            cost = edge[j][2]

            if dist[node] != INF and dist[next_node] > dist[node] + cost: 
                dist[next_node] = dist[node] + cost  
                if i == n-1:
                    return True
            
            return False
    

negative_cycle = bf(1)

if negative_cycle:
    print('-1')
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
    for i in range(2, n+1):
        if dist[i] == INF: 
            print('-1')
        else:
            print(dist[i])
