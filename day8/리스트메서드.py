'''
리스트 추가
append() : 리스트의 마지막에 새로운 요소를 추가한다.
insert() : 리스트의 중간에 새로운 요소를 삽입가능


리스트 삭제
remove() : 특정 값을 가진 요소를 삭제
pop() : 특정 위치에 있는 요소 삭제


리스트 정렬
sort(): 리스트를 오름차순으로 정렬(원본 리스트가 변경됨)
sort(reverse = True) : 리스트를 내림차순으로 정렬
sorted() : 정렬된 새로운 리스트를 반환(원본 리스트가 변경되지 않음)


리스트 반전
reverse() : 원본 리스트를 역순으로 변경


리스트 문자열
join() : 리스트 요소에 연결문자를 추가해 하나의 문자열로 결합
'''

# append() : 리스트의 마지막에 새로운 요소를 추가한다.
append_nums = [1,2,3]
print(f"append() 추가 전 : {append_nums}")
append_nums.append(4)
print(f"append() 추가 후 : {append_nums}")

print()

# insert() : 리스트의 중간에 새로운 요소를 삽입가능
alphabets = ["a","b","c"]
print(f"insert()추가 전 : {alphabets}") #['a', 'b', 'c']
alphabets.insert(1,"M") # 인덱스 1번에 M추가
print(f"insert()추가 후 : {alphabets}") #['a', 'M', 'b', 'c']

#remove() : 괄호 안에 일치하는 값을 찾아 삭제
remove_nums = [1,2,3,4]
print(f"remove()삭제 전 : {remove_nums}") #[1, 2, 3, 4]
remove_nums.remove(1) # 없는 값 넣으면 에러남
print(f"remove()삭제 후 : {remove_nums}") #[1, 3, 4]


# pop() : 특정 위치에 있는 요소 삭제
colors = ["red","black","yellow","black"]
print(f"pop()삭제 전 : {colors}") # ['red', 'black', 'yellow', 'black']
colors.pop(3) #인덱스번호에 해당하는거 삭제
print(f"pop()삭제 후 : {colors}") #['red', 'black', 'yellow']

#reverse() - 역순
reverse_num = [2,4,6,8,10]
print(f"reverse()적용 전 : {reverse_num}") # [2, 4, 6, 8, 10]
reverse_num.reverse() #역순
print(f"reverse()적용 후 : {reverse_num}") # [10, 8, 6, 4, 2]

#join() - 연결
join_text = ["a","b","c"]
print(f"join(-)적용 전 : {join_text}") # ['a', 'b', 'c']
join_result = "-".join(join_text) #a, b, c를 -로 연결해 하나의 문자열 출력
print(f"join(-)적용 후 : {join_result}") # a-b-c (리스트가 문자열로 변환됨!)
