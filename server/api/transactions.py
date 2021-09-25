from PyQt5.QtCore import pyqtSlot, QObject


class Transactions(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
    
    @pyqtSlot()
    def example_api(self):
        print('some data is being processed')
