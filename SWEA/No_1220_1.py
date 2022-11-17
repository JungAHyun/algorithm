table_len = int(input())

table = []
for _ in range(table_len):
    table.append(list(map(int, input().split())))

up = -1
down = +1
cnt = 0
for i in range(table_len):
    i_down = i
    for j in range(table_len):
        while(True):
            if table[k][j] == table[k + down][j] or table[k][j] == 0:
                break

            if table[k][j] == 1 and table[k + down][j] == 0:
                table[k][j] == 0
                table[k + down][j] == 1

            elif table[k][j] == 1 and table[k + 1][j] == 2:
                cnt += 1
                print(f"[{k}][{j}]")
                break

for i in range(table_len):
    print(table[i])
print(cnt)
