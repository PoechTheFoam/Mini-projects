import sys
import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QWidget, QVBoxLayout
from PyQt5.QtCore import QTime,QTimer,Qt
from PyQt5.QtGui import QFont, QFontDatabase

class Clock(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Helping you tell the time")
        self.setGeometry(300, 300, 500, 150)
        self.time=QTime()
        self.label=QLabel(self)
        self.timer = QTimer(self)
        self.initUI()
    def initUI(self):
        hbox = QHBoxLayout()
        self.setLayout(hbox)
        hbox.addWidget(self.label)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size:150px;color:lightblue")
        self.setStyleSheet("background-color:black")
        font_id=QFontDatabase.addApplicationFont('C:/Users/Admins/Downloads/ds_digital/DS-DIGII.TTF')
        font_family=QFontDatabase.applicationFontFamilies(font_id)[0]
        font=QFont(font_family,150)
        self.label.setFont(font)
        self.timer.timeout.connect(self.upd_time)
        self.timer.start(1000)
        self.upd_time()
    def upd_time(self):
        currentTime=QTime.currentTime().toString('hh:mm:ss')
        self.label.setText(currentTime)
def main():
    app = QApplication(sys.argv)
    clock = Clock()
    clock.show()
    sys.exit(app.exec())
if __name__ == '__main__':
    main()
