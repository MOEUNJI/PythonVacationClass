'''
class 클래스명 :
    클래스 변수
    생성자
    메서드

클래스 정의
1. 클래스 이름은 보통 대문자로 시작한다.
2. 클래스 내부에 메서드(함수)나 속성을 추가하여 동작을 정의한다.

속성정의하기(__init__ 메서드)
__init__메서드는 객체가 생성될 때 자동으로 호출되는 생성자이다.
생성자에서 객체의 초기상태(속성)을 설정한다.
self는 현재 생성ㅇ되는 객체 자신을 가리키는 변수로,
클래스 내부 메서드에서 항상 첫 매개변수로 전달된다.

행동 정의하기(메서드 추가)
메서드는 클래스가 제공하는 행동을 정의한다.
메서드도 항상 self를 첫 매개변수로 사용한다.
'''

class User:
    def __init__(self, name, age, nationality):  # self는 이 객체 자신을 의미함
        self.name = name  # 이 객체의 name을 전달받은 name으로 설정
        self.age = age    # 이 객체의 age를 전달받은 age로 설정
        self.nationality = nationality  # 이 객체의 nationality 설정


    def introduce(self): # 객체가 자기소개할 수 있는 함수
        print(f"이름 : {self.name}, 나이 : {self.age}, 국적 : {self.nationality}")

# 여기서부터 실제 객체를 만들어봄
user1 = User("모은지",20,"Korea") # User 클래스의 객체(실제 사람)를 생성
print(user1.name) # user1의 name 출력 → "모은지"
user1.introduce()  # introduce 함수 실행 → "이름 : 모은지, 나이 : 20, 국적 : Korea"