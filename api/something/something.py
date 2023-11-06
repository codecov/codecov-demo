class Something:
    def do_something(self, x):
        x = x + 1 if x > 0 else x
        return x

    def do_something_else(self, x, y):
        return x * 2 - y
