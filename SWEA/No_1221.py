# 1221

T = int(input())

for tc in range(1, T + 1):
    num, length = input().split()
    length = int(length)

    word = list(input().split())
    dic = {0: "ZRO", 1: "ONE", 2: "TWO", 3: "THR", 4: "FOR", 5: "FIV", 6: "SIX", 7: "SVN", 8: "EGT", 9: "NIN"}

    order = [[] for _ in range(10)]
    for i in range(len(word)):
        index = 0
        for j in range(10):
            if word[i] == dic[j]:
                index = j
                break
        order[index].append(word[i])

    print(f"#{tc}")
    for i in range(len(order)):
        for j in range(len(order[i])):
            print(order[i][j], end=' ')
