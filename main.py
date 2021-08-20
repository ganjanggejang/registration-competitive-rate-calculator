# 홍대 수강신청 경쟁률 계산기
# 수강신청 홈페이지에 나와 있는 그대로 (4학년/3학년/2학년/1학년) 입력하면 됨.
# 추가인원은 고려하지 않음.

def cal_rate_4():
    d = hold_list[0]
    if hold_list[0] > limit_list[0]:
        d = limit_list[0]

    limit_list[1] -= d
    limit_list[2] -= d
    limit_list[3] -= d


def cal_rate_3():
    d = hold_list[1]
    if hold_list[1] > limit_list[1]:
        d = limit_list[1]

    limit_list[2] -= d
    limit_list[3] -= d


def cal_rate_2():
    d = hold_list[2]
    if hold_list[2] > limit_list[2]:
        d = limit_list[2]

    limit_list[3] -= d


print("수강신청 경쟁률 계산기")

# 담아두기 인원
hold_list = input("담아두기 인원 (ex: 10/20/30/40): ").split("/")
for n in range(len(hold_list)):
    hold_list[n] = int(hold_list[n])

# 수업 정원
limit_list = input("수업 정원 (ex: 10/20/30/40): ").split("/")
for n in range(len(limit_list)):
    limit_list[n] = int(limit_list[n])

# 학년 질문
user_grade = int(input("학년 (숫자만 입력): "))

if user_grade == 4:
    cal_rate_4()
    rate_4 = float(hold_list[0] / limit_list[0])
    print(f"담은 인원: {hold_list[0]}명, 4학년 제한 인원: {limit_list[0]}명")
    print(f"경쟁률: {rate_4:.1f} : 1 입니다.")

elif user_grade == 3:
    cal_rate_4()
    cal_rate_3()
    rate_3 = float(hold_list[1] / limit_list[1])
    print(f"담은 인원: {hold_list[1]}명, 3학년 제한 인원: {limit_list[1]}명")
    print(f"경쟁률: {rate_3:.1f} : 1 입니다.")

elif user_grade == 2:
    cal_rate_4()
    cal_rate_3()
    cal_rate_2()
    rate_2 = float(hold_list[2] / limit_list[2])
    print(f"담은 인원: {hold_list[2]}명, 2학년 제한 인원: {limit_list[2]}명")
    print(f"경쟁률: {rate_2:.1f} : 1 입니다.")

elif user_grade == 1:
    cal_rate_4()
    cal_rate_3()
    cal_rate_2()
    rate_1 = float(hold_list[3] / limit_list[3])
    print(f"담은 인원: {hold_list[3]}명, 1학년 제한 인원: {limit_list[3]}명")
    print(f"경쟁률: {rate_1:.1f} : 1 입니다.")
