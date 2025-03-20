# 컴퓨터 스펙
import psutil

# cpu_rate = round(psutil.cpu_freq/1000,2)
print(f"cpu속도 :  {psutil.cpu_freq}GHz")

cpu_core_cnt = psutil.cpu_count(logical=False)
print(f"cpu 물리 코어 : {cpu_core_cnt}개")

print(f"memory 용량 : {psutil.virtual_memory()}GB")

disk = psutil.disk_partitions()
print(disk)

net = psutil.net_io_counters()
print(f"넷: {net} ")