# 줌 참여 자동화
import time
import pyperclip
import pyautogui

#줌 클릭
pyautogui.moveTo(1350,1050) 
pyautogui.click()
time.sleep(2)

# join 버튼
pyautogui.moveTo(820,400) 
pyautogui.click()
time.sleep(2)

# 회의 아이디
pyautogui.moveTo(1140,459) 
pyautogui.click()
pyautogui.moveTo(989,525) 
pyautogui.click()
time.sleep(2)

# 비디오/오디오 옵션
pyautogui.moveTo(766,587) 
pyautogui.click()
pyautogui.moveTo(766,623) 
pyautogui.click()
time.sleep(2)

# 참가 버튼
pyautogui.moveTo(973,675) 
pyautogui.click()
time.sleep(2)

# 비밀번호
pyautogui.moveTo(840,459) 
pyautogui.click()
pyperclip.copy("250205")
pyautogui.hotkey("ctrl","v")
time.sleep(2)
pyautogui.moveTo(952,672)
pyautogui.click()

# 미리보기 join
pyautogui.moveTo(1260,780)
pyautogui.click()



