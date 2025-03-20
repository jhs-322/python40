import psutil

cpu = psutil.cpu_freq()
print("cpu속도 : ",end='') #객체반환->f-string쓰거나 따로 써야함
print(cpu) # cpu의 속도

cpu_core = psutil.cpu_count(logical=False)
print("cpu 코어수 : ",end='')
print(cpu_core) # cpu의 물리 코어 수

memory = psutil.virtual_memory()
print("메모리 정보 : ",end='')
print(memory) # 메모리 정보

disk = psutil.disk_partitions()
print("디스크 정보 : ",end='')
print(disk) # disk 정보

net = psutil.net_io_counters()
print("네트워크 데이터량 : ",end='')
print(net) # 네트워크로 주고받은 데이터량을 출력