'''
튜플 -> 변수명 : (요소1, 요소2, 요소3, ... )
리스트 -> 변수명 : [요소1,요소2,요소3, ...]
'''

alphabets = ('a','b','c') # 문자
colors = ("red", "green", "blue") # 문자열
bools_tuple = (True,False,True) # 논리값
mix_tuple = ("red", 'g', 3, True) # 혼합

names = ("mo","eun","ji")
first_name = names[0]
second_name = names[1]
third_name = names[2]
print(first_name)
print(second_name)
print(third_name)

#리스트, 튜플 생성 및 전체 출력
list = [1,2,3]
tuple = (1,2,3)
print(list)
print(tuple)

# 각 첫번째 요소 수정 시도
list[0] = 30
# tuple[0] = 30 #오류남!!

#요소 추가
list.append(4)
# tuple.append(4) #오류남!!
print(f"list 요소 추가 완 : {list}")
print(f"tuple 요소 추가 완 : {tuple}")

#중첩
multi_tuple = (1,(2,3),[4,5]) #튜플 안에 2,3 튜플 있고, 4,5 리스트 있음
print(multi_tuple[2]) #[4, 5]
print(multi_tuple[1][1]) #3
print(multi_tuple[0]) #1

#튜플에 리스트를 담았다면 리스트는 수정이 가능한 자료구조인데 정말 수정 가능할까?
multi_tuple[2][0] = 3 #튜플 안에 있는 리스트는 수정 가능!
print(multi_tuple[2])

#튜플 슬라이싱
slice_tuple = (3,10,"파이썬",True,"고양이",23)
print(slice_tuple[1:4]) #(10, '파이썬', True) 마지막 인덱스 빼고 출력
print(slice_tuple[0:5]) #(3, 10, '파이썬', True, '고양이')
print(slice_tuple[0:8]) # 슬라이싱은 범위를 벗어나도 잘 출력됨
print(slice_tuple[8:50]) #만약 완전히 벗어나도 () 출력됨!

# 하지만 범위를 벗어난 요소를 출력하려한다면 오류남
print(slice_tuple[8])

#count() : 튜플에서 특정 값이 몇 번 등장했는지 세어줘.
my_tuple = (1, 2, 3, 2, 2, 4)
count_of_2 = my_tuple.count(2)
print(count_of_2)  # 출력: 3 (2가 3번 등장)


#index() : 튜플에서 특정 값이 **처음 등장하는 위치(인덱스)**를 찾아줘.
my_tuple2 = (10, 20, 30, 20, 40)
index_of_20 = my_tuple2.index(20)
print(index_of_20)  # 출력: 1 (20이 처음 나타난 위치)

#튜플의 데이터 교환
a = 10 #변수
b = 20 #변수
print(f"교환 전 : a:{a}, b:{b}")
a,b = b,a #변수 값을 기반으로 튜플을 만들었음 소괄호가 없어도 콤마가 있다면 튜플로 간주
print(f"교환 후 : a:{a}, b:{b}")
#이렇게 값을 변경하지는 못하지만 가지고 있는 값을 가지고 교환이 가능하다.
