count = 0
while count < 3:
    print(count)
    count += 1


while count == 5:
    # count < 5
    break

num = 0
while num < 20:
    num += 1
    if num == 5:
        continue
    print(num,end=" ")

print()
print()
'''
조건
시작 숫자는  0
숫자는 30까지 증가할것인데
5의 배수는 출력하지 않으며, 짝수도 출력하지 않는다.
27전까지만 출력한다.
브레이크와 컨티뉴를 둘 다 사용해서 작성해보기
'''
number = 0
while number < 30:
    number += 1
    if number % 5 == 0:
        continue
    if number % 2 == 0:
        continue
    elif number > 27:
        break
    print(number)
