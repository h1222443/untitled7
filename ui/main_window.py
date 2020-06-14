from typing import Dict,Any
from PyQt5.QtWidgets import QMainWindow,QWidget,QTableWidget,QDockWidget,QApplication,QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCloseEvent
from event import EventEngine
from ui.widget import Main_Monitor
import sys

class Main_Window(QMainWindow):
    def __init__(self,event_engine:EventEngine):
        super().__init__()
        self.setWindowTitle("test")
        self.event_engine = event_engine
        self.init_()

    def init_(self):
        self.init_dock()

    def init_dock(self):
        widget,area = self.create_dock(Main_Monitor,"自定义表格",Qt.LeftDockWidgetArea)
        widget2,area2 = self.create_dock(Main_Monitor,"自定义表格",Qt.RightDockWidgetArea)df

    def init_enum(self):
        pass


    def create_dock(self,widget_class:QWidget,name:str,area:int):dsaf
        widget = widget_class(self.event_engine)
        dock = QDockWidget(name)
        dock.setWidget(widget)
        dock.setObjectName(name)
        self.addDockWidget(area,dock)
        return widget,dock

    def closeEvent(self, a0: QCloseEvent) -> None:
        reply = QMessageBox.question(self,'退出',"确认退出？",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.event_engine.exit()
            a0.accept()
        else:
            a0.ignore()


app = QApplication([])
test = Main_Window(EventEngine())
test.showMaximized()
sys.exit(app.exec_())
