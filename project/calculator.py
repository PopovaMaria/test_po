

class Calculator:
    def calculate_add(self, lhs, rhs):
        return lhs + rhs

    def calculate_substract(self, lhs, rhs):
        return lhs - rhs

    def calculate_multiply(self, lhs, rhs):
        return lhs * rhs

    def calculate_divide(self, lhs, rhs):
        try:
            lhs / rhs
        except ZeroDivisionError as exc:
            raise ValueError('division by zero') from exc
        return lhs / rhs
