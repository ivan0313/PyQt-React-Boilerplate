import json

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget


class Foo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    @pyqtSlot(str, int, str, result=str)
    def foo(self, mystr, myint, myobjectjson):
        print('bar', mystr, myint)
        myobject = json.loads(myobjectjson)

        print('My Object', myobject)

        return mystr
