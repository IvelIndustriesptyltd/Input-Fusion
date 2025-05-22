# InputFusion GUI with driver install buttons
import sys, os, subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class InputFusionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("InputFusion")
        self.setGeometry(100, 100, 350, 200)
        layout = QVBoxLayout()

        self.label = QLabel("Welcome to InputFusion!")
        layout.addWidget(self.label)

        self.vjoy_btn = QPushButton("Install VJoy Driver")
        self.vjoy_btn.clicked.connect(self.install_vjoy)
        layout.addWidget(self.vjoy_btn)

        self.vigem_btn = QPushButton("Install ViGEm Driver")
        self.vigem_btn.clicked.connect(self.install_vigem)
        layout.addWidget(self.vigem_btn)

        self.setLayout(layout)

    def install_vjoy(self):
        try:
            subprocess.run([resource_path("drivers/VJoySetup.exe")], check=True)
        except Exception as e:
            self.label.setText(f"VJoy Error: {e}")

    def install_vigem(self):
        try:
            subprocess.run([resource_path("drivers/ViGEmBusSetup.exe")], check=True)
        except Exception as e:
            self.label.setText(f"ViGEm Error: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = InputFusionApp()
    win.show()
    sys.exit(app.exec_())
