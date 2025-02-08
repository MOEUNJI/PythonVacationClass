'''
요소 추가하기
add() : 한 번에 하나의 요소를 추가.
update() : 여러개의 요소를 한 번에 추가 ( 리스트,튜플같은 세트가 아닌 자료형도 인자로 받아들임)

요소 삭제하기
remove() : 특정 요소를 제거(요소가 없으면 오류 발생).
discard(디스카드) : 특정 요소를 제거(요소가 없어도 오류 발생하지 않음).
pop() : 임의의 요소를 제거하고 반환(순서 없음).
clear() : 세트의 모든 요소를 제거
'''

set = {1,2,3}
set.add(4)
print(set) #{1, 2, 3, 4}

# update()메서드를 통한 요소 추가
set.update({5,6})
print(set) #{1, 2, 3, 4, 5, 6}

print()

set_c = {'a','s','d','f','g','h','j','k','l'}

# remove()메서드를 통한 요소 삭제
set_c.remove('a')
print(set_c) # 뒤죽박죽 출력될것{'f', 's', 'h', 'k', 'j', 'l', 'd', 'g'}
# set_c.remove("강아지") #세트에 없는 요소를 삭제하려고 하면 오류남
# print(set_c)

print()

# discard()메서드를 통한 요소 삭제
set_c.discard("고양이") # 없는 요소를 작성해도 오류나지 않음
print(set_c) # 뒤죽박죽 출력될것{'f', 's', 'h', 'k', 'j', 'l', 'd', 'g'}

print()

# pop()메서드를 통한 요소 삭제
set_red = {'r','e','d'}
# set_red.pop() # 랜덤으로 하나 제거
print(set_red) # 뒤죽박죽 출력될것{{'r', 'e'}
#만약 제거하고 남은 값이 아니라 제거된 값을 받고 싶다면?
#이거 할때 무조건 set_red.pop() # 랜덤으로 하나 제거 이 라인 주석하고 작성하기
print(set_red.pop())
print(set_red)

# clear()메서드를 통한 요소 삭제
set_blue = {'b','l','u','e'}
set_blue.clear() # 세트의 모든 요소를 제거
print(set_blue) # set() 빈 집합 출력