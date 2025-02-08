movie_name = input("영화 이름을 입력하세요 : ")
while True: #별점이 1 ~ 5 사이가 아니라면 반복하기
    star_input = int(input("영화 평점을 입력하세요(1~5) : ")) # 평점입력받기

    if 1 <= star_input <= 5:# 1과 같거나 크고 , 5보다 작거나 같으면
        print(f"{movie_name}의 평점 : " + "⭐" * star_input)
    else:
        print("⚠️1부터 5 사이의 숫자를 입력하세요!")
        continue

    break