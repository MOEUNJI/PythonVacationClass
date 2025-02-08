me = {
   "name" : "MoEunJi", # key : value
   "age" : 20, # 숫자나 불리언 값은 따옴표 없이 사용 가능
   "phone" : "010-1234-5678",
   "class" : ["c언어", "python","java"] # 값을 리스트로도 가질 수 있다
}


my_phone = {
   "name" : "아이폰16",
   "price" : "1,400,000",
   "color" : "white",
   "storage" : "256GB"
}
print(me)

print(my_phone["color"]) #white
print(me["class"]) #['c언어', 'python', 'java']
print(me["class"][1]) #python

friends = {}
friends["도현"] = 19 # 키 : value 를 넣어준 것
friends["소민"] = 27
print(friends)
print(friends["소민"]) # 27

friends["도현"] = 25 # value 변경
print(friends["도현"]) # 25

#딕셔너리에서 소민 삭제
del friends["소민"]
print(friends)

#딕셔너리 초기화
friends.clear()
print(friends)

print()
print()

'''
1. keys() : 딕셔너리의 모든 key값들을 모아 튜플 형태로 반환
2. values() : 딕셔너리의 모든 값을 반환
3. items() : 딕셔너리의 모든 키(key)와 값(value) 쌍을 반환합니다.
4. update(other_dict) : 딕셔너리에 다른 딕셔너리의 키-값 쌍을 추가하거나 덮어씁니다.
'''

print("keys()")
my_dict = {
   "name" : "kelly",
   "age" : 25,
   "city" : "New York"
}
keys = my_dict.keys() #my_dict의 모든 키들을 뽑아서 리스트처럼 보이게 만들어줌
print(keys)
print()

list = list(my_dict.keys()) #my_dict의 모든 키들을 리스트화
print(list)  # 결과: ['name', 'age', 'city']
print()

print("values()") # 딕셔너리의 모든 값을 반환
values = my_dict.values()
print(values)  # 결과: dict_values(['kelly', 25, 'New York'])
print()

print("items()") # 딕셔너리의 모든 키(key)와 값(value) 쌍을 반환합니다.
items = my_dict.items()
print(items)
# 결과: dict_items([('name', 'Alice'), ('age''New York')])
print("이거")

print("update()")
#update(other_dict) 딕셔너리에 다른 딕셔너리의 키-값 쌍을 추가하거나 덮어씁니다.
my_dict.update({"age":26,"hobby":"freediving"})
print(my_dict)
# 결과: {'name': 'kelly', 'age': 26, 'city': 'New York', 'hobby': 'freediving'}
# 키가 있다면 값을 변경하고, 키가 없다면 추가함
print()

#오름차순 ( 키값 )
print(sorted(my_dict)) #키만출력됨 ['age', 'city', 'hobby', 'name']
print(sorted(my_dict.items())) #[('age', 26), ('city', 'New York'), ('hobby', 'freediving'), ('name', 'kelly')]

#내림차순
print(sorted(my_dict,reverse=True)) #['name', 'hobby', 'city', 'age']
