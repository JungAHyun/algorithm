

n =  int(input())
scores = []

for _ in range(n):
    scores.append(int(input()))

cnt = 0
s = scores[0]

i = 1
while i < n:
    if len(scores)  < 3:
        s = sum(scores)
        break

    # if i == n-3 and scores[i] < scores[i+1] and scores[i+1] < scores[i+2]:
    #     s = s + scores[i+2] + scores[i]
    #     break

    if cnt == 2 :
        i+=1
        cnt =0
        continue
    

        
    if scores[i] > scores[i+1]:
        s = scores[i]+ s
        i += 2
        cnt += 1
    else:
        s = scores[i+1]+ s
        i +=1
        cnt = 0
        
        


print(s)