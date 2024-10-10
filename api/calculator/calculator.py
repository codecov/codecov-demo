class Calculator:
  def add(x,y):
    return x + y
  
  def subtract(x,y):
    return x - y
  
  def multiply(x,y): 
    return x * y
  
  def divide(x,y):
    if y == 0:
      return 'Cannot divide by zero'
    return x * 1.0 / y