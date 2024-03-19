import sys
import os

print("Installing requirements...")
f=open('requirements.txt', 'r')
for line in f:
	print(" ".join(line.replace("==","=").split('=')))
f.close()
if sys.platform == 'win32':
	os.system('pip install -r requirements.txt')
else:
	os.system('pip3 install -r requirements.txt')