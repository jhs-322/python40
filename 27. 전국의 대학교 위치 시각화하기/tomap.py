import pandas as pd
import os

# 엑셀 파일 읽기
url = 'https://www.localdata.go.kr/datafile/etc/LOCALDATA_ALL_12_04_12_E.xlsx'
os.chdir(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_excel('전국민방위대피시설.xlsx', engine='openpyxl')

# '도로명주소전체'와 '시설명' 칼럼 추출
addresses = df['도로명주소전체'].dropna().tolist()
facilities = df['시설명'].dropna().tolist()
