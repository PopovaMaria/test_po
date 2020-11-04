import typing as t
import unittest.mock as mock

import pytest

from project.calculator_presenter import CalculatorPresenter


@pytest.mark.parametrize(
    'presenter_slot_name, calculator_operation_name',
    (
        ('on_plus_clicked', 'calculate_add'),
        ('on_minus_clicked', 'calculate_substract'),
        ('on_divide_clicked', 'calculate_divide'),
        ('on_multiply_clicked', 'calculate_multiply'),
    ),
)
def test_operations(
    presenter_slot_name: str,
    calculator_operation_name: str,
    context: t.Tuple[mock.Mock, mock.Mock, CalculatorPresenter],
):
    calculator, view, presenter = context

    slot = getattr(presenter, presenter_slot_name)
    slot()

    view.first_number_input.text.assert_called_once()
    view.second_number_input.text.assert_called_once()

    lhs = view.first_number_input.text.return_value
    rhs = view.second_number_input.text.return_value

    callback = getattr(calculator, calculator_operation_name)
    callback.assert_called_once_with(float(lhs), float(rhs))
