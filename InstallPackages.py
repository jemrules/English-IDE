import sys
import os
import platform as pl

oskey={"windows":"win","darwin":"macos"}

streamline=False

print("Installing requirements...")
f=open('requirements.txt', 'r')
for line in f:
	print(" ".join(line.replace("==","=").split('=')))
f.close()
if streamline==True:
	os.system("cd src\\english-rs\\ && maturin build")
	os.system("cd ..\\..\\")
if sys.platform == 'win32':
	os.system('pip install -r requirements.txt')
	print("INSTALLING RUST END")
	os.system(f'pip uninstall english-rs -y')
	os.system(f'pip install src\\english-rs\\target\\wheels\\english_rs-0.1.0-cp37-none-win_amd64.whl')
else:
	os.system('pip3 install -r requirements.txt')
	print("INSTALLING RUST END")
	dirs=os.listdir("src/english-rs/target/wheels/")
	fName=[x for x in dirs if x.__contains__(oskey[pl.system().lower()])][0]
	print(fName)
	os.system(f'pip3 uninstall english-rs -y')
	os.system(f'pip3 install src/english-rs/target/wheels/{fName}')