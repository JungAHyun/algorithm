from collections import deque

sadari_cnt, snake_cnt = map(int, input().split(' '))
table = []
sadari_list = []
sadari_q = deque()
snake_q = deque()

for i in range(100):
    table.append(i)

for i in range(sadari_cnt):
    sadari_list.append(list(map(int, input().split(' '))))
sadari_list.sort()

for i in range(sadari_cnt):
    sadari_q.append(sadari_list[i])

for i in range(sadari_cnt):
    x, y = map(int, input().split(' '))
    snake_q.append((x,y))

num = 1 
cnt = 0
x, y = sadari_q.popleft()
def dfs(num):
    global cnt, x, y
    use_x, use_y = x,y
    if table[num] == 100:
        return cnt

    for i in range(1,6):
        if table[num+i] == 100:
            return cnt
            
        #사다리가 있는 경우
        if len(sadari_q)!=0 and table[num+i] == use_x:
            if (num < use_y):
                num = use_y
                x, y = sadari_q.popleft()
                if(y>(num+6-i)):
                    continue

        #사다리가 없는 경우  
        else:
            if(len(snake_q)!=0 and use_y in snake_q):
                continue
            num = num + 1
    print(num)

    cnt +=1
    dfs(num)

dfs(num)

print(cnt)