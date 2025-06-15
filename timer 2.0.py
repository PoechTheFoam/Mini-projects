import sys
from PyQt5.QtGui import QFont, QFontDatabase,QIcon
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QWidget
class Timer(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(433,130,500,500)
        self.setWindowTitle('Timer')
        self.setWindowIcon(QIcon("C:/Users/Admins/Pictures/Images and Media/838963873699987476.webp"))
        self.label=QLabel(self)
        self.timer = QTimer(self)
        self.time=QTime(0,0,0,0)
        self.b1 = QPushButton('Start',self)
        self.b2 = QPushButton('Stop', self)
        self.b3 = QPushButton('Reset', self)
        self.initUI()
    def initUI(self):
        vbox=QVBoxLayout()
        vbox.addWidget(self.label)
        self.label.setAlignment(Qt.AlignCenter)

        self.setLayout(vbox)
        hbox=QHBoxLayout()
        hbox.addWidget(self.b1)
        hbox.addWidget(self.b2)
        hbox.addWidget(self.b3)

        vbox.addLayout(hbox)
        self.label.setText(self.time.toString())

        font_id=QFontDatabase.addApplicationFont('C:/Users/Admins/Downloads/ds_digital/DS-DIGII.TTF')
        font_family=QFontDatabase.applicationFontFamilies(font_id)[0]
        font=QFont(font_family)
        self.label.setFont(font)
        self.b1.setFont(font)
        self.b2.setFont(font)
        self.b3.setFont(font)

        self.setStyleSheet(""" 
        QPushButton {
        background-color: white;
        color:black;
        font-size:50px;
        border-radius:5px;
        border:2px solid black;
        }
        QPushButton:hover {
        background-color: lightgray;
        }
        QPushButton:pressed {
        background-color: gray
        }
        QLabel{
        background-color: lightblue;
        font-size:50px;
        border-radius:5px;
        color:white
        }""")
        self.b1.clicked.connect(self.Start)
        self.b2.clicked.connect(self.Stop)
        self.b3.clicked.connect(self.Reset)
        self.format=self.format
        self.timer.timeout.connect(self.display)
    def Start(self):
        self.timer.setInterval(10)
        self.timer.start()
    def Stop(self):
        self.timer.stop()
    def Reset(self):
        self.timer.stop()
        self.time=QTime(0,0,0,0)
        self.label.setText(self.format())
    def format(self):
        time=self.time
        hours=time.hour()
        minutes=time.minute()
        seconds=time.second()
        milliseconds=time.msec()//10
        fformat=f"{hours:02}:{minutes:02}:{seconds:02}:{milliseconds:02}"
        return fformat
    def display(self):
        self.label.setText(self.format())
        self.time=self.time.addMSecs(10)
def main():
    app = QApplication(sys.argv)
    timer = Timer()
    timer.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()