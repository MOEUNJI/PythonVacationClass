'''
조건
초기값은 0
반복문을 사용해서 0을 10까지 증가시키는데
0이 증가하다가 3의 배수가 되었다면 "짝"을 출력하고
컨티뉴로 반복문의 조건을 다시 검사함. 즉 3의 배수라면 짝이 출력되는 것!
3의 배수가 아닐 경우는 그냥 숫자 출력

'''

num = 0
while num < 10:
    num += 1
    if num % 3 == 0:
        print("짝")
        continue
    print(num)

