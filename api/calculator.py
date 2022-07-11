class Calculator:
    def add(x, y):
        return x + y                        # pragma: no cover
    
    def subtract(x, y):
        return x - y                        # pragma: no cover
    
    def multiply(x, y):
        return x * y                        # pragma: no cover
    
    def divide(x, y):
        if y == 0:                          # pragma: no cover
            return 'Cannot divide by 0'
        return x * 1 / y                    # pragma: no cover
    