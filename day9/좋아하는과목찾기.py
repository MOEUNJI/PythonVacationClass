students = {
    "철수": ["수학", "과학"],
    "영희": ["영어", "국어"],
    "민수": ["체육", "미술"],
    "지혜": ["음악", "과학"]
}

subject = input("어떤 과목을 좋아하는 학생을 찾을까요? ")

for name, subjects in students.items():
    if subject in subjects:
        print(f"{name} 학생이 {subject}을(를) 좋아해요! 😊")
