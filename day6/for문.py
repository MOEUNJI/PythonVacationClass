'''
for 변수 in 리스트:
    코드1
    코드2
'''

for num in [1,2,3,4,5]:
    print(num)

list_number = [6,7,8,9,10]
for list_for in list_number:
    print(list_for)

'''
for(int i = 0; i < 3; i++) {
}
'''

black_pink = ["제니","로제","지수","리사"]
for bp_hello in black_pink:
    print(f"안녕하세요 블랙핑크 {bp_hello}입니다.")

for char in "apple":
    print(char)

#range() 함수
# sum = 1+2+3+4+5
#
# sum = 0
# sum += 1
# sum += 2
# sum += 3
# sum += 4
# sum += 5

sum_list = [1,2,3,4,5]
sum = 0
for sum_for in sum_list:
    sum += sum_for
print(sum)

'''
for 변수 in range(start,stop,step):
    실행할 코드
'''

for range_for in range(5):
    print(range_for)
# 시작값은 0이라는 것을 알 수 있으며 stop 값인 5는 포함되지 않는 것을 확인

print()

for range_for2 in range(2,6):
    print(range_for2)
    # 시작값은 포함, 끝나는 값은 불포함

print()

for range_for3 in range(1,10,2):
    print(range_for3)
# 1부터 10 이전까지 숫자를 2씩 증가시키며 반복시킨다.
# 1을 출력하고 2스텍을 건너뛰면 2,3 을 건너뛰고 4를 출력해야하는거 아니야?
# ㄴㄴ! 1 + 2 = 3 / 3 + 2 = 5 / 5 + 2 = 7 이렇게 생각하기

print()

for range_for4 in range(10, 0, -2):
   print(range_for4)

print()

total = 0
for range_for5 in range(1,6): # 1 ~ 5
    total += range_for5
print("합계 : ",total)

print()

fruits = ["apple","banana","cherry"] # 리스트 생성
for range_for6 in range(len(fruits)):
    print(f"인덱스 {range_for6}: {fruits[range_for6]}")