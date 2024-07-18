from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from gui_app import GUIApp
import sys
import qdarkstyle

def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window = GUIApp()
    icon_path = "logo.png"
    window.setWindowIcon(QIcon(icon_path))
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
