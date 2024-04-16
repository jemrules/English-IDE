![classdiagram](https://raw.githubusercontent.com/jemrules/English-IDE/main/readmeAssets/classdiagram_dark.png#gh-dark-mode-only)
![classdiagram](https://raw.githubusercontent.com/jemrules/English-IDE/main/readmeAssets/classdiagram_light.png#gh-light-mode-only)
## What is English IDE?
English IDE is just like a programming IDE, but it gives you grammer errors and spelling errors. It will also be able to eventually have auto-complete for the rest of the sentence. *Sentence auto-complete may only be finished after individual projects end.*

## How are things organized?
- English IDE uses **Python as the main language.** English IDE uses **PyQt5** for Python to make a gui.
- **We use Rust for the auto-correct and auto-complete.** This is because **Rust is 2x to 50x faster than Python**. So the much heavier work is done on Rust.
- We use **maturin** to make Rust programs into python packages.

## How to run
*English IDE rust end is not compiled. This means you will not get autocorrect.*
1. Install Packages by running **InstallPackages.py** or by using **pip3 install -r requirements.txt**.
2. Use what every method you would like to **open "EngIDE.py"**


### Credits
 - **dwyl** for the word list that I use for the auto-correct. [Link to dwyl's word lists](https://github.com/dwyl/english-words/tree/master)