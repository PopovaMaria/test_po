import pytest

from project.calculator import Calculator


@pytest.mark.parametrize(
    'operation_name, lhs, rhs, expected_result',
    (
        ('calculate_add', 2.0, 3, 5),
        ('calculate_add', -2.0, 3, 1),
        ('calculate_add', 0, 2.0, 2),
        ('calculate_add', 2.0, 0, 2),

        ('calculate_substract', 2.0, 3, -1),
        ('calculate_substract', -2.0, 3, -5),
        ('calculate_substract', 0, 2.0, -2),
        ('calculate_substract', 2.0, 0, 2),

        ('calculate_divide', 2.0, 3, 2.0 / 3),
        ('calculate_divide', -2.0, 3, -2.0 / 3),
        ('calculate_divide', 0, 2.0, 0),
        #('calculate_divide', 2.0, 0, 'division by zero'),

        ('calculate_multiply', 2.0, 3, 6.0),
        ('calculate_multiply', -2.0, 3, -6.0),
        ('calculate_multiply', 0, 2.0, 0),
        ('calculate_multiply', 2.0, 0, 0),
    ),
)
def test_operations(
        operation_name: str,
        lhs: float,
        rhs: float,
        expected_result: float,
        calculator: Calculator,
):
    operation = getattr(calculator, operation_name)

    value = operation(lhs, rhs)

    assert value == expected_result
