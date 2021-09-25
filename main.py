import os
import sys
import threading

from dotenv import load_dotenv
from PyQt5.Qt import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView

from server.utils.react import serve
from server.api import Foo, Transactions

load_dotenv()

ENVIRONMENT = os.environ['ENVIRONMENT']


class WebEngineView(QWebEngineView):

    def __init__(self):
        super().__init__()

        if ENVIRONMENT == 'production':
            self.load(QUrl("http://localhost:8000"))
        elif ENVIRONMENT == 'development':
            self.load(QUrl("http://localhost:3000"))
        else:
            raise Exception(f"Unknown environment configuration: {ENVIRONMENT}")

        # setup channel
        self.channel = QWebChannel()
        self.channel.registerObject('transactions', Transactions(self))
        self.channel.registerObject('foo', Foo(self))
        self.page().setWebChannel(self.channel)

        self.show()


if __name__ == "__main__":
    # Serve static files build using react
    if ENVIRONMENT == 'production':
        react = threading.Thread(target=serve, daemon=True)
        react.start()
    
    # Init PyQt application
    app = QApplication(sys.argv)
    view = WebEngineView()
    view.show()

    # Run Application
    sys.exit(app.exec_())
