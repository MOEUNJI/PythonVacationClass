'''
특정 조건을 만족하는 숫자만 골라서 반환하는 기능 만들기
filter() 함수 사용해야함
filter(조건을 검사할 함수, 반복 가능한 데이터) : 반복 가능한 요소 중에서 함수가 True를 반환하는 값만
골라서 필터링하는 함수
1. 첫 번째 인수: 조건을 검사할 콜백 함수
2. 두 번째 인수: 반복 가능한(iterable) 데이터 (리스트, 튜플, 세트 등)
3. True를 반환하는 값들만 남겨서 새로운 필터링된 객체 반환
'''
nums = [1,2,3,4,5,6,7,8,9]
def is_even(num):
    return num % 2 == 0 # 짝수면 True, 홀수면 False

even_numbers = list(filter(is_even,nums))
#is_even() 함수는 짝수일 때 True를 반환
#filter(is_even, numbers)는 짝수만 남긴 새로운 리스트를 반환
print(even_numbers)


def filter_numbers(number,callback):
    return list(filter(callback,number))
    # filter(callback, numbers) → numbers 리스트에서 callback 함수의 조건을 만족하는 값들만 골라 줌

def is_odd(num):
    return num % 2 != 0

def bigger_than_10(num):
    return num > 10

number = [1,4,9,8,76,30,56,81,22,54,37]
print(filter_numbers(number,is_odd))
print(filter_numbers(number,bigger_than_10))