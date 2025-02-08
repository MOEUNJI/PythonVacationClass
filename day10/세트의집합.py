'''
set의 교집합
1. &연산자 사용 : 두 세트를 &연산자로 연결하여 새로운 세트를 만들며 이 때 중복되는 요소는 제거
2. intersection(인터섹션)메서드 사용 : 두 세트를 인자로 전달하여 교집합을 반환한다
'''

set_a = {1,2,3,4}
set_b = {3,4,5,6}
print(set_a) # {1, 2, 3, 4}
print(set_b) # {3, 4, 5, 6}

#intersection() 메서드를 사용하여 두 세트의 교집합을 찾기
insersection_a_b = set_a.intersection(set_b)
print(insersection_a_b) # {3, 4} 교집합만 뽑아옴

# &연산자를 사용하여 두 세트의 교집합 찾기
and_a_b = set_a & set_b
print(and_a_b) # {3, 4}

#문자열도 가능할까요?
'''
과일바구니에 딸기 오렌지 체리가 있어요!
그런데 내가 좋아하는 과일은 포도, 오렌지, 딸기 입니다.
공통되게 겹치는 과일을 두가지 방법으로 출력해보도록 할게요!
'''

set_fruits = {"strawberry","orange","cherry"}
set_favorites = {"grape","orange","strawberry"}

#& 연산자로 교집합 구하기
and_fruits = set_fruits & set_favorites #{'strawberry', 'orange'}
intersection_fruits = set_fruits.intersection(set_favorites) #{'strawberry', 'orange'}

print(and_fruits)
print(intersection_fruits)


'''
set의 합집합
1. | 연산자 사용 (파이프연산자)
2. union() 메서드 사용
'''

set_a = {1, 2, 3}
set_b = {3, 4, 5}

# |연산자를 사용하여 합집합 구하기
pipe_set = set_a | set_b
print(pipe_set)  # 출력: {1, 2, 3, 4, 5} ( 중복 제거 후 합을 반환 )


# union() 메서드를 사용하여 합집합 구하기
union_set = set_a.union(set_b)
print(union_set)  # 출력: {1, 2, 3, 4, 5}

# 학원생 전원의 명단을 뽑아보자
'''
학원에서 수학 수업을 듣는 학생은 엘사, 모아나, 라푼젤이다.
학원에서 영어 수업을 듣는 학생은 엘사, 안나, 모아나이다.
학원의 모든 학생을 |,union을 사용해서 출력해보자
'''
students_math = {"엘사", "모아나", "라푼젤"}
students_english = {"엘사", "안나", "모아나"}

# |연산자를 사용하여 합집합 구하기
all_students = students_math | students_english  # 방법 1: | 연산자
print("모든 학생:", all_students)  # 출력: {'엘사', '라푼젤', '모아나', '안나'}

# union() 메서드를 사용하여 합집합 구하기
all_students_method = students_math.union(students_english)  # 방법 2: union 메서드
print("모든 학생:", all_students_method)  # 출력: {'엘사', '라푼젤', '모아나', '안나'}


'''
set의 차집합
1. - 연산자 사용 (마이너스 연산자)
2. difference() 메서드 사용
'''

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# -(subtraction 서브트랙션)연산자를 사용하여 차집합 구하기
subtraction_set = set_a - set_b
print(subtraction_set)  # 출력: {1, 2}

# difference() 메서드를 사용하여 차집합 구하기
diff_set = set_a.difference(set_b)
print(diff_set)  # 출력: {1, 2}

#음악과 역사반이 있는데 음악 공부하지만 역사는 공부하지 않는 학생을 찾아보자
music_students = {"알라딘", "오로라", "자스민"}
history_students = {"오로라", "자스민"}

# 음악만 공부하는 학생 ( - )
only_music = music_students - history_students
print("음악만 공부하는 학생:", only_music)  # 출력: {'알라딘'}

# 음악만 공부하는 학생 ( difference() )
only_music_method = music_students.difference(history_students)
print("음악만 공부하는 학생:", only_music) # 출력: {'알라딘'}