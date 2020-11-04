import unittest.mock as mock

import pytest

from calculator import Calculator
from calculator_presenter import CalculatorPresenter


@pytest.fixture
def calculator():
    return Calculator()


@pytest.fixture
def context():
    calculator = mock.Mock()

    view = mock.Mock()
    view.first_number_input.text = mock.Mock(return_value='4')
    view.second_number_input.text = mock.Mock(return_value='2')

    presenter = CalculatorPresenter(calculator, view)

    return calculator, view, presenter
