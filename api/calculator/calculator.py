class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            return 'Cannot divide by 0'
        return x * 1.0 / y

    @staticmethod
    def mod(x, y):
        return x % y
