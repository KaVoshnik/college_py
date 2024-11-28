import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from decimal import Decimal
from ui_converter import Ui_MainWindow
from api_client import fetch_exchange_rates
from converter import convert_currency
import warnings

class CurrencyConverterApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.rates = {}

        self.btn_convert.clicked.connect(self.handle_conversion)
        self.btn_swap.clicked.connect(self.swap_currencies)

        self.load_rates()

    def load_rates(self):
        self.rates = fetch_exchange_rates()
        if not self.rates:
            QMessageBox.critical(self, "Error", "No exchange rates available.")
            return

        currencies = sorted(self.rates.keys())
        self.comboBox_from.addItems(currencies)
        self.comboBox_to.addItems(currencies)

    def handle_conversion(self):
        try:
            amount = Decimal(self.input_amount.text())
            from_currency = self.comboBox_from.currentText()
            to_currency = self.comboBox_to.currentText()
            rate_from = Decimal(self.rates[from_currency])
            rate_to = Decimal(self.rates[to_currency])
            result = convert_currency(amount, rate_from, rate_to)
            self.label_result.setText(f"{result:.2f} {to_currency}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error occurred: {e}")
    def swap_currencies(self):
        from_index = self.comboBox_from.currentIndex()
        to_index = self.comboBox_to.currentIndex()
        self.comboBox_from.setCurrentIndex(to_index)
        self.comboBox_to.setCurrentIndex(from_index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CurrencyConverterApp()
    window.show()
    sys.exit(app.exec_())