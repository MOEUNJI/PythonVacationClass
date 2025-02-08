# 사용자가 비가 오는지 입력
is_raining = input("비가 오나요? (예/아니오): ")

# 입력 값을 판단해서 출력
if is_raining == "예":
    print("우산을 챙기세요!")
else:
    print("우산은 필요 없어요.")


like_number = int(input("숫자를 입력해주세요 : "))

odd = "홀수"
even = "짝수"
result = even if like_number % 2 == 0 else odd
print(result)
'''
코드에서 like_number는 **input()**으로 받아오는데,
**input()**의 반환 값은 항상 문자열(str) 형태야.
하지만 **%(나머지 연산자)**는 숫자(int) 타입에서만 동작하기 때문에 오류발생
'''

gender = "women"
if gender == "women":
   print("여자입니다.")
else:
   print("남자입니다.")