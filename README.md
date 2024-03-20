## What is English IDE?
English IDE is just like a programming IDE, but it gives you grammer errors and spelling errors. It will also be able to eventually have auto-complete for the rest of the sentence. *Sentence auto-complete may only be finished after individual projects end.*

## How are things organized?
- English IDE uses **Python as the main language.** English IDE uses **PyQt5** for Python to make a gui.
- **We use Rust for the auto-correct and auto-complete.** This is because **Rust is 2x to 50x faster than Python**. So the much heavier work is done on Rust.
- We use **maturin** to make Rust programs into python packages.
