import sys
import os
import platform as pl

oskey={"windows":"win","darwin":"macos"}

print("Installing requirements...")
f=open('requirements.txt', 'r')
for line in f:
	print(" ".join(line.replace("==","=").split('=')))
f.close()
if sys.platform == 'win32':
	os.system('pip install -r requirements.txt')
	print("INSTALLING RUST END")
	fName=""
	dirs=os.listdir("src\\english-rs\\target\\wheels\\")
	#os.system(f'pip install src\\english-rs\\target\\wheels\\english_rs_0.1.0-cp.whl')
else:
	os.system('pip3 install -r requirements.txt')
	print("INSTALLING RUST END")
	dirs=os.listdir("src/english-rs/target/wheels/")
	fName=[x for x in dirs if x.__contains__(oskey[pl.system().lower()])][0]
	print(fName)
	#os.system(f'pip3 install src/english-rs/target/wheels/english_rs_.whl')