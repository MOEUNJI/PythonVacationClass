numbers = [3,7,8,6,10,4,2,5,0,1]
new_list = []
for num in numbers:
    if num > 5:
        new_list.append(num)
new_list.sort()
print(new_list)





numbers2 = [62,44,5,95,13,48,33,2,74]
even_numbers = []  # 짝수를 저장할 리스트

for num2 in numbers2:
    if num2 % 2 == 0:  # 짝수라면
        even_numbers.append(num2)  # 리스트에 추가
even_numbers.sort()
print(even_numbers)




numbers = [62, 44, 5, 95, 13, 48, 33, 2, 74]

even_numbers = []  # 짝수 리스트
odd_numbers = []   # 홀수 리스트

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

even_numbers.sort()  # 짝수 리스트 정렬
odd_numbers.sort()   # 홀수 리스트 정렬

print(f"짝수 리스트: {even_numbers}")
print(f"홀수 리스트: {odd_numbers}")



words = ["사과", "바나나", "포도", "딸기", "망고", "바람", "바이올린"]
selected_words = []

for word in words:
    if "바" in word:  # "바"라는 글자가 포함된 단어 찾기
        selected_words.append(word)

print(f"선택된 단어들: {selected_words}")

#중복제거
set_number = [5, 2, 9, 1, 5, 7, 2, 9, 10]
set_list = sorted(set(set_number))  # 중복 제거 후 정렬
print(set_list)

names = ["김철수", "이영희", "김민수", "박지훈", "김지영", "최수진"]
kim_family = []

for name in names:
    if name.startswith("김"):  # "김"으로 시작하는지 확인
        kim_family.append(name)

print(f"김씨 성을 가진 사람들: {kim_family}")

