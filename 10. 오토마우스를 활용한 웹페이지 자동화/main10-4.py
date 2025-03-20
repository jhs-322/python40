import pyautogui
import time
import pyperclip
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

weather = ["서울 날씨", "시흥 날씨", "청주 날씨", "부산 날씨", "강원도 날씨"]

addr_x = 1236
addr_y = 155

start_x = 1001
start_y = 305
end_x = 1832
end_y = 923

for localwth in weather:
    # 초기화
    pyautogui.moveTo(addr_x, addr_y, 1)
    pyautogui.click()
    pyautogui.write(["enter"])
    # 검색
    pyperclip.copy(localwth) 
    pyautogui.hotkey("ctrl", "v")
    pyautogui.write(["enter"])
    time.sleep(1)
    # 스크린샷 저장
    save_path = localwth + '.png'
    pyautogui.screenshot(save_path, region=(start_x, start_y, end_x-start_x, end_y-start_y))

