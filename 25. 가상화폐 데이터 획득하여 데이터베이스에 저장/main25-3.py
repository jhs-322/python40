import pandas as pd 
import sqlite3

#파일 읽기
db_path = r"25. 가상화폐 데이터 획득하여 데이터베이스에 저장\coin.db"
#db접속
con = sqlite3.connect(db_path, isolation_level=None)
# select문 쿼리 실행 -> 데이터조회, 
readed_df = pd.read_sql("SELECT * FROM 'BTC'", con, index_col='index')
# 출력 : 쿼리언어 mysql postgresql sqlite since 1970
print(readed_df)