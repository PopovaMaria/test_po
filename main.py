import sys

from PyQt5.QtWidgets import QApplication

from project.calculator_view import CalculatorView
from project.calculator_presenter import CalculatorPresenter
from project.calculator import Calculator

if __name__ == '__main__':

    app = QApplication(sys.argv)
    view = CalculatorView()
    calculator = Calculator()

    controller = CalculatorPresenter(calculator, view)
    view.show()
    app.exec()
