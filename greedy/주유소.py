
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

lenth_sum = 0
before_index = 0
result_money=0
index = reversed(index)
print(index)
for i in index:
    for j in range(before_index, index[i]):
        lenth_sum += lenth[j]
    before_index = index[i]
    result_money += lenth_sum*money[i] 


print(result_money)




'''
9
1 1 1 1 1 1 1 1
4 3 2 7 1 7 6 2 8

[4]
[4, 2, 1]

'''