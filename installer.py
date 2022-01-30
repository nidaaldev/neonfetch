import os
import time
print('''
██╗███╗░░██╗░██████╗████████╗░█████╗░██╗░░░░░██╗░░░░░███████╗██████╗░
██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗██║░░░░░██║░░░░░██╔════╝██╔══██╗
██║██╔██╗██║╚█████╗░░░░██║░░░███████║██║░░░░░██║░░░░░█████╗░░██████╔╝
██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║██║░░░░░██║░░░░░██╔══╝░░██╔══██╗
██║██║░╚███║██████╔╝░░░██║░░░██║░░██║███████╗███████╗███████╗██║░░██║
╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝╚═╝░░╚═╝''')

time.sleep(1)

try:
    print('Installing Dependencies...')
    os.system('pip3 install py-cpuinfo')
except:
    print("Error Ocurred, maybe you don't have pip3 installed.")
    time.sleep(1)
try:
    os.system('sudo apt update -y && sudo apt install python3 -y && sudo apt install python3-pip')
except:
    print('Uknown error')

print('All Dependencies Installed Successfully')