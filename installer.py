import os
import time
import platform
print('''
██╗███╗░░██╗░██████╗████████╗░█████╗░██╗░░░░░██╗░░░░░███████╗██████╗░
██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗██║░░░░░██║░░░░░██╔════╝██╔══██╗
██║██╔██╗██║╚█████╗░░░░██║░░░███████║██║░░░░░██║░░░░░█████╗░░██████╔╝
██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║██║░░░░░██║░░░░░██╔══╝░░██╔══██╗
██║██║░╚███║██████╔╝░░░██║░░░██║░░██║███████╗███████╗███████╗██║░░██║
╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝╚═╝░░╚═╝''')

print("\n")
time.sleep(1)
if platform.system() == 'Linux':
    try:
        print('Installing Dependencies...')
        os.system('sudo apt update -y && sudo apt install python3 -y && sudo apt install python3-pip && pip3 install py-cpuinfo')
        print('All Dependencies Installed Successfully')
        print('Use python3 index.py')
    except:
        print('Unknown error')


if platform.system() == 'Windows':
    try:
        os.system('pip3 install py-cpuinfo')
        print('All Dependencies Installed Successfully')
        print('Use python3 index.py')
    except:
        print('Unknown Error')