import pyautogui
import pyperclip
import time
import datetime

def calculate_cnt(start_date):
    today = datetime.date.today()  # 현재 날짜 가져오기
    cnt = 1  # 초기값 설정
    current_date = start_date

    while current_date < today:
        current_date += datetime.timedelta(days=1)  # 하루 증가
        if current_date.weekday() < 5:  # 0~4: 평일만
            cnt += 1

    return cnt

# # 북마크 노션(정보보안3기과정) 접속
# pyautogui.moveTo(1089, 128)
# pyautogui.click()
# time.sleep(2)

# # 측면 바 이동, TIL 클릭
# pyautogui.moveTo(1907, 652)
# pyautogui.doubleClick()
# time.sleep(2)

# pyautogui.moveTo(1700, 510)
# pyautogui.click()
# time.sleep(2)

# 날짜 분석
start_date = datetime.date(2025, 2, 24)
cnt = calculate_cnt(start_date)
pyautogui.click()
print(f"현재 cnt 값: {cnt}")

# # TIL 리스트 생성
# pyautogui.moveTo(1909, 986)  # 측면 바 이동
# pyautogui.doubleClick()

pyautogui.moveTo(1111, 600 + (cnt - 1) * 40)  # 새 페이지 - 한 칸에 40
pyautogui.click()


round = cnt + 2
pyautogui.moveTo(1383, 600)  # 제목
pyautogui.click()
pyautogui.hotkey("ctrl", "a")  # template 지우기
pyautogui.hotkey("del")
pyperclip.copy("미니 프로그램 " + str(round))  # 회차 텍스트 복사
pyautogui.hotkey("ctrl", "v")
pyautogui.moveTo(1010, 763)  # 바탕 누르기
pyautogui.click()


# # 기본 값 세팅
# time.sleep(2)
# pyautogui.click()
# pyautogui.moveTo(1202, 384)  # 날짜 지정 클릭
# pyautogui.click()
# pyautogui.hotkey("ctrl", "a")
# time.sleep(2)
# pyautogui.hotkey("ctrl", "x")
# time.sleep(2)
# pyautogui.hotkey("ctrl", "v")  # 편집한 뒤 나와야 수정 가능
# time.sleep(2)
# pyautogui.moveTo(1010, 763)  # 바탕 누르기
# pyautogui.click()

# pyautogui.moveTo(1265, 598)  # 수업
# pyautogui.click()
# time.sleep(1)
# pyautogui.moveTo(1282, 860)  # 파이썬 실습
# pyautogui.doubleClick()
# pyautogui.moveTo(1010, 763)  # 바탕 누르기
# pyautogui.click()



# # pyautogui.moveTo(1460, 600 + (cnt - 1) * 40)  # 문서 열기
# # pyautogui.click()
