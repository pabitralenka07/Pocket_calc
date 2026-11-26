import tkinter as tk
from tkinter import font
import math
from decimal import Decimal, ROUND_HALF_UP

MAX_DIGITS = 8
MAX_DECIMAL_PLACES = 3

class CalculatorEngine:
    def __init__(self):
        self.reset()

    def reset(self):
        self.acc = None
        self.op = None
        self.cur = "0"
        self.fresh = True
        self.after_op = False
        self.done = False
        self.err = False
        self.last_op = None
        self.last_operand = None

    def digit_count(self, s: str) -> int:
        return len([c for c in s if c.isdigit()])

    def dec_count(self, s: str) -> int:
        if "." not in s:
            return 0
        return len(s.split(".")[1])

    def format_number(self, n: float) -> str:
        if not math.isfinite(n):
            return None
        
        n_rounded = round(n, MAX_DECIMAL_PLACES)
        int_part_digits = len(str(int(math.fabs(n_rounded))))
        if int_part_digits > MAX_DIGITS:
            return None

        allowed_decimals = min(MAX_DECIMAL_PLACES, MAX_DIGITS - int_part_digits)
        
        dec_val = Decimal(str(n_rounded)).quantize(
            Decimal('1.' + '0' * allowed_decimals if allowed_decimals > 0 else '1'),
            rounding=ROUND_HALF_UP
        )
        s = f"{dec_val:f}"
        if "." in s:
            s = s.rstrip("0").rstrip(".")
        if s == "-0":
            s = "0"
        return s

    def calculate(self, a: float, op: str, b: float):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            if b == 0:
                return None
            return a / b
        return b

    def fail(self):
        self.err = True
        self.acc = None
        self.op = None
        self.cur = "0"
        self.fresh = True

    def input_digit(self, d: str):
        if self.err:
            return
        if self.done:
            self.acc = None
            self.op = None
            self.done = False

        if self.fresh:
            self.cur = str(d)
            self.fresh = False
        elif self.digit_count(self.cur) < MAX_DIGITS:
            if self.cur == "0":
                self.cur = str(d)
            elif self.cur == "-0":
                self.cur = "-" + str(d)
            elif "." not in self.cur or self.dec_count(self.cur) < MAX_DECIMAL_PLACES:
                self.cur += str(d)
        self.after_op = False

    def input_dot(self):
        if self.err:
            return
        if self.done:
            self.acc = None
            self.op = None
            self.done = False

        if self.fresh:
            self.cur = "0."
            self.fresh = False
        elif "." not in self.cur and self.digit_count(self.cur) < MAX_DIGITS:
            self.cur += "."
        self.after_op = False

    def set_operator(self, op: str):
        if self.err:
            return
        if self.after_op:
            self.op = op
            return

        val = float(self.cur)
        if self.op is not None and self.acc is not None:
            res = self.calculate(self.acc, self.op, val)
            if res is None:
                self.fail()
                return
            formatted = self.format_number(res)
            if formatted is None:
                self.fail()
                return
            self.acc = float(formatted)
            self.cur = formatted
        else:
            self.acc = val

        self.op = op
        self.fresh = True
        self.after_op = True
        self.done = False

    def equals(self):
        if self.err:
            return
        if self.op is None or self.acc is None:
            if self.last_op is not None and self.last_operand is not None:
                val_a = float(self.cur)
                res = self.calculate(val_a, self.last_op, self.last_operand)
                if res is None:
                    self.fail()
                    return
                formatted = self.format_number(res)
                if formatted is None:
                    self.fail()
                    return
                self.cur = formatted
                self.fresh = True
                self.done = True
            return

        b = self.acc if self.after_op else float(self.cur)
        self.last_op = self.op
        self.last_operand = b

        res = self.calculate(self.acc, self.op, b)
        if res is None:
            self.fail()
            return
        formatted = self.format_number(res)
        if formatted is None:
            self.fail()
            return

        self.cur = formatted
        self.acc = None
        self.op = None
        self.fresh = True
        self.after_op = False
        self.done = True

    def clear_entry(self):
        if self.err:
            return
        if self.after_op:
            formatted = self.format_number(self.acc) if self.acc is not None else "0"
            self.cur = formatted if formatted is not None else "0"
            self.acc = None
            self.op = None
            self.after_op = False
            self.fresh = True
        else:
            self.cur = "0"
            self.fresh = True

    def clear_all(self):
        self.reset()

    def negate(self):
        if self.err:
            return
        if self.cur == "0" and self.fresh:
            return
        if self.cur.startswith("-"):
            self.cur = self.cur[1:]
        else:
            self.cur = "-" + self.cur
        if self.after_op:
            self.after_op = False
            self.fresh = False


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pocket Calc")
        self.root.geometry("340x480")
        self.root.resizable(False, False)
        self.root.configure(bg="#2d333b")

        self.engine = CalculatorEngine()
        self.sym_map = {"+": "+", "-": "−", "*": "×", "/": "÷"}

        self.create_widgets()
        self.bind_keys()
        self.render()

    def create_widgets(self):
        display_frame = tk.Frame(self.root, bg="#8fa07c", bd=0, relief="sunken")
        display_frame.pack(padx=16, pady=(16, 12), fill="x")

        self.meta_label = tk.Label(
            display_frame,
            text="",
            font=("Courier", 11, "bold"),
            bg="#8fa07c",
            fg="#1b2618",
            anchor="e"
        )
        self.meta_label.pack(fill="x", padx=10, pady=(6, 0))

        self.display_label = tk.Label(
            display_frame,
            text="0",
            font=("Courier", 34, "bold"),
            bg="#8fa07c",
            fg="#1b2618",
            anchor="e"
        )
        self.display_label.pack(fill="x", padx=10, pady=(0, 6))

        pad_frame = tk.Frame(self.root, bg="#2d333b")
        pad_frame.pack(padx=14, pady=(0, 14), fill="both", expand=True)

        for i in range(5):
            pad_frame.rowconfigure(i, weight=1)
        for j in range(4):
            pad_frame.columnconfigure(j, weight=1)

        buttons = [
            ("AC", 0, 0, 1, "#d49a2c", "#1a1304", lambda: self.press("AC")),
            ("C",  0, 1, 1, "#d49a2c", "#1a1304", lambda: self.press("C")),
            ("+/-",0, 2, 1, "#2a8a85", "#f0fbfb", lambda: self.press("neg")),
            ("÷",  0, 3, 1, "#2a8a85", "#f0fbfb", lambda: self.press("/")),

            ("7",  1, 0, 1, "#cfcabd", "#1f2328", lambda: self.press("7")),
            ("8",  1, 1, 1, "#cfcabd", "#1f2328", lambda: self.press("8")),
            ("9",  1, 2, 1, "#cfcabd", "#1f2328", lambda: self.press("9")),
            ("×",  1, 3, 1, "#2a8a85", "#f0fbfb", lambda: self.press("*")),

            ("4",  2, 0, 1, "#cfcabd", "#1f2328", lambda: self.press("4")),
            ("5",  2, 1, 1, "#cfcabd", "#1f2328", lambda: self.press("5")),
            ("6",  2, 2, 1, "#cfcabd", "#1f2328", lambda: self.press("6")),
            ("−",  2, 3, 1, "#2a8a85", "#f0fbfb", lambda: self.press("-")),

            ("1",  3, 0, 1, "#cfcabd", "#1f2328", lambda: self.press("1")),
            ("2",  3, 1, 1, "#cfcabd", "#1f2328", lambda: self.press("2")),
            ("3",  3, 2, 1, "#cfcabd", "#1f2328", lambda: self.press("3")),
            ("+",  3, 3, 1, "#2a8a85", "#f0fbfb", lambda: self.press("+")),

            ("0",  4, 0, 2, "#cfcabd", "#1f2328", lambda: self.press("0")),
            (".",  4, 2, 1, "#cfcabd", "#1f2328", lambda: self.press(".")),
            ("=",  4, 3, 1, "#c4473a", "#ffffff", lambda: self.press("="))
        ]

        self.btn_widgets = []
        for text, r, c, cspan, bg_col, fg_col, cmd in buttons:
            btn = tk.Button(
                pad_frame,
                text=text,
                font=("Helvetica", 16, "bold"),
                bg=bg_col,
                fg=fg_col,
                activebackground=bg_col,
                relief="raised",
                bd=1,
                cursor="hand2",
                command=cmd
            )
            btn.grid(row=r, column=c, columnspan=cspan, sticky="nsew", padx=3, pady=3)
            self.btn_widgets.append((text, btn))

    def press(self, action: str):
        if action == "AC":
            self.engine.clear_all()
        elif self.engine.err:
            return
        elif action.isdigit():
            self.engine.input_digit(action)
        elif action == ".":
            self.engine.input_dot()
        elif action == "C":
            self.engine.clear_entry()
        elif action == "neg":
            self.engine.negate()
        elif action == "=":
            self.engine.equals()
        elif action in ["+", "-", "*", "/"]:
            self.engine.set_operator(action)
        self.render()

    def bind_keys(self):
        for digit in "0123456789":
            self.root.bind(digit, lambda e, d=digit: self.press(d))
        self.root.bind(".", lambda e: self.press("."))
        self.root.bind("+", lambda e: self.press("+"))
        self.root.bind("-", lambda e: self.press("-"))
        self.root.bind("*", lambda e: self.press("*"))
        self.root.bind("/", lambda e: self.press("/"))
        self.root.bind("<Return>", lambda e: self.press("="))
        self.root.bind("=", lambda e: self.press("="))
        self.root.bind("<BackSpace>", lambda e: self.press("C"))
        self.root.bind("<Escape>", lambda e: self.press("AC"))
        self.root.bind("<n>", lambda e: self.press("neg"))
        self.root.bind("<N>", lambda e: self.press("neg"))

    def render(self):
        if self.engine.err:
            self.display_label.config(text="ERR")
            self.meta_label.config(text="PRESS AC")
            for text, btn in self.btn_widgets:
                if text != "AC":
                    btn.config(state="disabled")
        else:
            self.display_label.config(text=self.engine.cur)
            op_char = self.sym_map.get(self.engine.op, "") if self.engine.op else ""
            self.meta_label.config(text=op_char)
            for text, btn in self.btn_widgets:
                btn.config(state="normal")


def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
