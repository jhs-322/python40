# 숫자 맞추기 (+예외처리)
# 1-100까지 임의의 숫자를 컴퓨터가 배정, 그 수를 up,down형태로 맞추기

import random
randN = random.randint(1,100)
cnt = 0

while(True):
    try: 
        guess = int(input("1부터 100 사이의 숫자를 입력하세요 >> "))
        cnt+=1
        if (guess>randN):
            print("다운")
        elif (guess<randN):
            print("업")
        else:
            print(f"축하합니다. {cnt}회 만에 맞췄습니다.")
            break
    except:
        print("잘못된 입력입니다. 다시 시도하세요.") 