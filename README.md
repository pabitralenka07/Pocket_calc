# Calculator Project

A responsive, glassmorphic calculator web application built in vanilla JavaScript, HTML5, and CSS3 complying with all specification rules and bonus requirements.

## 🚀 Features

### Core Requirements
- **Display**: Shows the current number entered, intermediate state, and results with formula history display.
- **Entry Pad**: Full keypad for digits `0-9`, operators (`+`, `−`, `×`, `÷`, `=`), Clear (`C`), and All Clear (`AC`).
- **Digit Restriction**: Maximum sequence length of 8 digits. Any input exceeding 8 digits is ignored.
- **Operator Processing**:
  - Chains multiple operations sequentially.
  - Repeating `=` operations.
  - Operates on previous result or preceding operands without `eval()`.
- **C (Clear) Button**: Clears the current input or, if the previous entry was an operator, reverts to the preceding number.
- **AC (Clear All) Button**: Resets all internal registers, memory, and returns display to `0`.
- **Error Handling**: Displays `ERR` when an operation exceeds the 8-digit capacity or when division by zero occurs.
- **Strict Constraint**: Calculations are performed using safe arithmetic logic without `eval()`.

### Bonus Features
- **Sign Inversion (`+/-`)**: Inverts sign between positive and negative numbers.
- **Decimal Support (`.`)**: Supports floating-point numbers up to 3 decimal places.
- **Light/Dark Theme Toggle**: Theme switcher with persistent preference saved in `localStorage`.
- **Keyboard Support**: Full keyboard input support (number keys, `/`, `*`, `-`, `+`, `Enter`, `=`, `Backspace`, `Delete`, `Escape`).
- **Responsive & Modern UI**: Glassmorphic design with subtle glow effects, smooth transitions, and mobile viewport adaptability.

## 📁 File Structure

- [index.html](file:///Users/pabitra/Downloads/new/index.html) - Application layout and markup
- [style.css](file:///Users/pabitra/Downloads/new/style.css) - Styling, variables, theme support, and animations
- [app.js](file:///Users/pabitra/Downloads/new/app.js) - Calculation engine and event controller

## 🛠️ How to Run

Simply open [index.html](file:///Users/pabitra/Downloads/new/index.html) in any modern web browser or serve it with any local HTTP server:

```bash
# Example using Python:
python3 -m http.server 8000
# Then visit http://localhost:8000
```
