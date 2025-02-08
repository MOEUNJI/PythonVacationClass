num = int((input("숫자를 입력하세요 : ")))

# for hello in range(num):
#     # num은 정수인데 for문은 반복 가능한 값에서만 사용 가능하기 때문에
#     # 정수가 들어갈 수 없다. 즉 아무리 int형으로 받아와도 안됨
#     if num <= 0:
#         print("잘못된 입력입니다. 1 이상의 수를 입력하세요")
#     print(f"{hello}번째 안녕하세요")

if num <= 0:
    print("잘못된 입력입니다. 1 이상의 수를 입력하세요")
else :
    for hello in range(num):
        print(f"{hello + 1}번째 안녕하세요")