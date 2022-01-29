import os
import platform
import socket
import cpuinfo

# Local IPV4
localIPV4 = socket.gethostbyname(socket.gethostname())
print('IPV4: ' + localIPV4)

# CPU
CPU = cpuinfo.get_cpu_info()['brand_raw']
print('CPU: ' +  CPU)

# ARCH
archInfo = cpuinfo.get_cpu_info()['arch']
print('ARCH: ' + archInfo)

# OS
osName = platform.system()
print('OS: ' + osName)