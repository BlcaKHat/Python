#simple pyqt code with one quit button....
import sys
from PyQt4 import QtGui, QtCore

class window(QtGui.QMainWindow):
	def __init__(self):
		super(window,self).__init__()
		self.setGeometry(50,50,500,300)
		self.setWindowTitle("PyQt !!")
		self.setWindowIcon(QtGui.QIcon('err1.png'))
		print("Hey !!!")

		extractAction = QtGui.QAction("&comm onnn",self)
		extractAction.setShortcut("Q")
		extractAction.setStatusTip('leavee the app')
		extractAction.triggered.connect(self.close_application)

		self.statusBar()

		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(extractAction)


		self.home()

	def home(self):
		btn = QtGui.QPushButton("quit",self)
		btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		btn.resize(btn.sizeHint())
		btn.move(100,100)
		self.show()

	def close_application(close):
		sys.exit()
		
def run():
	app=QtGui.QApplication(sys.argv)
	GUI=window()
	sys.exit(app.exec_())

run()
