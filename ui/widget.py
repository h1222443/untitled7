from typing import Dict,Any,List
from ..event import Event,EventEngine
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem,QMenu,QAction
from PyQt5.QtCore import Qt,pyqtSignal
from PyQt5.QtGui import QContextMenuEvent,QCursor

class BaseCell(QTableWidgetItem):
    def __init__(self,content,data):
        super().__init__()
        self.setTextAlignment(Qt.AlignCenter)
        self.set_content(content,data)

    def set_content(self,content,data):
        self.setText(str(content))
        self.data = data

    def get_data(self):
        return self.data


class BasicMonitor(QTableWidget):
    event_type : str = ""
    data_key : str = ""
    sorting : bool = False
    headers : Dict[str,dict] = {}
    signal : pyqtSignal(Event)

    def __init__(self,event_engine:EventEngine):
        super().__init__()
        self.event_engine :EventEngine = EventEngine
        self.cells : Dict[str,dict] = {}
        self.initUI()
        self.register_event()

    def initUI(self):
        self.init_table()
        self.init_menu()

    def init_table(self):

        self.setColumnCount(len(self.headers))
        labels = [d['display'] for d in self.headers.values()]
        self.setHorizontalHeaderLabels(labels)
        self.verticalHeader().setVisible(False)

        self.setEditTriggers(self.NoEditTriggers)
        self.setAlternatingRowColors(True)
        self.setSortingEnabled(self.sorting)

    def init_menu(self):
        self.menu = QMenu(self)
        resize_action = QAction('调整列宽',self)
        resize_action.triggered.connect(self.resize_columns)
        self.menu.addAction(resize_action)

        save_action = QAction('保存数据',self)
        save_action.triggered.connect(self.save_csv)
        self.menu.addAction(save_action)

    def register_event(self):
        if self.event_type:
            self.signal.connect(self.process_event)
            self.event_engine.register(self.event_type,self.signal.emit)

    def process_event(self,event):
        if self.sorting:
            self.setSortingEnabled(False)
        data = event.data

        if not self.data_key:
            self.insert_new_row(data)
        else:
            key = data.__getattribute__(self.data_key)
            if key in self.cells:
                self.update_old_row(data)
            else:
                self.insert_new_row(data)
        if self.sorting:
            self.setSortingEnabled(True)


    def insert_new_row(self,data):
        self.insertRow(0)
        row_cell = {}
        for column,header in enumerate(self.headers.keys()):
            setting = self.headers[header]

            content = data.__getattribute__(header)
            cell = setting['cell'](content,data)
            self.setItem(0,column,cell)

            if setting['update']:
                row_cell[header] = cell

        if self.data_key:
            key = data.__getattribute__(self.data_key)
            self.cells[key] = row_cell

    def update_old_row(self,data):
        key = data.__getattribute__(self.data_key)
        row_cell = self.cells[key]

        for header,cell in row_cell.items():
            content = data.__getattribute__(header)
            cell.set_content(content,data)

    def resize_action(self):
        pass
    def save_csv(self):
        pass
    def contextMenuEvent(self, event: QContextMenuEvent) -> None:

        self.menu.popup(QCursor.pos())