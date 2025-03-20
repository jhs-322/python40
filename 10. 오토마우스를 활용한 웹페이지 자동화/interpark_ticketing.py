import pyautogui
import time
import pyperclip

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
#1129,132,0.01

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
pyperclip.copy("hhss232") 
pyautogui.hotkey("ctrl", "v")
time.sleep(1)

pyautogui.moveTo(1053,443,0.00001)
pyautogui.click()
pyperclip.copy("woskdj28@") 
pyautogui.hotkey("ctrl", "v")

pyautogui.moveTo(1084,569,0.001)
pyautogui.click()
time.sleep(1)

#다시 예매 버튼

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

for i in range(139,768,10): # 139~
    for j in range(502,690,10): #502
        pyautogui.moveTo(i,j,0.000001)
        pyautogui.click()
#139,502

#오류 메시지 확인
pyautogui.moveTo(799,214)
pyautogui.click()

#선택완료
pyautogui.moveTo(911,786)
pyautogui.click()

#문자 입력 커서
pyautogui.moveTo(564,608)
pyautogui.click()
