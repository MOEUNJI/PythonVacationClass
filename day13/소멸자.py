'''
동작원리
소멸자는 객체가 삭제되거나 프로그램이 종료될 때 호출됩니다.
모든 객체를 수동으로 del로 삭제하지 않아도,
Python의 가비지 컬렉터(Garbage Collector) 가 알아서 필요 없는 객체를 삭제해요.
객체가 삭제되면 __del__ 함수가 작동된다.
'''


#소멸자로 파일 정리하기
#이 클래스(설계도)는 파일을 열고 내용을 쓰고 닫는 방법이 적혀있다.
class FileHandler:
   def __init__(self,filename):
       # 클래스의 설계도를 사용할 때 자동으로 실행되는 부분이다.
       #filename : 어떤 파일을 오픈할지 알려주는 매개변수
       self.file = open(filename,'w')
       # 매개변수로 받은 파일을 열고 쓰기모드로 내용을 쓸 준비를 한다.
       print(f"{filename} 파일을 열었습니다.")
       #출력메시지 : 파일이 정상적으로 열렸음을 확인하기


   def write_data(self,data):
       # 매개변수 data에 파일에 쓸 내용을 전달받을것임
       self.file.write(data)
       print("매개변수로 전달받은 내용을 작성했습니다.")
       # 전달받은 내용을 파일에 작성한다.
       #파일은 __init__() 함수로 가장 먼저 실행되어 열려있다.


   def __del__(self):
       self.file.close()
       print("파일을 닫았습니다.")


handler = FileHandler("test.txt")
handler.write_data("hellowwwwww python")
# del handler