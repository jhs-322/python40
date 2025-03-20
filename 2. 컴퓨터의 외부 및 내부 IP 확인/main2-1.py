import socket
in_addr = socket.gethostbyname(socket.gethostname())
print(in_addr)

# function 함수
def get_my_ip_addr(): 
    in_addr = socket.gethostbyname(socket.gethostname())
    return in_addr
ip = get_my_ip_addr()
print(ip)


# MAC 주소
import uuid
mac_addr = ':'.join(f'{b:02x}' for b in uuid.getnode().to_bytes(6, 'big'))
print(mac_addr)
"""맥주소 정수로 16자리
6byte씩 빅엔디안
x는 16진수라는 의미, 02는 16진수 변환한뒤 2자리 수로 만들라는 의미
6개의 바이트 배열의 요소를 : 로 연결한다
"""