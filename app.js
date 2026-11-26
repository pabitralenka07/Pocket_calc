class Calculator {
  constructor(mainDisplayEl, historyDisplayEl) {
    this.mainDisplayEl = mainDisplayEl;
    this.historyDisplayEl = historyDisplayEl;

    this.MAX_DIGITS = 8;
    this.MAX_DECIMAL_PLACES = 3;

    this.reset();
  }

  reset() {
    this.currentValue = '0';
    this.previousValue = null;
    this.operator = null;
    this.isNewInput = true;
    this.lastAction = 'init';
    this.isError = false;
    this.activeOperatorBtn = null;
    this.historyText = '';
    
    this.lastOperand = null;
    this.lastExecutedOp = null;

    this.updateUI();
  }

  getDigitCount(str) {
    return str.replace(/[^0-9]/g, '').length;
  }

  getDecimalCount(str) {
    if (!str.includes('.')) return 0;
    const parts = str.split('.');
    return parts[1] ? parts[1].length : 0;
  }

  setError() {
    this.isError = true;
    this.currentValue = 'ERR';
    this.previousValue = null;
    this.operator = null;
    this.historyText = '';
    this.updateUI();
  }

  clearAll() {
    this.reset();
  }

  clearEntry() {
    if (this.isError) {
      this.reset();
      return;
    }

    if (this.lastAction === 'operator') {
      this.operator = null;
      this.currentValue = this.previousValue !== null ? this.previousValue : '0';
      this.previousValue = null;
      this.historyText = '';
      this.isNewInput = false;
      this.lastAction = 'clear';
    } else {
      this.currentValue = '0';
      this.isNewInput = true;
      this.lastAction = 'clear';
    }

    this.updateUI();
  }

  inputDigit(digit) {
    if (this.isError) {
      this.reset();
    }

    const currentDigits = this.getDigitCount(this.currentValue);

    if (this.isNewInput) {
      this.currentValue = digit.toString();
      this.isNewInput = false;
    } else {
      if (currentDigits >= this.MAX_DIGITS) {
        return;
      }

      if (this.currentValue.includes('.') && this.getDecimalCount(this.currentValue) >= this.MAX_DECIMAL_PLACES) {
        return;
      }

      if (this.currentValue === '0') {
        this.currentValue = digit.toString();
      } else {
        this.currentValue += digit.toString();
      }
    }

    this.lastAction = 'digit';
    this.updateUI();
  }

  inputDecimal() {
    if (this.isError) {
      this.reset();
    }

    if (this.isNewInput) {
      this.currentValue = '0.';
      this.isNewInput = false;
      this.lastAction = 'decimal';
      this.updateUI();
      return;
    }

    if (!this.currentValue.includes('.')) {
      this.currentValue += '.';
      this.lastAction = 'decimal';
      this.updateUI();
    }
  }

  toggleSign() {
    if (this.isError) return;
    if (this.currentValue === '0' || this.currentValue === '0.') return;

    if (this.currentValue.startsWith('-')) {
      this.currentValue = this.currentValue.slice(1);
    } else {
      this.currentValue = '-' + this.currentValue;
    }
    this.lastAction = 'negate';
    this.updateUI();
  }

  setOperator(op) {
    if (this.isError) return;

    if (this.operator && !this.isNewInput) {
      const success = this.calculate();
      if (!success) return;
    }

    this.previousValue = this.currentValue;
    this.operator = op;
    this.isNewInput = true;
    this.lastAction = 'operator';

    const opSymbol = this.getOpSymbol(op);
    this.historyText = `${this.previousValue} ${opSymbol}`;
    this.updateUI();
  }

  equals() {
    if (this.isError) return;

    if (this.operator && this.previousValue !== null) {
      this.lastOperand = this.currentValue;
      this.lastExecutedOp = this.operator;
      this.calculate();
      this.operator = null;
      this.previousValue = null;
    } else if (this.lastExecutedOp && this.lastOperand !== null) {
      this.previousValue = this.currentValue;
      this.operator = this.lastExecutedOp;
      this.currentValue = this.lastOperand;
      this.calculate();
      this.operator = null;
      this.previousValue = null;
    }

    this.historyText = '';
    this.lastAction = 'equals';
    this.isNewInput = true;
    this.updateUI();
  }

  calculate() {
    const a = parseFloat(this.previousValue);
    const b = parseFloat(this.currentValue);

    if (isNaN(a) || isNaN(b)) return true;

    const decA = this.getDecimalCount(this.previousValue.toString());
    const decB = this.getDecimalCount(this.currentValue.toString());
    const targetDecimals = Math.min(this.MAX_DECIMAL_PLACES, Math.max(decA, decB));

    let result = 0;

    switch (this.operator) {
      case '+':
        result = a + b;
        break;
      case '-':
        result = a - b;
        break;
      case '*':
        result = a * b;
        break;
      case '/':
        if (b === 0) {
          this.setError();
          return false;
        }
        result = a / b;
        break;
      default:
        return true;
    }

    let formattedResult;
    if (targetDecimals > 0) {
      formattedResult = parseFloat(result.toFixed(targetDecimals)).toString();
    } else {
      formattedResult = parseFloat(result.toFixed(this.MAX_DECIMAL_PLACES)).toString();
    }

    const digitCount = this.getDigitCount(formattedResult);

    if (digitCount > this.MAX_DIGITS || !isFinite(result)) {
      this.setError();
      return false;
    }

    this.currentValue = formattedResult;
    return true;
  }

  getOpSymbol(op) {
    switch (op) {
      case '+': return '+';
      case '-': return '−';
      case '*': return '×';
      case '/': return '÷';
      default: return '';
    }
  }

  updateUI() {
    this.mainDisplayEl.textContent = this.currentValue;
    this.historyDisplayEl.textContent = this.historyText;

    if (this.isError) {
      this.mainDisplayEl.classList.add('error-state');
    } else {
      this.mainDisplayEl.classList.remove('error-state');
    }

    if (this.currentValue.length > 9) {
      this.mainDisplayEl.style.fontSize = '2.0rem';
    } else if (this.currentValue.length > 7) {
      this.mainDisplayEl.style.fontSize = '2.3rem';
    } else {
      this.mainDisplayEl.style.fontSize = '2.7rem';
    }

    document.querySelectorAll('.btn-operator').forEach((btn) => {
      if (this.operator && btn.dataset.op === this.operator && this.isNewInput) {
        btn.classList.add('active-operator');
      } else {
        btn.classList.remove('active-operator');
      }
    });
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const mainDisplay = document.getElementById('main-display');
  const historyDisplay = document.getElementById('history-display');
  const calc = new Calculator(mainDisplay, historyDisplay);

  document.querySelector('.keypad').addEventListener('click', (e) => {
    const btn = e.target.closest('button');
    if (!btn) return;

    const action = btn.dataset.action;
    const val = btn.dataset.val;
    const op = btn.dataset.op;

    switch (action) {
      case 'digit':
        calc.inputDigit(val);
        break;
      case 'decimal':
        calc.inputDecimal();
        break;
      case 'operator':
        calc.setOperator(op);
        break;
      case 'equals':
        calc.equals();
        break;
      case 'clear-entry':
        calc.clearEntry();
        break;
      case 'clear-all':
        calc.clearAll();
        break;
      case 'negate':
        calc.toggleSign();
        break;
    }
  });

  const themeToggle = document.getElementById('theme-toggle');
  const savedTheme = localStorage.getItem('calc-theme') || 'dark';
  if (savedTheme === 'light') {
    document.documentElement.setAttribute('data-theme', 'light');
  }

  themeToggle.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    if (newTheme === 'light') {
      document.documentElement.setAttribute('data-theme', 'light');
    } else {
      document.documentElement.removeAttribute('data-theme');
    }
    localStorage.setItem('calc-theme', newTheme);
  });

  window.addEventListener('keydown', (e) => {
    if (e.key >= '0' && e.key <= '9') {
      calc.inputDigit(e.key);
    } else if (e.key === '.') {
      calc.inputDecimal();
    } else if (e.key === '+' || e.key === '-') {
      calc.setOperator(e.key);
    } else if (e.key === '*') {
      calc.setOperator('*');
    } else if (e.key === '/') {
      e.preventDefault();
      calc.setOperator('/');
    } else if (e.key === 'Enter' || e.key === '=') {
      e.preventDefault();
      calc.equals();
    } else if (e.key === 'Backspace' || e.key === 'Escape') {
      calc.clearEntry();
    } else if (e.key === 'Delete') {
      calc.clearAll();
    }
  });
});
