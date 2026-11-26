# 📟 Pocket Calc

<p align="center">
  <img src="https://img.shields.io/badge/Language-HTML5%20%7C%20CSS3%20%7C%20JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="Languages" />
  <img src="https://img.shields.io/badge/Dependencies-Zero-brightgreen?style=for-the-badge" alt="Dependencies" />
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="License" />
</p>

<p align="center">
  A sleek, retro-hardware inspired pocket calculator web application built with pure vanilla web technologies. Designed with vintage LCD aesthetics, tactile button feedback, and safe precision arithmetic.
</p>

---

## ✨ Features

### 🧮 Core Calculator Features
- **📟 Vintage LCD Display**: High-contrast LCD styling with segmented ghost numerals (`88888888`) and operation indicators.
- **🔢 8-Digit Sequence Limit**: Strictly adheres to an 8-digit hard maximum. Any extra keystrokes beyond 8 digits are ignored.
- **🛡️ 100% Safe Arithmetic**: Operates purely through native arithmetic expressions without using `eval()` or `Function()`.
- **🔄 Smart Clear Controls**:
  - `C` (Clear Entry): Reverts the active number input, or if pressed right after an operator, restores the preceding operand.
  - `AC` (All Clear): Clears all internal work registers, resets errors, and returns the display to `0`.
- **⚠️ Error Handling (`ERR`)**: Automatically flags overflow (results exceeding 8 integer digits) and division-by-zero, locking keypad until `AC` is pressed.

### 🌟 Bonus & Accessibility
- **± Sign Inversion (`+/-`)**: Toggle between positive and negative numbers on the fly.
- **🎯 Floating Point Support (`.`)**: Accepts decimals up to 3 decimal places with integer-scaled arithmetic to eliminate JavaScript floating point inaccuracies (e.g. `0.1 + 0.2 = 0.3`).
- **🔗 Expression Chaining**: Seamlessly chain consecutive calculations (e.g., `2 + 3 × 4 = 20`).
- **🔁 Repeat Operations**: Pressing `=` consecutively repeats the last applied operator and operand.
- **🌓 Adaptive Themes**: Automatic light/dark mode honoring system preferences (`prefers-color-scheme`).
- **⌨️ Keyboard Support**: Fully controllable with your physical keyboard.

---

## ⌨️ Keyboard Shortcuts

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
├── 📄 index.html    # Semantic structure & inline retro UI styling
├── 🎨 style.css      # Alternative modular styles & glassmorphism theme
├── ⚡ app.js         # Modular Calculator class & event listeners
├── 📜 README.md     # Project documentation
└── 🙈 .gitignore    # Ignore system & editor files
```

---

## 🚀 Quick Start

No installations, build tools, or package managers required!

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/pabitralenka07/Pocket_calc.git
cd Pocket_calc
```

### 2️⃣ Run in Browser
Simply double-click `index.html` to open it in your browser, or spin up a quick local web server:

```bash
# Python 3
python3 -m http.server 3000

# Node.js (npx)
npx serve .
```

Visit [`http://localhost:3000`](http://localhost:3000) and enjoy calculating! 🎉

---

## 📜 License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute!

---

<p align="center">
  Built with ❤️ by <a href="https://github.com/pabitralenka07">Pabitra Lenka</a>
</p>
