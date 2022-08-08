

n =  int(input())
scores = []

for _ in range(n):
    scores.append(int(input()))


sum = scores[0]
cnt = 0
i = 0
while i < n:
    
    if cnt == 2:
        i+=1
        cnt =0
        continue

    if scores[i]> scores[i+1]:
        sum = scores[i]+ sum
        i += 2
        cnt += 1
    else:
        sum = scores[i+1]+ sum
        i +=1
        cnt = 0
        
        


print(sum)