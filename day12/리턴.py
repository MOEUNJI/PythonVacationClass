'''
def 함수이름(매개변수1,매개변수2...):
   코드1
   코드2
   코드3
   return 함수 밖으로 전달하고 싶은 값
'''

def plus(a,b):
   return(a+b)

sum = plus(10,20)
print(sum)

print()

#한 번 더 해볼까요?
def multiply(num):
   result = num * 7 #호출할 때 넣는 숫자랑 7을 곱해서
   return result # 곱한 값을 반환한다.

print(multiply(3))

print()

#7의 배수
def check_divide_seven(num2):
   if num2 % 7 == 0:
       return  True
   else:
       return False


print(check_divide_seven(44))
