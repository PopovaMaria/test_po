from PyQt5.QtWidgets import (QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox)


class CalculatorView(QWidget):

    def __init__(self, *, parent=None):
        super().__init__(parent)
        self._layout = QVBoxLayout()
        self.setLayout(self._layout)

        self.first_number_input = QLineEdit()
        self.second_number_input = QLineEdit()
        self._actions = QHBoxLayout()

        self.plus_button = QPushButton("+")
        self.minus_button = QPushButton("-")
        self.multiply_button = QPushButton("*")
        self.divide_button = QPushButton("÷")

        self._actions.addWidget(self.plus_button)
        self._actions.addWidget(self.minus_button)
        self._actions.addWidget(self.multiply_button)
        self._actions.addWidget(self.divide_button)

        self._result_view = QLineEdit()
        self._result_view.setEnabled(False)

        self._layout.addWidget(self.first_number_input)
        self._layout.addWidget(self.second_number_input)
        self._layout.addLayout(self._actions)
        self._layout.addWidget(self._result_view)

        self.error_message_box = QMessageBox(parent=self)
        self._layout.addWidget(self.error_message_box)

    @property
    def result(self):
        return self._result_view.text()

    @result.setter
    def result(self, value: str):
        self._result_view.setText(value)
