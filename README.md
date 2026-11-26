# 📟 Pocket Calc

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Version" />
  <img src="https://img.shields.io/badge/GUI-Tkinter-yellow?style=for-the-badge" alt="Tkinter GUI" />
  <img src="https://img.shields.io/badge/Web-HTML5%20%7C%20CSS3%20%7C%20JS-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="Web Version" />
  <img src="https://img.shields.io/badge/Dependencies-Zero-brightgreen?style=for-the-badge" alt="Dependencies" />
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="License" />
</p>

<p align="center">
  A retro-hardware inspired pocket calculator application available in both <b>Python Desktop GUI (Tkinter)</b> and <b>Web (Vanilla HTML/CSS/JS)</b> versions. Built with vintage LCD aesthetics, zero-eval safe calculations, 8-digit sequence limits, and precision floating-point arithmetic.
</p>

---

## 🐍 Python Version (`calculator.py`)

Run natively on Windows, macOS, or Linux with zero third-party dependencies!

### 🚀 Running the Python App
```bash
python3 calculator.py
```

### ✨ Python Implementation Highlights
- **🖥️ Native Desktop Window**: Built with standard library `tkinter`.
- **📟 Retro LCD Look**: Styled matching vintage electronic pocket calculators with dark case and green LCD screen.
- **🛡️ Zero `eval()` Execution**: Performs all mathematical evaluations safely with native arithmetic operations.
- **🔢 8-Digit Sequence Limit**: Digit inputs beyond 8 digits are ignored.
- **⚡ Decimal Accuracy**: Supports floating points up to 3 decimal places using `decimal.Decimal` and `ROUND_HALF_UP` to prevent floating-point precision anomalies.
- **⚠️ Full ERR Handling**: Prevents division by zero and triggers `ERR` whenever calculation results exceed 8 integer digits, disabling the keypad until `AC` is pressed.
- **⌨️ Keyboard Bound**: Supports all standard keyboard inputs natively.

---

## 🌐 Web Version (`index.html`)

For a zero-setup browser experience:

```bash
# Simply double-click index.html or run:
python3 -m http.server 3000
```
Then visit [`http://localhost:3000`](http://localhost:3000).

---

## ⌨️ Keyboard Shortcuts (Both Desktop & Web)

| Key | Calculator Action |
|:---:|:---|
| `0` – `9` | Enter numbers |
| `.` | Decimal point (up to 3 places) |
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication (`×`) |
| `/` | Division (`÷`) |
| `Enter` or `=` | Calculate result (`=`) |
| `Backspace` | Clear Entry (`C`) |
| `Escape` | Clear All (`AC`) |
| `N` or `F9` | Negate / Invert Sign (`+/-`) |

---

## 📂 Project Structure

```bash
Pocket_calc/
├── 🐍 calculator.py   # Python desktop calculator GUI application
├── 📄 index.html      # Retro web calculator
├── 🎨 style.css       # Web styling
├── ⚡ app.js          # Web calculation engine
├── 📜 README.md       # Project documentation
└── 🙈 .gitignore     # Git ignore patterns
```

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

<p align="center">
  Built with ❤️ by <a href="https://github.com/pabitralenka07">Pabitra Lenka</a>
</p>
