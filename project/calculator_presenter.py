from PyQt5.QtCore import QObject


class CalculatorPresenter(QObject):
    def __init__(self, calculator, view, *, parent=None):
        super().__init__(parent)

        self._view = view
        self._view.plus_button.clicked.connect(self.on_plus_clicked)
        self._view.minus_button.clicked.connect(self.on_minus_clicked)
        self._view.multiply_button.clicked.connect(self.on_multiply_clicked)
        self._view.divide_button.clicked.connect(self.on_divide_clicked)
        self._calculator = calculator
        self._current = 0

    def on_plus_clicked(self):
        try:
            value1 = float(self._view.first_number_input.text())
            value2 = float(self._view.second_number_input.text())
            result = self._calculator.calculate_add(value1, value2)
        except ValueError:
            result = 'wrong value'
        self._current = result
        self._view.result = str(result)
        self._view.first_number_input.clear()
        self._view.second_number_input.clear()

    def on_minus_clicked(self):
        try:
            value1 = float(self._view.first_number_input.text())
            value2 = float(self._view.second_number_input.text())
            result = self._calculator.calculate_substract(value1, value2)
        except ValueError:
            result = 'wrong value'
        self._current = result
        self._view.result = str(result)
        self._view.first_number_input.clear()
        self._view.second_number_input.clear()

    def on_multiply_clicked(self):
        try:
            value1 = float(self._view.first_number_input.text())
            value2 = float(self._view.second_number_input.text())
            result = self._calculator.calculate_multiply(value1, value2)
        except ValueError:
            result = 'wrong value'
        self._current = result
        self._view.result = str(result)
        self._view.first_number_input.clear()
        self._view.second_number_input.clear()

    def on_divide_clicked(self):
        try:
            value1 = float(self._view.first_number_input.text())
            value2 = float(self._view.second_number_input.text())
            result = self._calculator.calculate_divide(value1, value2)
        except ValueError as exc:
            self._view.error_message_box.critical(self._view, "Error", str(exc))
            result = 'wrong value'
        self._current = result
        self._view.result = str(result)
        self._view.first_number_input.clear()
        self._view.second_number_input.clear()