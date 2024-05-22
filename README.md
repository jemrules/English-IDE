![classdiagram](https://raw.githubusercontent.com/jemrules/English-IDE/main/readmeAssets/classdiagram_dark.png#gh-dark-mode-only)
![classdiagram](https://raw.githubusercontent.com/jemrules/English-IDE/main/readmeAssets/classdiagram_light.png#gh-light-mode-only)
## What is English IDE?
English IDE is just like a programming IDE, but it gives you grammer errors and spelling errors. It will also be able to eventually have auto-complete for the rest of the sentence. *Sentence auto-complete may only be finished after individual projects end.*

## How are things organized?
- English IDE uses **Python as the main language.** English IDE uses **PyQt5** for Python to make a gui.
- **We use Rust for the auto-correct and auto-complete.** This is because **Rust is 2x to 50x faster than Python**. So the much heavier work is done on Rust.
- We use **maturin** to make Rust programs into python packages.

## How to run
_Look at "How to compile for other platforms" if you want to use on linux_
1. Install Packages by running **InstallPackages.py**. Alternatively you can manually install by running:
```bash
# For macOS
pip3 install -r requirements.txt
pip3 install src/english-rs/target/wheels/english_rs-0.1.0-cp310-cp310-macosx_11_0_arm64.whl
```
```bat
:: For Windows
pip install -r requirements.txt
pip install src\english-rs\target\wheels\english_rs-0.1.0-cp37-none-win_amd64.whl
```
2. Open *EnglishIDE for Mac* OR *EnglishIDE.exe for Windows*

## How to compile for other platforms
_You will need to have rust already installed, and be on the target machine._
Run [InstallPackages.py](https://github.com/jemrules/English-IDE/blob/Windows/InstallPackages.py) with args -r OR --rust
```bash
python InstallPackages.py -r
python3 InstallPackages.py --rust

# Run using
python -u src/EngIDE.py
```

#### Credits
 - **dwyl** for the word list that I use for the auto-correct. [Link to dwyl's word lists](https://github.com/dwyl/english-words/tree/master)
