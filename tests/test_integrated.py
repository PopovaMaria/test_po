from unittest.mock import patch, Mock

import pytest
from PyQt5 import QtCore

from project.calculator import Calculator
from project.calculator_view import CalculatorView
from project.calculator_presenter import CalculatorPresenter


@pytest.mark.parametrize(
    "button_name, case_data",
    (
        ("plus_button", (1.0, 2.0, 3.0)),
        ("minus_button", (1.0, 2.0, -1.0)),
        ("multiply_button", (2.0, 3.0, 6.0)),
        ("divide_button", (1.0, 2.0, 0.5)),
    ),
)
def test__integrated__success(button_name, case_data, qtbot):
    lhs, rhs, expected_result = case_data

    calculator = Calculator()
    view = CalculatorView()
    _ = CalculatorPresenter(calculator, view)

    view.first_number_input.setText(str(lhs))
    view.second_number_input.setText(str(rhs))
    button = getattr(view, button_name)
    qtbot.mouseClick(button, QtCore.Qt.LeftButton)

    assert view._result_view.text() == str(expected_result)
