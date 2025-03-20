# 미니 프로젝트
# 숫자 맞추기 (+예외처리)

# 1-100까지 임의의 숫자를 컴퓨터가 배정, 그 수를 up,down형태로 맞추기

import random

random_n = random.randint(1,100)
game_cnt = 1

while True:
    try:
        guess_num = int(input("1~100사이의 숫자를 입력하세요: "))
        if (guess_num==random_n):
            print(f"축하합니다. {game_cnt}회 만에 맞췄습니다.")
            break;
        elif (guess_num>random_n):
            print("다운")
        else:
            print("업")
        game_cnt+=1
    except:
        print("잘못된 입력입니다. 숫자를 입력하세요")

