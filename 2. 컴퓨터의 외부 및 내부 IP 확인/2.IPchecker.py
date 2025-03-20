# import socket

# # 컴퓨터 내부 ip 알아보기(가상환경 등에 영향o)
# in_addr = socket.gethostbyname(socket.gethostname())
# print(in_addr)

# # 컴퓨터 내부 ip (외부사이트 접속 정보를 바탕으로. 외부 환경 영향 x)
# in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# in_addr.connect(("www.google.co.kr", 443))
# print(in_addr.getsockname()[0])

# # 둘 다 동일하게 192.168.0.12

# #컴퓨터의 외부 ip (접속한 사이트)
# import requests
# import re

# req = requests.get("http://ipconfig.kr")
# # out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3})\.\d{1,3}\.\d{1,3})', req.text)[1]
# # out_addr = re.search(r'IP Address\s*:\s*(\d+\.\d+\.\d+\.\d+)', req.text)
# print(out_addr)

import socket
import requests
import re

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.co.kr", 443))
print("내부 IP")
