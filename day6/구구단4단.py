# for gugudan4 in range(1,10):
#     print(f"4 X {gugudan4} = {gugudan4 * 4}")
#
# for gugudan3 in range(1,10):
#     print(f"3 X {gugudan3} = {gugudan3 * 3}")

for gugudan in range(1,10):
    for gugudan_in in range(1,10):
        print(f"{gugudan} X {gugudan_in} = {gugudan * gugudan_in}")


# 숫자피라미드
n = 5
for i in range(1, n + 1):  # 1부터 n까지 반복
    for j in range(i):  # i만큼 숫자 출력
        print(i, end=" ")
    print()  # 줄 바꿈
