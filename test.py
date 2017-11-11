import sys
from PyQt4 import QtGui


class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        self.statusBar().showMessage('achievement')
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('im abt to die rn')    
        self.show()


def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

main()
