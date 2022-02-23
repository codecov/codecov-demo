const calc = require('./calculator');

describe('Calculator test suite', () => {
  test('calculator clears', () => {
    const calculator = new calc.Calculator();
    calculator.clear();

    expect(calculator.currentOperand).toBe('');
    expect(calculator.previousOperand).toBe('');
    expect(calculator.operation).toBe(undefined);
    expect(calculator.validOperand).toBe(true);
  })

  test('calculator can input numbers', () => {
    const calculator = new calc.Calculator();
    calculator.appendNumber(1);
    expect(calculator.currentOperand).toBe('1');

    calculator.appendNumber(2);
    expect(calculator.currentOperand).toBe('12');
  })

  test('calculator can deletes', () => {
    const calculator = new calc.Calculator();
    calculator.appendNumber(1);
    expect(calculator.currentOperand).toBe('1');

    calculator.appendNumber(2);
    expect(calculator.currentOperand).toBe('12');

    calculator.delete();
    expect(calculator.currentOperand).toBe('1');
  })

  test('test operation', () => {
    const calculator = new calc.Calculator();
    calculator.chooseOperation('+');
    expect(calculator.operation).toBeUndefined();

    calculator.appendNumber(1);
    calculator.appendNumber(2);
    calculator.chooseOperation('+');
    expect(calculator.currentOperand).toBe('');
    expect(calculator.operation).toBe('+');
    expect(calculator.previousOperand).toBe('12');

    calculator.appendNumber(3);
    calculator.appendNumber(4);
    expect(calculator.currentOperand).toBe('34');
    expect(calculator.operation).toBe('+');
    expect(calculator.previousOperand).toBe('12');
  })
})
