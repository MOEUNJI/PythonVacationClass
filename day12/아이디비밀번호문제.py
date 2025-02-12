#정해진 아이디와 비밀번호
right_id = "moeunji"
right_pw = 1234

def login(id,pw): #두 개의 매개변수를 받을거임
   if right_id == id: #매개변수로 받은 아이디가 정해진 아이디와 일치하는지 확인
       if right_pw == pw: #비밀번호도 일치하는지 확인 (아이디가 일치해야지만 확인)
           print("로그인 되었습니다.") # 아이디 비번 둘 다 일치하면 출력
       else: # 비밀번호가 일치하지 않는다면
           print("비밀번호가 일치하지 않습니다.") # 출력
   else: # 아이디가 일치하지 않는다면
       print("아이디가 일치하지 않습니다.") # 출력


# 사용자로부터 아이디와 비밀번호 입력받기
user_id = input("아이디를 입력해주세요 : ")
user_pw = int(input("비밀번호를 입력해주세요 : ")) #숫자형으로 받아옴


login(user_id, user_pw)
