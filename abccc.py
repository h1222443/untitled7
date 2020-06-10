import sys,time
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QListWidget,QGridLayout


class main_(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("test")
        self.layout = QGridLayout()

        self.listFile = QListWidget(self)
        self.btnstart = QPushButton("开始",self)

        self.layout.addWidget(self.listFile,0,0,1,2)
        self.layout.addWidget(self.btnstart,1,1)

        self.btnstart.clicked.connect(self.slotAdd)
        self.setLayout(self.layout)
        self.show()

    def slotAdd(self):
        for n in range(10):
            str_n = 'file index {0}'.format(n)
            self.listFile.addItem(str_n)
            QApplication.processEvents()
            time.sleep(5)


app = QApplication([])
test = main_()
sys.exit(app.exec_())