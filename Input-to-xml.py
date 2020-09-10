from PyQt5 import QtCore, QtGui, QtWidgets
import xml.etree.ElementTree as xml
from datetime import datetime

jetzt = datetime.now()
datum = jetzt.strftime("%d.%m.%y")
date = str(datum)




mandant_pr_var        = ('1')
prod_variante_var     = ('1')
prod_kostenstelle_var = ('6021')
prod_datum            = (datum)
prod_auftrag_var      = ('99999')
menge_var             = ('1')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(769, 555)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(30, 170, 331, 41))
        self.lineEdit1.setObjectName("lineEdit1")
        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(30, 270, 331, 41))
        self.lineEdit2.setObjectName("lineEdit2")
        self.lineEdit3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit3.setGeometry(QtCore.QRect(30, 370, 331, 41))
        self.lineEdit3.setObjectName("lineEdit3")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(434, 332, 311, 171))
        self.pushButton1.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton1.clicked.connect(self.clickMich)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 120, 331, 41))
        self.label.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 220, 331, 41))
        self.label_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 320, 331, 41))
        self.label_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 20, 571, 71))
        self.label_4.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 769, 21))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        self.actionclose = QtWidgets.QAction(MainWindow)
        self.actionclose.setObjectName("actionclose")
        self.actionclose.setShortcut("Ctrl+Q")
        self.actionclose.setStatusTip('Leave The App')
        self.actionclose.triggered.connect(self.close_application)

        self.menufile.addAction(self.actionclose)
        self.menubar.addAction(self.menufile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "insertname_line63"))
        self.pushButton1.setText(_translate("MainWindow", "OK"))
        self.label.setText(_translate("MainWindow", "Stücklisten Nummer:"))
        self.label_2.setText(_translate("MainWindow", "MHD:"))
        self.label_3.setText(_translate("MainWindow", "Charge:"))
        self.label_4.setText(_translate("MainWindow", "insertname_line68"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.actionclose.setText(_translate("MainWindow", "close"))
        
    def close_application(self):
        print("whooaaaa so custom!!!")
        sys.exit()


    



#-----------------------------------------------------------------------------------------XML----------------------------------------------------------
    def clickMich(self):
        
        Stuecklisten_NR_var = self.lineEdit1.text()
        mhd_var = self.lineEdit2.text()
        charge_var = self.lineEdit3.text()
        
        self.lineEdit1.clear()
        self.lineEdit2.clear()
        self.lineEdit3.clear()
        
        def createXML(filename):
            
            root = xml.Element("produktion")
            children1 = xml.Element("auftrag")
            root.append(children1)

            mandant_pr = xml.SubElement(children1, "mandant_pr")
            mandant_pr.text = mandant_pr_var 

            Stuecklisten_NR =xml.SubElement(children1, "Stuecklisten_NR")        #--------------Eingabe---------------
            Stuecklisten_NR.text = Stuecklisten_NR_var

            prod_variante = xml.SubElement(children1, "prod_variante")
            prod_variante.text = prod_variante_var

            prod_kostenstelle = xml.SubElement(children1, "prod_kostenstelle")
            prod_kostenstelle.text = prod_kostenstelle_var

            prod_datum = xml.SubElement(children1, "prod_datum")         #--------------Tagesdatum---------------
            prod_datum.text = datum

            prod_auftrag = xml.SubElement(children1, "prod_auftrag")
            prod_auftrag.text = prod_auftrag_var

            mhd = xml.SubElement(children1, "mhd")          #--------------Eingabe---------------
            mhd.text = mhd_var

            charge = xml.SubElement(children1, "charge")       #--------------Eingabe---------------
            charge.text = charge_var

            menge = xml.SubElement(children1, "menge")
            menge.text = menge_var



            tree = xml.ElementTree(root)
            with open(filename, "wb") as fh:
                tree.write(fh)
        createXML("Produktion-Manuell.xml")
#--------------------------------------------------------------------------------------------------------------------------------------------------
    
    





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
