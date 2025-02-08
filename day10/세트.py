'''
변수명  = {요소1,요소2,요소3}
set(세트로 바꾸고 싶은 다른 자료구조)
'''

str = "apple"
list2 = [1,2,3]
tuple2 = (1,2,3)
print("각자의 형태를 가진 자료구조들")
print("str : ",str)
print("list : ",list2)
print("tuple : ",tuple2)

#set로 변환
set_str = set(str)
set_list = set(list2)
set_tuple = set(tuple2)

print()

#변환된 값 출력
print("set로 변환된 자료구조들")
print("set_str", set_str)
print("set_list", set_list)
print("set_tuple", set_tuple)

print()

str_banana = "banana"
set_banana = set(str_banana)
print(str_banana[0])
# print(set_banana[0]) # 에러!

#요소에 접근하기 위해 리스트,튜플로 변환하기
print(set_banana) #세트 출력해보면 n,a,b만 남은것을 볼 수 있음(중복제거)

print()

list_banana = list(set_banana) #세트바나나를 리스트로 변환
tuple_banana = tuple(set_banana) #세트바나나를 튜플로 변환

print(list_banana) #['a', 'n', 'b']
print(tuple_banana[1]) #n
print(tuple_banana) #('a', 'n', 'b')

#마구잡이 알파벳에서 중복을 삭제하고 오름차순정렬
#1. 중복 삭제

str_random = "sdpflneklfcmsljiahnklsdmclslx" #마구잡이 알파벳 생성
str_random = set(str_random) #중복제거
print(str_random)
sorted_list_change = sorted(set(str_random))#이렇게 하면 원본이 바뀌지 않는 상태로 오름차순 + 중복제거됨
print(sorted_list_change)
print(str_random)#원본이 바뀌는 것은 아님

#리스트로 변환
list_str = list(str_random)
print(list_str) # [] 대괄호로 변경 되었나 확인하기

#리스트를 오름차순으로 변경
list_str.sort()
print(list_str)

#특정 순서의 알파벳 출력
print(f"3번째로 작은 알파벳은 {list_str[2]} 입니다")
print(f"7번째로 작은 알파벳은 {list_str[6]} 입니다")