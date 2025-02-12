def hello(name):
   #hello이라는 함수를 만들기
   # 매개변수인 name은 함수가 실행될 때 외부에서 전달되는 이름.
   print(f"안녕,{name}!")

def call_function_with_name(callback,name):
   #call_function_with_name 함수는 두 가지를 받아요
   #callback: 실행할 "다른 함수"를 받음.
   #name: 이름 데이터를 받음.
   callback(name)#전달받은 함수(callback)을 실행.
   #이 함수 안에서 callback(name)을 호출해서 콜백 함수로 전달된 hello이 실행돼요.
   #callback(name)의 의미는 callback이라는 함수에 name이라는 값을 전달해서 실행하라는 뜻.
   #예를 들어, callback에 hello이라는 함수가 전달되었다면, 이 줄은 hello(name)과 같아짐.
call_function_with_name(hello,"은지")

'''
실행 과정 설명
호출 : call_function_with_name(hello,"은지") 실행
--> call_function_with_name 함수에 hello이라는 함수와 "은지" 라는 데이터 넣음


함수선언부 : call_function_with_name(callback,name)에서는
callback은 hello 함수가 되고, name은 "은지"가 됨.


call_function_with_name 내부 실행
함수 내부에서 callback(name)을 실행하는데,
callback은 매개변수로 받은 hello이므로, hello(name)과 같다.
따라서 이 줄은 hello("은지")로 바뀜.


hello("은지") 실행
hello 함수가 실행되면서, name에 "은지"가 전달됨.
hello 함수 코드인 print(f"안녕,{name}!")이 실행되고, 안녕, 은지!라는 문장이 화면에 출력돼요.
'''


#함수선언
def calculator(x,y, operation):#calculator는 계산기를 작동시키는 틀이에요.
   #x: 첫 번째 숫자 (예: 2)
   #y: 두 번째 숫자 (예: 3)
   #operation: 계산 방법 (덧셈, 뺄셈, 곱셈, 나눗셈 중 하나)
   return operation(x,y)
   #여기서 operation은 나중에 덧셈, 뺄셈, 곱셈, 나눗셈 중 하나의 함수가 들어와요.
'''
operation(x, y)는 이렇게 동작해요:

만약 operation이 plus라면 → plus(x, y)를 실행.
만약 operation이 minus라면 → minus(x, y)를 실행.
'''

def plus(x,y): # 더하기 operation 함수 생성
   return x+y


def minus(x,y): # 마이너스 operation 함수 생성
   return x-y


def multiple(x,y): # 곱하기 operation 함수 생성
   return x*y


def divide(x,y): # 나누기 operation 함수 생성 #디바이브드
   return x/y if y != 0 else "Error : 0으로 나눌 수 없습니다."

#함수호출
plus_result = calculator(2,3,plus) # calculator호출 매개변수 2,3 연산자는 plus함수
minus_result = calculator(2,3,minus) # calculator호출 매개변수 2,3 연산자는 minus함수
multiple_result = calculator(2,3,multiple) # calculator호출 매개변수 2,3 연산자는 multiple함수
divide_result = calculator(6,2,divide) # calculator호출 매개변수 2,3 연산자는 divide함수
# 파이썬에서 / 연산자는 항상 실수(float) 값을 반환합니다.
# 정수 나눗셈을 하려면 // 사용해야함
#출력
print(plus_result)
print(minus_result)
print(multiple_result)
print(divide_result)

