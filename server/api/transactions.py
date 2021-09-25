from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget


class Transactions(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
    
    @pyqtSlot()
    def example_api(self):
        print('some data is being processed')
