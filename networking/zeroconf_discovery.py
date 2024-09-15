# networking/zeroconf_discovery.py

from zeroconf import Zeroconf, ServiceBrowser
from PyQt5.QtCore import pyqtSignal, QObject

class DeviceDiscovery(QObject):
    device_discovered = pyqtSignal(str)  # Signal for device discovery
    device_removed = pyqtSignal(str)  # Signal for device removal

    def __init__(self):
        super().__init__()
        self.zeroconf = Zeroconf()

    def start(self):
        self.browser = ServiceBrowser(self.zeroconf, "_http._tcp.local.", self)

    def remove_service(self, zeroconf, type, name):
        device_name = name
        self.device_removed.emit(device_name)
        print(f"Service {device_name} removed")

    def add_service(self, zeroconf, type, name):
        device_name = name
        self.device_discovered.emit(device_name)
        print(f"Service {device_name} added")

    def stop(self):
        self.zeroconf.close()
