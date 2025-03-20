import pandas as pd 
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
file = '고등교육기관 하반기 주소록(2020).xlsx'

df_from_excel = pd.read_excel(file, engine='openpyxl')
df_from_excel.columns = df_from_excel.loc[4].tolist()
df_from_excel = df_from_excel.drop(index = list(range(0,5)))
# df_from_excel = pd.read_excel(file, skiprows=4, engine='openpyxl')
# df_from_excel.columns = df_from_excel.iloc[0]  # 첫 번째 행을 컬럼명으로 사용
# df_from_excel = df_from_excel[1:].reset_index(drop=True)  # 컬럼명 설정 후 첫 행 삭제
# df_from_excel = df_from_excel.drop(index = list(range(0,5)))


print(df_from_excel.head())
print(df_from_excel['학교명'].values)
print(df_from_excel['주소'].values)

