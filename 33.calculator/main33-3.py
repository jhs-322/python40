import os, sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

os.chdir(os.path.dirname(os.path.abspath(__file__)))
ui_path = 'calculator.ui'
form_class = uic.loadUiType(ui_path) #loadUiType ->Qt에서 class

class WindowClass(QMainWindow, form_class): #상속
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        buttons = [
        self.btn_C, self.btn_number0, self.btn_number1, self.btn_number2, self.btn_number3,
        self.btn_number4, self.btn_number5, self.btn_number6, self.btn_number7, self.btn_number8, 
        self.btn_number9, self.btn_result, self.btn_minus, self.btn_add, self.btn_multipy, self.btn_divide]

        for button in buttons:
            button.clicked.connect(self.btn_clicked)

        # self.btn_C.clicked.connect(self.btn_clicked())
        # self.btn_number0.clicked.connect(self.btn_clicked())
        # self.btn_number1.clicked.connect(self.btn_clicked())
        # self.btn_number2.clicked.connect(self.btn_clicked)
        # self.btn_number3.clicked.connect(self.btn_clicked)
        # self.btn_number4.clicked.connect(self.btn_clicked)
        # self.btn_number5.clicked.connect(self.btn_clicked)
        # self.btn_number6.clicked.connect(self.btn_clicked)
        # self.btn_number7.clicked.connect(self.btn_clicked)
        # self.btn_number8.clicked.connect(self.btn_clicked)
        # self.btn_number9.clicked.connect(self.btn_clicked)
        # self.btn_result.clicked.connect(self.btn_clicked)
        # self.btn_minus.clicked.connect(self.btn_clicked)
        # self.btn_add.clicked.connect(self.btn_clicked)
        # self.btn_multipy.clicked.connect(self.btn_clicked)
        # self.btn_divide.clicked.connect(self.btn_clicked)

        
        self.le_view.setEnabled(False) # 사용자 직접입력 x
        self.text_value = "" # 초기화
    
    
    def btn_clicked(self): 
        btn_value = self.sender().text()
        if btn_value == 'C':
            print("clear")
            self.le_view.setText("0")
        elif btn_value == '=':
            print("=")
            
            try:
                resultValue = eval(self.text_value.lstrip("0"))
                self.le_view.setText(str(resultValue))
            except:
                self.le_view.setText("error")
        else:
            if btn_value == 'x':
                btn_value = '*'
                self.text_value = self.text_value + btn_value
                print(self.text_value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
