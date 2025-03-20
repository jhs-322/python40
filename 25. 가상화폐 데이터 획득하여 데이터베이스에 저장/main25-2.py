import pyupbit
import sqlite3
import os

ticker = 'KRW-BTC' #비트코인
interval = 'minute1' #1분단위 데이터
to = '2025-03-05 11:00' # -까지, 기간 설정
count = 50000 #10000개 데이터 행 불러오기

#데이터 요청하고 가져오기
price_now = pyupbit.get_ohlcv(ticker = ticker, interval = interval, to= to, count = count)

# os.chdir(os.path.dirname(os.path.abspath(__file__)))
# db_path = 'coin.db'
db_path = r"25. 가상화폐 데이터 획득하여 데이터베이스에 저장\coin.db"
con = sqlite3.connect(db_path, isolation_level = None)
price_now.to_sql('BTC', con, if_exists='append')
con.close