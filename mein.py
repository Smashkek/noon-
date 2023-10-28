import random
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.example)
    def example(self):
        siqns = ''
        if self.ui.checkBox.isChecked():
            signs = 'qwertyuiopsdfghjklzxcvbnm'
        if self.ui.checkBox_2.isChecked():
            signs += '0123456789'
        result = ''
        number = random.randint(5, 10)
        for i in range(number):
            result += random.choice(siqns)
        self.ui.label_2.setText(result)
app - QApplication[]
ex = Widget()
ex.show()
app.exec_()
