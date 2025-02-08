'''
while 조건식:
    #조건식이 참이면 실행되는 코드

while 조건식:
    코드1
    코드2
    코드3
'''

count = 0
while count < 3:
    print(count)
    count = count + 1

count2 = 10
while count2 > 5:
    # print(count2)
    count2 -= 1
    print(count2)

'''
우리가 가진 돈 : 5000
아이스크림 : 1000
아이스크림을 2번 사먹을거임
아이스크림을 1번 사먹었다! 남은 돈은 ??원
아이스크림을 2번 사먹었다! 남은 돈은 ??원
'''
money = 5000  # 우리가 가진 돈
icecream_price = 1000  # 아이스크림 가격
icecream_count = 1  # 아이스크림을 몇 번 사먹었는지 저장하는 변수

while icecream_count <= 2:  # 아이스크림을 2번 사먹을 때까지 반복
    money -= icecream_price  # 아이스크림 가격만큼 돈을 차감
    # 첫번째 반복에 돈은 4000원이 됨
    print(f"아이스크림을 {icecream_count}번 사먹었다! 남은 돈은{money} 원! ")  # 텍스트 출력

    icecream_count += 1  # 횟수를 증가시킴




