import pyautogui
import time
import pyperclip
import tkinter as tk
import tkinter.font

window = tk.Tk()
window.title("Jekyll＆Hyde Ticketing")
window.geometry("500x300+800+300")
window.resizable(False, False)

noPause = False  # 실행 중인지
isPaused = False # 아닌지

# start 버튼
def Clicked():
    global noPause, isPaused
    if not noPause:  
        noPause = True
        isPaused = False
        print("실행되었습니다.")
        run_task()

# 메인 작업
def run_task():
    if noPause and not isPaused:
        # 인터파크 예매
        pyautogui.moveTo(1150,507,0.01)
        pyautogui.click()
        pyperclip.copy("인터파크 티켓") 
        pyautogui.hotkey("ctrl", "v")
        pyautogui.write(["enter"]) 
        # 링크 접속
        pyautogui.moveTo(1075,362,1)
        pyautogui.click()
        time.sleep(1)
        #검색 엔진 접근
        pyautogui.moveTo(1129,132,0.001)
        pyautogui.click()
        pyperclip.copy("지킬앤하이드") 
        pyautogui.hotkey("ctrl", "v")
        pyautogui.write(["enter"]) 
        time.sleep(1)
        # 검색결과 클릭
        pyautogui.moveTo(1192,375,0.0001)
        pyautogui.click()
        time.sleep(1)
        # 하단 바 이동
        pyautogui.moveTo(1860,1008,0.0001)
        pyautogui.click()
        # 측면 바 이동
        pyautogui.moveTo(1909,184,0.0001)
        pyautogui.click()
        #예매 버튼 클릭
        pyautogui.moveTo(1681,849,0.0001)
        pyautogui.click()
        time.sleep(1)
        #로그인
        pyautogui.moveTo(1053,364,0.1)
        pyautogui.click()
        pyperclip.copy("아이디") 
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)
        pyautogui.moveTo(1053,443,0.00001)
        pyautogui.click()
        pyperclip.copy("비밀번호") 
        pyautogui.hotkey("ctrl", "v")
        pyautogui.moveTo(1084,569,0.001)
        pyautogui.click()
        time.sleep(1)
        # 하단 바 이동
        pyautogui.moveTo(1860,1008,0.0001)
        pyautogui.click()
        # 측면 바 이동
        pyautogui.moveTo(1909,184,0.0001)
        pyautogui.click()
        #예매 버튼 클릭
        pyautogui.moveTo(1681,849,0.0001)
        pyautogui.click()
        time.sleep(3)
        #문자 입력->나중에
        pyautogui.moveTo(679,780)
        pyautogui.click()
        for i in range(139,169,10): # 139~768
            for j in range(502,690,10): #502~690
                pyautogui.moveTo(i,j,0.000001)
                pyautogui.click()
        #오류 메시지 확인
        pyautogui.moveTo(799,214)
        pyautogui.click()
        #선택완료
        pyautogui.moveTo(911,786)
        pyautogui.click()
        #문자 입력 커서
        pyautogui.moveTo(564,608)
        pyautogui.click()


# stop 버튼
def Paused():
    global isPaused
    if noPause and not isPaused:
        isPaused = True
        print("중단되었습니다.")


# 버튼 생성
button_start = tk.Button(window, overrelief="groove", text="start", width=15, command=Clicked)
button_start.pack(pady=10)

button_pause = tk.Button(window, overrelief="groove", text="stop", width=15, command=Paused)
button_pause.pack(pady=10)

# 메인 루프 실행
window.mainloop()
