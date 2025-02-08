num1 = 100
num2 = 50
bigger = num1 if num1>num2 else num2
#가운데 조건식이 true라면 if왼쪽에 있는 num1을 big에 대입한다.
print(bigger)


x = 21
y = 20
if x < y: #x가 y보다 작니? False!
   result = x #조건이 True라면 출력
   '''
   max는 python의 내장함수인 예약어이기 때문에 이 변수이름을 사용하면
   max함수를 사용하지 못함 ! 바꿔주어야함
   '''
else:
   result = y #조건이 False라면 출력
print(result) # y의 값 20 출력될것