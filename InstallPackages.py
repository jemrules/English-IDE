import sys
import os
import platform as pl

oskey={"windows":"win","darwin":"macos"}

streamline=False
if len(sys.argv)>1:
    if sys.argv[1]=="-r" or sys.argv[1]=="--rust":
        streamline=True
        print("Rust installation...")

print("Installing requirements...")
f=open('requirements.txt', 'r')
for line in f:
    print(" ".join(line.replace("==","=").split('=')))
f.close()
if sys.platform == 'win32':
    if not streamline:
        os.system('pip install -r requirements.txt')
    print("INSTALLING RUST END")
    if streamline==True:
        os.system("cd src\\english-rs\\ && maturin build")
        os.system("cd ..\\..\\")
        os.system(f'pip uninstall english-rs -y')
    os.system(f'pip install src\\english-rs\\target\\wheels\\english_rs-0.1.0-cp37-none-win_amd64.whl')
else:
    os.system('pip3 install -r requirements.txt')
    print("INSTALLING RUST END")
    dirs=os.listdir("src/english-rs/target/wheels/")
    fName=[x for x in dirs if x.__contains__(oskey[pl.system().lower()])][0]
    if streamline==True:
        os.system("cd src/english-rs/ && python3 -m maturin build")
        os.system("cd ../../")
        os.system(f'pip3 uninstall english-rs -y')
    os.system(f'pip3 uninstall english-rs -y')
    os.system(f'pip3 install src/english-rs/target/wheels/{fName}')