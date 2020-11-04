from unittest.mock import patch, Mock

import pytest
from PyQt5 import QtCore

from calculator_view import CalculatorView
from calculator_presenter import CalculatorPresenter


@pytest.mark.parametrize(
    "button_name, slot_name",
    (
        ("plus_button", "on_plus_clicked"),
        ("minus_button", "on_minus_clicked"),
        ("multiply_button", "on_multiply_clicked"),
        ("divide_button", "on_divide_clicked"),
    ),
)
def test_view_redirect_call_to_presenter(button_name: str, slot_name: str, qtbot):
    view = CalculatorView()

    mock_slot = Mock()
    with patch.object(CalculatorPresenter, slot_name, new=mock_slot):
        _ = CalculatorPresenter(calculator=Mock(), view=view)

        button = getattr(view, button_name)
        qtbot.mouseClick(button, QtCore.Qt.LeftButton)

        mock_slot.assert_called_once()


def test_view__division_by_zero__call_message_box(qtbot):
    view = CalculatorView()

    message_box_mock = Mock()
    message_box_mock.critical = Mock()

    mock_calculator = Mock()
    mock_calculator.calculate_divide = Mock(side_effect=ValueError)

    with patch.object(view, "error_message_box", new=message_box_mock):
        _ = CalculatorPresenter(calculator=mock_calculator, view=view)

        view.first_number_input.setText("1")
        view.second_number_input.setText("0")
        qtbot.mouseClick(view.divide_button, QtCore.Qt.LeftButton)

        message_box_mock.critical.assert_called_once()
