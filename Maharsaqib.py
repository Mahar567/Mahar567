#coding=utf-8
import os, sys, platform

os.system('https://facebook.com/groups/1050351206364380/ ')

try:
    if sys.argv[1]=='update':
        os.system('rm -rf Saqib.so Saqib32.so')
except:
    pass
os.system('rm -rf Saqib.so Sqib32.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('Saqib.so'):
        os.system('curl -L https://github.com/Mr-Saqib/executables/blob/main/Sarfraz.cpython-311.so?raw=true -o Sarfraz.so') 
        import Sarfraz
    else:
        import Sarfraz

elif bit == '32bit':
    if not os.path.isfile('Saqib32.so'):
        os.system('curl -L https://github.com/Saqib-Saqib/executables/blob/main/Sarfraz32.cpython-311.so?raw=true -o Sarfraz32.so') 
        import Saqib32
    else:
        import Saqib32
