num1 = 10 # 양의 정수
num2 = -3 # 음의정수
num3 = 0 #양의정수

print(num1)
print(num2)
print(num3)

first = 3.9
second = 3
print(first * second)


# 한 학교에서 학생 한명당 필요한 급식비는 8,000원이다.
# 선생님은 6,000원이다..
#
#
# 학생 23명과 선생님 2명이 급식을 먹는다
# 급식비를 계산하면?
# """


student_cost = 8000 #학생가격
teacher_cost = 6000 #선생가격
student = 23 #학생수
teacher = 2 #선생수


teacher_total_cost = teacher * teacher_cost #선생수 * 선생가격 = 선생토탈
student_total_cost = student * student_cost #학생수 * 학생가격 = 학생토탈


all_cost = teacher_total_cost + student_total_cost
# 선생토탈 + 학생토탈 = 전체토탈


print("총 급식비는 :", all_cost, " 원 입니다.")