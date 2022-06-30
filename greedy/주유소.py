
city_cnt = int(input())
lenth = list(map(int, input().split(' '))) 
money = list(map(int, input().split(' '))) 

index = []
min_index=0
min_momey = money[0]

#제일 금액이 적은 도시의 인덱스 찾음
for i in range(1,len(money)):
    if min_momey > money[i]:
        min_index = i
        min_momey = money[i]
    elif min_momey == money[i]:
        continue

index.append(min_index)
print(index)
result = 0
j = min_index

if min_momey == money[0]:
    result = money[0]*(sum(lenth))
else:
    while(min_index>1):
        min_momey = money[0]
        for i in range(j):
            if min_momey > money[i]:
                min_index = i
                min_momey = money[i]
            elif min_momey == money[i]:
                continue
        j = min_index
        index.append(j)        


index = reversed

print(index)
