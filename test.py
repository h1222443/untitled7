from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator, QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import *
import sys


class QLineEditValidator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("文本输入框的校验器")
        # 实例化表单布局
        formLayout = QFormLayout()

        # 创建三个文本输入框
        ipLineEdit = QLineEdit()
        portLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()

        # 实例化整型校验器，并设置范围0~65536
        portValidator = QIntValidator(0, 65536)
        # 设置 正则表达式，显示输入0.0.0.0~255.255.255.255
        regExp = QRegExp('^((2[0-4]\d|25[0-5]|\d?\d|1\d{2})\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)$')
        # 实例化自定义校验器
        ipValidator = QRegExpValidator(regExp)
        # 实例化浮点校验器，并设置范围-360~360，精度为小数点两位
        doubleValidator = QDoubleValidator(-360, 360, 2)
        doubleValidator.setBottom(0)

        # 为文本输入框设置对应的校验器
        ipLineEdit.setValidator(ipValidator)
        portLineEdit.setValidator(portValidator)
        doubleLineEdit.setValidator(doubleValidator)

        # 文本输入框添加到表单布局上
        formLayout.addRow("IP", ipLineEdit)
        formLayout.addRow("Port", portLineEdit)
        formLayout.addRow("Double", doubleLineEdit)

        self.setLayout(formLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditValidator()
    main.show()
    sys.exit(app.exec_())