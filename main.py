import sys

from PyQt5.QtWidgets import QApplication

from calculator_view import CalculatorView
from calculator_presenter import CalculatorPresenter
from calculator import Calculator

if __name__ == '__main__':

    app = QApplication(sys.argv)
    view = CalculatorView()
    calculator = Calculator()

    controller = CalculatorPresenter(calculator, view)
    view.show()
    app.exec()
