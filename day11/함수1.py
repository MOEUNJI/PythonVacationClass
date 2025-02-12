'''
함수의 장점
1. 반복적인 코드 제거 및 재사용성 향상
2. 코드의 가독성 및 유지보수 향상
3. 오류추적 및 디버깅 용이

def 함수이름():
   코드1
   코드2
   코드3

'''

def hello():
    print("안녕하세요")
    print("저는 안나입니다.")
    print("엘사 동생이에요")

hello()

colors = ["red", "orange", "yellow", "green", "skyblue"] #색상리스트 생성
index = 0 # 초기 index변수 설정(처음에는 0이므로 처음 색상인 red를 뜻할것)
def change_color():
    global index
    if index >= len(colors): #index가 colors의 리스트의 길이보다 같거나 크다면
        index = 0 #인덱스를 0으로 변경해라.
        # 즉 만약 index가 5보다 크거나 같아지면, 리스트의 끝을 넘어가므로 다시 처음 색상(index = 0)으로 돌아갑니다.
    print(f"배경색을 {colors[index]}로 변경합니다.")
    # 현재 index에 해당하는 색상을 선택하여 출력합니다. index = 0일 때는 red가 출력됩니다.
    index += 1
    # 색상을 출력한 후에는 index를 1 증가시켜 다음 색상을 가리키도록 합니다.
    # 예를 들어, index = 0에서 1을 더하면 index = 1이 되고,
    # 다음번 호출에서 colors[1]인 "orange"가 선택됩니다.

change_color()
change_color()
change_color()
change_color()
change_color()
change_color()
#호출할때마다 "red", "orange", "yellow", "green", "skyblue" 색이 바뀌고
#스카이 블루가 지나면 다시 red가 출력될 것

'''
매개변수
def 함수이름(매개변수1,매개변수2...):
   코드1
   코드2

'''

#솜사탕 함수 선언
def candy_fluff(count): #캔디플러프
    print("오늘은 솜사탕을 "+ str(count) +"개 만들어야 합니다.")
#솜사탕함수 호출
candy_fluff(15)

print()

#함수선언
def hello(name):
   print(f"안녕하세요 제 이름은 {name}입니다.")

# 호출
hello("제니")  # 안녕하세요 제 이름은 제니  입니다.
hello("지수")  # 안녕하세요 제 이름은 지수  입니다.


print()

#함수선언
def plus(a,b):
   print(a+b)

plus(10,20) #30
plus(5,20) #25
plus(3,50) #53

print()

def student(name, age, hobby):
   print(f"안녕하세요 저는 {name}입니다. 나이는 {age}살 입니다.")
   print(f"취미는 {hobby}입니다.")

student("모은지",20, "프리다이빙")
student("홍길동",19, "러닝")
student("김도현",25, "쇼핑")

