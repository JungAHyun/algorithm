table_len = int(input())

table = []
for _ in range(table_len):
    table.append(list(map(int, input().split())))

up = -1
down = +1
cnt = 0
for i in range(table_len):

    for j in range(table_len):
        for k in range(table_len - i,0):
            if i == table_len-1:
                break
            if table[i][j] == 1 and table[i + down][j] == 0:
                table[i + down][j] == 1
                table[i][j] == 0
            elif table[i][j] == 1 and table[i + down][j] == 2:
                cnt += 1
                break

        for k in range(table_len - i):
            if i == 0:
                break
            if table[i][j] == 2 and table[i + up][j] == 0:
                table[i + up][j] == 2
                table[i][j] == 0
            elif table[i][j] == 2 and table[i + up][j] == 1:
                cnt += 1
                break
print(cnt)
