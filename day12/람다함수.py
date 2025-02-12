#list, range를 사용해서 lambda함수로 구구단2단 출력
numbers = list(range(20))
#range는 연속된 숫자를 출력하는 함수로 여기서는 20까지 출력한다.
#list로 감싸주어서 20개가 들어있는 리스트 객체로 만든다
# 예를들면 range(20) → [0, 1, 2, 3, ..., 19]


even_numbers = list(filter(lambda x : x % 2 == 0,numbers))
print(even_numbers)
#filter(function, iterable 이터러블) : 는 조건에 맞는 요소만 걸러주는 함수
#function: 조건을 만족하면 True, 아니면 False를 반환.
#iterable: 검사할 데이터(리스트, 튜플 등).
# 람다함수는 filter에 전달될 검사받을 함수이다.
# x를 2로 나눈 나머지가 0과 같다면 결과가 True이면 짝수이다.
#최종적으로, filter는 [0, 2, 4, 6, ..., 18]라는 짝수 리스트를 반환.
#즉!!!!!!number list에서 앞에 조건을 검사한다고 생각하기
#다시 list로 감싸주는 이유는 filter는 리스트가 아니라 필터객체를 반환하기 때문에
#그래서 list()로 필터 객체를 리스트로 변환합니다.
'''
람다함수의 매개변수인 x에 매개변수에 아무것도 전달이 안 되었는데 어떻게 출력하는거지?
filter 함수가 iterable(number)에서 값을 하나씩 꺼내고,
그 값을 function(람다 함수)에 자동으로 전달
'''


#람다함수 정렬
tuple_num = [(1,10),(4,2),(99,6),(5,1),(8,12),(-3,20)]
#tuple_num : 튜플로 이루어진 리스트를 생성함 (각 튜플은 두개의 숫자로 이루어짐)


sorted_tuple = sorted(tuple_num)
#sorted(iterable)는 리스트, 튜플 등 정렬 가능한 데이터를 오름차순 정렬해서 반환합니다.
#sorted함수는 두번째 매개변수가 없으면 튜플의 경우는 첫번재 요소로 정렬
#(1, 10) → 첫 번째 요소는 1 / (4, 2) → 첫 번째 요소는 4 ...


print(sorted_tuple)
#[(-3, 20), (1, 10), (4, 2), (5, 1), (8, 12), (99, 6)]
# -3,1,4,5,8,99 앞자리 오름차순으로 정렬된것임


sorted_tuple = sorted(tuple_num,key=lambda index:index[1])
# sorted는 원래 첫째자리의 오름차순으로 정렬하는데, 튜플의 두 번째 요소로 설정하기 위해 작성한것.
# 리스트의 각 요소는 sorted()와 key 매개변수로 자동으로 전달됩니다
# sorted(리스트 튜플 등 작성, key=None) 함수는 어떤 기준으로 정렬할지를 결정해야 하는데 기본적으로는 "첫 번째 요소"를 기준으로 정렬.
# sorted 함수의 기능인 key 매개변수를 사용하면 어떤 기준으로 정렬할지 직접 설정할 수 있습니다.
#sorted()가 리스트에서 첫 번째 튜플 (1, 10)을 꺼냅니다. 람다함수의 매개변수인 index에 (1, 10)이 전달됩니다
#람다함수의 매개변수(1,10)을 받아서 index[1] 10을 기준으로 삼겠다는 뜻!


print(sorted_tuple)
