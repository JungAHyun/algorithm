# 1225

T = 10
for tc in range(1, T + 1):
    num = int(input())
    num_list = list(map(int, input().split()))

    result = num_list[0]
    while (result != 0):
        disc = 1
        for _ in range(5):
            if num_list[0] - disc > 0:
                num_list[0] = num_list[0] - disc
            else:
                num_list[0] = 0

            num_list = num_list[1:] + num_list[:1]  # num_list.pop(0) 하면 0번째 인덱스 삭제
            disc = disc + 1
            result = num_list[-1]
            if result == 0:
                break

    print(f"#{tc} ")
    for i in range(len(num_list)):
        print(num_list[i], end=" ")
    print()
