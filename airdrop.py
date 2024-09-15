import sys
from PyQt5.QtWidgets import QApplication
from gui.main_window import AirDropApp

def main():
    # Initialize QApplication before creating any widgets
    app = QApplication(sys.argv)

    # Create and show the main window
    main_window = AirDropApp()
    main_window.show()

    # Execute the application event loop
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
