# networking/network_manager.py

import socket
import threading
from PyQt5.QtCore import pyqtSignal, QObject

class NetworkManager(QObject):
    transfer_status = pyqtSignal(str)  # Signal for file transfer status

    def __init__(self):
        super().__init__()
        self.devices = {}

    def send_file(self, device_ip, file_path):
        thread = threading.Thread(target=self._send_file, args=(device_ip, file_path))
        thread.start()

    def _send_file(self, device_ip, file_path):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((device_ip, 5001))
                with open(file_path, 'rb') as file:
                    while chunk := file.read(1024):
                        sock.send(chunk)
                    sock.send(b'EOF')
            self.transfer_status.emit(f"File {file_path} sent to {device_ip}")
        except Exception as e:
            self.transfer_status.emit(f"Failed to send file: {str(e)}")

    def receive_file(self, save_path):
        thread = threading.Thread(target=self._receive_file, args=(save_path,))
        thread.start()

    def _receive_file(self, save_path):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.bind(('0.0.0.0', 5001))
                sock.listen(1)
                conn, addr = sock.accept()
                with conn:
                    with open(save_path, 'wb') as file:
                        while True:
                            data = conn.recv(1024)
                            if data == b'EOF':
                                break
                            file.write(data)
            self.transfer_status.emit(f"File received and saved to {save_path}")
        except Exception as e:
            self.transfer_status.emit(f"Failed to receive file: {str(e)}")
