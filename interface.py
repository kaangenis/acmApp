# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(597, 825)
        MainWindow.setStyleSheet("font: 30pt \"MS Shell Dlg 2\";")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 271, 51))
        self.label.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 271, 31))
        self.label_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.linePost = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.linePost.setGeometry(QtCore.QRect(10, 130, 551, 31))
        self.linePost.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.linePost.setObjectName("linePost")
        self.textAll = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textAll.setGeometry(QtCore.QRect(20, 230, 256, 391))
        self.textAll.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.textAll.setObjectName("textAll")
        self.textWinners = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textWinners.setGeometry(QtCore.QRect(310, 230, 261, 391))
        self.textWinners.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.textWinners.setObjectName("textWinners")
        self.btnScraper = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnScraper.setGeometry(QtCore.QRect(20, 630, 261, 51))
        self.btnScraper.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.btnScraper.setObjectName("btnScraper")
        self.btnRandom = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnRandom.setGeometry(QtCore.QRect(310, 630, 261, 51))
        self.btnRandom.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.btnRandom.setObjectName("btnRandom")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 201, 31))
        self.label_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 190, 201, 31))
        self.label_4.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.btnClear = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(20, 690, 261, 51))
        self.btnClear.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.btnClear.setObjectName("btnClear")
        self.btnQuit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnQuit.setGeometry(QtCore.QRect(310, 690, 261, 51))
        self.btnQuit.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.btnQuit.setObjectName("btnQuit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ACM"))
        self.label.setText(_translate("MainWindow", "ACM Draw App"))
        self.label_2.setText(_translate("MainWindow", "Instagram Post Linki :"))
        self.btnScraper.setText(_translate("MainWindow", "Yorumları Al"))
        self.btnRandom.setText(_translate("MainWindow", "Kazananları Belirle"))
        self.label_3.setText(_translate("MainWindow", "Tüm Katılımcılar:"))
        self.label_4.setText(_translate("MainWindow", "Kazananlar:"))
        self.btnClear.setText(_translate("MainWindow", "Sıfırla"))
        self.btnQuit.setText(_translate("MainWindow", "Çıkış"))