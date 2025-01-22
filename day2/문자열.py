name = "mo"
name2 = 'eun ji'
name3 = '''mo eun ji'''
name4 = """MO EUN JI"""

num = "100"
null_string = ""

str1 = "Park's Bakery"
str2 = 'eunji say "so funny"'
print(str2)

first_name = "mo"
last_name = " eun ji"
full_name = first_name + last_name
print(full_name)

class_name = 'Python '
print(class_name * 5)

a = "apple"
first_char = a[0]
third_char = a[2]
print(first_char)
print(third_char)

last_char = a[-1]
print(last_char)
second_char = a[-5]
print(second_char)

text = "I love Pasta"
slicing1 = text[2:6] # 인덱스 2번부터 l부터 6-1인 5까지(e) 출력하겠다.
print(slicing1)
slicing2 = text[7:12]
print(slicing2)

last_lost = text[6:]# 작성숫자부터 해당되니까 띄어쓰기를 포함한다.( Pasta)
print(last_lost)


coca = "---This is coca"
strip_cola2 = coca.strip("-") # 작성하지 않으면 ---This is coca 이렇게 출력ㄴ
print(strip_cola2)

#학번 입력받기
student_id = input("4자리 학번을 입력하세요 : ")


#문자열 인덱싱과 슬라이싱으로 학년, 반, 번호 추출
grade = student_id[0] # 학번의 첫 번째 문자
class_num = student_id[1:2] #인덱스번호 1부터 3-1(2)까지 # 학번의 두 번째와 세 번째 문자
student_num = student_id[2:4] #인덱스번호 3부터 5-1(4)까지 # 학번의 네 번째와 다섯 번째 문자


#결과 출력
print(f"{grade}학년 {class_num}반 {student_num}번 ")

