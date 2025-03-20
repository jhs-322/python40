import psutil

cpu = psutil.cpu_freq().current
print(f"cpu속도 : {round(cpu/1000, 2)}GHz")

cpu_core = psutil.cpu_count(logical=False)
print(f"코어 : {cpu_core}개")

memory = psutil.virtual_memory().total
print(f"메모리 : {round(memory/2**30,2)}GB")

disk = psutil.disk_partitions()
for p in disk:
    print(p.mountpoint, p.fstype, end='')
    du = psutil.disk_usage(p.mountpoint).total
    print(f"디스크 크기 : {round(du/2**30, 2)}GB")

net = psutil.net_io_counters()
print(f"보내기 : {round(net.bytes_sent/2**20,2)}MB, 빋기 :{round(net.bytes_recv/2**20,2)}MB")
