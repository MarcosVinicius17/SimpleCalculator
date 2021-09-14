from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys, math


class Button():
    def __init__(self,text, results):
        self.b = QPushButton(str(text))
        self.text = text

        #To grab the text in the QLineEdit
        self.results = results
        self.b.clicked.connect(lambda:self.handleInput(self.text))

    def handleInput(self,btn_pressed):
        if btn_pressed == "=":
            resu = eval(self.results.text())
            self.results.setText(str(resu))
        elif btn_pressed =="AC":
            self.results.setText("")
        elif btn_pressed =="√":
            value = float(self.results.text())
            self.results.setText(str(math.sqrt(value)))
        elif btn_pressed =="DEL":
            current_value = self.results.text()
            self.results.setText(current_value[:-1])
        else:
             current_value = self.results.text()
             new_value = current_value + str(btn_pressed)
             self.results.setText(new_value)




class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.createApp()
        


    def createApp(self):
        grid = QGridLayout()
        results = QLineEdit()

        #This list contain all buttons in the calculator
        buttons = ["AC","√","DEL","/",7,8,9,"*",4,5,6,"-",1,2,3,"+",0,".","="]

        grid.addWidget(results,0,0,1,4)
        
        row = 1
        column = 0

        #Add all the buttons. When arrives the 4th column, jump to the next line.
        for button in buttons:
            if column > 3:
                column = 0
                row += 1
            buttonObject = Button(button,results)

            #Makes the zero button occupy two colums
            if button == 0:
                grid.addWidget(buttonObject.b, row, column, 1,2)
                column += 1
            else:
                grid.addWidget(buttonObject.b, row, column, 1,1)
            column += 1


        self.setLayout(grid)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec_())