'''
open("파일명", "모드")
파일명
   작업할 파일의 이름(data.txt)
모드
   "r" : 읽기 모드(파일을 읽기만 할 때)
   "w" : 쓰기 모드(새로운 파일을 생성하거나 내용으 덮어쓸 때)
   "a" : 추가 모드(파일 끝에 데이터를 추가할 때)
'''
file = open("example.txt", "w", encoding="utf-8")  # 읽기 모드로 파일 열기
# file_read = file.read()
file.write("I love icecream")
file.close()  # 파일 닫기

# print(file_read)

'''
파일 읽기
1. 변수명.read() : 파일 전체 내용 읽기
2. 변수명.readline() : 파일 한 줄씩 읽기
3. 변수명.readlines() : 파일의 모든 줄을 읽어 리스트로 반환하기
'''


'''
파일 존재여부 검사
import os
print("파일 존재 여부:", os.path.exists("test.txt"))
'''
import os
print("파일 존재 여부:", os.path.exists("example.txt"))
# exists : 익짓트 / path 패스