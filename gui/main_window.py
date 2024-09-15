# gui/main_window.py

from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QFileDialog, QVBoxLayout, QWidget, QListWidget, QMessageBox

from networking.network_manager import NetworkManager
from networking.zeroconf_discovery import DeviceDiscovery

class AirDropApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.device_discovery = DeviceDiscovery()
        self.network_manager = NetworkManager()
        self.initUI()
        self.setupConnections()
        self.device_discovery.start()

    def initUI(self):
        self.setWindowTitle('Airdrop-like File Transfer App')
        self.setGeometry(100, 100, 600, 400)

        # Main widget and layout
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Device list and file select button
        self.device_list = QListWidget(self)
        layout.addWidget(self.device_list)

        self.label = QLabel("Select a file to send", self)
        layout.addWidget(self.label)

        self.select_file_button = QPushButton("Select File", self)
        self.select_file_button.clicked.connect(self.open_file_dialog)
        layout.addWidget(self.select_file_button)

        self.send_button = QPushButton("Send File", self)
        self.send_button.clicked.connect(self.send_file)
        layout.addWidget(self.send_button)

        self.receive_button = QPushButton("Receive File", self)
        self.receive_button.clicked.connect(self.receive_file)
        layout.addWidget(self.receive_button)

        self.status_label = QLabel("", self)
        layout.addWidget(self.status_label)

        # Set layout to the main window
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def setupConnections(self):
        self.device_discovery.device_discovered.connect(self.update_device_list)
        self.device_discovery.device_removed.connect(self.remove_device)
        self.network_manager.transfer_status.connect(self.update_status)

    def update_device_list(self, device):
        self.device_list.addItem(device)

    def remove_device(self, device):
        items = self.device_list.findItems(device, Qt.MatchExactly)
        for item in items:
            self.device_list.takeItem(self.device_list.row(item))

    def update_status(self, status_message):
        self.status_label.setText(status_message)

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select File")
        if file_path:
            self.label.setText(f"Selected File: {file_path}")
            self.selected_file_path = file_path

    def send_file(self):
        selected_device = self.device_list.currentItem()
        if selected_device:
            device_name = selected_device.text()
            if hasattr(self, 'selected_file_path'):
                self.network_manager.send_file(device_name, self.selected_file_path)
            else:
                QMessageBox.warning(self, "Error", "No file selected.")
        else:
            QMessageBox.warning(self, "Error", "No device selected.")

    def receive_file(self):
        save_path, _ = QFileDialog.getSaveFileName(self, "Save File")
        if save_path:
            self.network_manager.receive_file(save_path)
