mixed_list = [1, "apple", 3.14, True] #숫자, 문자, 논리값 혼합리스트
print(mixed_list)
'''
1 = 정수형(int)
2 = "apple": 문자열(str)
3 = 3.14: 실수형(float)
4 = True: 불리언(bool)
'''
print(mixed_list[1])#추가!!!!!!!!!!

mixed_list[1] = "mango"
print(mixed_list)

#중첩 list만들기
python_class = [
    ["철수", "영희", "민수"],  # 1조
    ["지수", "현우", "나영"],  # 2조
    ["동현", "수진", "호영"]   # 3조
]

#1조를 출력하고싶다면?
print(python_class[0])

#2조를 출력하고싶다면?
print(python_class[1])

#3조를 출력하고싶다면?
print(python_class[2])

#3조에 있는 수진이를 출력하고 싶다면?
print(python_class[2][1])

#그럼 민수를 출력해볼까요?
print(python_class[0][2])

#지수가 이름을 로제로 개명했다!
python_class[1][0] = "로제"
print(python_class[1]) # 2조 출력


family = ["mother","father","sister","dog"]
print(family[-1]) # 뒤에서부터 출력 ( dog 출력 )
print(family[-4])


'''
list[start:end:step]


start: 슬라이싱이 시작되는 인덱스 (포함)
end: 슬라이싱이 끝나는 인덱스 (포함되지 않음)
step: 요소를 건너뛰는 간격 (기본값은 1)
'''

numbers = [10,20,30,40,50]
print(numbers[0:3])
# 0,1,2,3 번 출력하라고 한 건데 마지막 인덱스는 출력되지 않는 것!


print(numbers[1:4])  # [20, 30, 40]
# 1,2,3 출력 4번은 출력 안 된 것!


# 뒤에서 두 번째 요소부터 마지막 요소까지
print(numbers[-2:])  # [40, 50]
# 시작 인덱스는 -2인거고 끝나는 지점을 비우면 마지막까지 출력됨

# 위에서-2를 작성해도 시작이 40인 이유는 start이기 때문

# 첫 번째부터 뒤에서 두 번째 요소까지 표현할건데
# stop자리에다 쓴 인덱스는 포함하지 않으므로 40은 들어가지 않음
print(numbers[:-2])  # [10, 20, 30]

# 한 요소씩 건너뛰기
print(numbers[::2])  # [10, 30, 50]

# 역순으로 추출
print(numbers[::-1])  # [50, 40, 30, 20, 10]

# 첫 두 요소를 100, 200으로 변경
numbers[:2] = [100, 200] #[:2] 는 2를 포함하지 않으니까 0,1번을 뜻함
print(numbers)  # [100, 200, 30, 40, 50]

# 첫 두 요소 삭제
numbers[:2] = []
print(numbers)  # [30, 40, 50]

colors = ["red",[1,2],"orange","green","yello"]
for color_for in colors:
    print(color_for, end=" ")

python_class = [
   ["철수", "영희", "민수"],  # 1조
   ["지수", "현우", "나영"],  # 2조
   ["동현", "수진", "호영"]   # 3조
]
for python_class_for in python_class:
    for student in python_class_for:
        print(student)

