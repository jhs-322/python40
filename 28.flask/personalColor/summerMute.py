from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import urllib.request

# 이미지 저장할 폴더 생성
save_folder = "images"
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Selenium WebDriver 설정 (Chrome)
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")

# ★ headless 모드 OFF (직접 눈으로 확인) ★
# options.add_argument("--headless")  # 이 줄을 삭제!

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 구글 이미지 검색
search_query = "여름뮤트화장품추천"
search_url = f"https://www.google.com/search?tbm=isch&q={search_query}"
driver.get(search_url)

# 스크롤 다운 (이미지가 더 많이 로드되도록)
for _ in range(5):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    time.sleep(2)

# 이미지 요소 로드 대기
wait = WebDriverWait(driver, 10)
image_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img")))

# 이미지 URL 저장
image_urls = []
for img in image_elements[:10]:  # 상위 10개 이미지 저장
    src = img.get_attribute("src") or img.get_attribute("data-src")
    if src and "http" in src:
        image_urls.append(src)

# 이미지 다운로드
for idx, url in enumerate(image_urls):
    try:
        file_path = os.path.join(save_folder, f"img_{idx}.jpg")
        urllib.request.urlretrieve(url, file_path)
        print(f"이미지 {idx + 1} 저장 완료: {file_path}")
    except Exception as e:
        print(f"이미지 {idx + 1} 저장 실패: {e}")

driver.quit()
print(f"총 {len(image_urls)}개의 이미지를 저장했습니다.")
