# API

## Creating new API group

1. Create new file in this directory

    For example, `server/api/foo.py`

2. Create new PyQt Widget using the following template

    Rename Foo to the API group's name and foo to the API's name accordingly.

    ```py
    import json

    from PyQt5.QtCore import pyqtSlot, QObject


    class Foo(QObject):
        def __init__(self, parent=None):
            super().__init__(parent)

        @pyqtSlot()
        def foo(self):
            print('bar')
    ```

3. Export API group from api module

    ```py
    # server/api/__init__.py

    from .foo import *
    ```

4. Add API group as channel to PyQt Web Server

    ```py
    # main.py

    from server.api import Foo  # Add this line

    class WebEngineView(QWebEngineView):

        def __init__(self):
            super().__init__()

            ...

            # setup channel
            self.channel = QWebChannel()
            self.channel.registerObject('foo', Foo(self))  # Add this line
            self.page().setWebChannel(self.channel)

            self.show()
    ```

## pyqtSlot

There is not a lot of examples found online regarding pyqtSlot. You may reference to the following documentation.
<https://doc.qt.io/qtforpython-6/PySide6/QtCore/Slot.html>

But for our purpose, the following guide should suffice.

### Add arguments

To add a new argument, first specify the argument type in the pyqtSlot decorator `[float, int, str]`

```py
@pyqtSlot(str, int)
def foo(self, mystr):
    print(mystr)
```

I haven't figured out how to pass python or node.js object into slots yet, for now, you may make use of json.

```py
import json

...

# Receive

@pyqtSlot(str)
def foo(self, myobjectjson):

    myobject = json.loads(myobjectjson)
    print('My Object', myobject)


# Return

@pyqtSlot(result=str)
def foo(self, myobjectjson):
    myobject = {
        'text': 'some text',
        'list': ['1', 2],
    }
    myobjectjson = json.dump(myobject)

    return myobjectjson
```
