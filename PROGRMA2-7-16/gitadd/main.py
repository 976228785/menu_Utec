#!/usr/bin/python
# -*- coding: utf-8 -*-


from PyQt4 import QtGui  # Import the PyQt4 module we'll need
from PyQt4 import QtCore
import sys  # We need sys so that we can pass argv to QApplication

import primerapantalla #Esto se genera de esto: primerapantalla.ui
import segundapantalla #Esto se genera de esto: segundapantalla.ui
import tercerapantalla
import tercerapantalla1
import tercerapantalla2
import platosalacarta
import platosalacarta1
import platosalacarta2
import platosalacarta3
import platosalacarta4
import platosalacarta5
import platosalacarta6
import panes
import panes1
import panes2
import panes3
import panes4
import panes5
import panes6
import panes7
class MainWindow(QtGui.QMainWindow, primerapantalla.Ui_PrimeraWindow):
    def __init__(self):

        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.btnMenu.clicked.connect(self.btnMenuClicked)
        self.btnPlatoslacarta.clicked.connect(self.btnPlatosalacartaClicked)
        self.btnSandwiches.clicked.connect(self.btnSandwichesClicked)
        self.secondW = None
        self.thirdW = None
        self.fourW = None

    def btnMenuClicked(self):
        if self.secondW is None:
            self.secondW = SecondWindow(self)
        self.secondW.show()

    def btnPlatosalacartaClicked(self):
    	if self.thirdW is None:
    		self.thirdW = ThirdWindow(self)
    	self.thirdW.show()

    def btnSandwichesClicked(self):
        if self.fourW is None:
            self.fourW = FourWindow(self)
        self.fourW.show()

class SecondWindow(QtGui.QMainWindow, segundapantalla.Ui_segundaWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.btnIzquierda2.clicked.connect(self.btnIzquierda2Clicked)
        self.btnEconomico2.clicked.connect(self.btnEconomico2Clicked)
        self.bntEstudiantil2.clicked.connect(self.btnEstudiantil2Clicked)
        self.btnMenu2.clicked.connect(self.btnMenu2Clicked)
        self.btnEjecutivo2.clicked.connect(self.btnEjecutivo2Clicked)
        self.sevenW = None
        self.sixW = None
        self.fiveW = None

    def btnEconomico2Clicked(self):
        if self.sevenW is None:
            self.sevenW = SevenWindow(self)
        self.sevenW.show()

    def btnEstudiantil2Clicked(self):
        if self.sixW is None:
            self.sixW = SixWindow(self)
        self.sixW.show()

    def btnEjecutivo2Clicked(self):
        if self.fiveW is None:
            self.fiveW = FiveWindow(self)
        self.fiveW.show()

    def btnIzquierda2Clicked(self):
        self.close()

    def btnMenu2Clicked(self):
        self.close()


class ThirdWindow(QtGui.QMainWindow, platosalacarta.Ui_pcWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.btnIzquierda4.clicked.connect(self.btnIzquierda4Clicked)
        self.btnPlatosalacarta0.clicked.connect(self.btnPlatosalacarta0Clicked)
        self.btnLomosaltado0.clicked.connect(self.btnLomosaltado0Clicked)
        self.btnPollosaltado0.clicked.connect(self.btnPollosaltado0Clicked)
        self.btnAlfredo0.clicked.connect(self.btnAlfredo0Clicked)
        self.btnTallarin0.clicked.connect(self.btnTallarin0Clicked)
        self.btnChifa0.clicked.connect(self.btnChifa0Clicked)
        self.btnCubana0.clicked.connect(self.btnCubana0Clicked)
        self.tenW = None
        self.elevenW = None
        self.twelveW = None
        self.thirteenW = None
        self.fourteenW = None
        self.fifteenW = None

    def btnIzquierda4Clicked(self):
        self.close()

    def btnPlatosalacarta0Clicked(self):
        self.close()

    def btnLomosaltado0Clicked(self):
        if self.tenW is None:
            self.tenW = TenWindow(self)
        self.tenW.show()

    def btnPollosaltado0Clicked(self):
        if self.elevenW is None:
            self.elevenW = ElevenWindow(self)
        self.elevenW.show()

    def btnAlfredo0Clicked(self):
        if self.twelveW is None:
            self.twelveW = TwelveWindow(self)
        self.twelveW.show()

    def btnTallarin0Clicked(self):
        if self.thirteenW is None:
            self.thirteenW = ThirteenWindow(self)
        self.thirteenW.show()

    def btnChifa0Clicked(self):
        if self.fourteenW is None:
            self.fourteenW = FourteenWindow(self)
        self.fourteenW.show()

    def btnCubana0Clicked(self):
        if self.fifteenW is None:
            self.fifteenW = FifteenWindow(self)
        self.fifteenW.show()


class FourWindow(QtGui.QMainWindow, panes.Ui_panesWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.btnIzquierda5.clicked.connect(self.btnIzquierda5Clicked)
        self.btnPanes0.clicked.connect(self.btnPanes0Clicked)
        self.btnMixto0.clicked.connect(self.btnMixto0Clicked)
        self.btnHamburguesa0.clicked.connect(self.btnHamburguesa0Clicked)
        self.btnPan0.clicked.connect(self.btnPan0Clicked)
        self.btnFilete0.clicked.connect(self.btnFilete0Clicked)
        self.btnChorizo0.clicked.connect(self.btnChorizo0Clicked)
        self.btnCroissant0.clicked.connect(self.btnCroissant0Clicked)
        self.btnTriple0.clicked.connect(self.btnTriple0Clicked)
        self.sixteenW = None
        self.seventeenW = None
        self.eighteenW = None
        self.nineteenW = None
        self.twentyW = None
        self.twentyoneW = None
        self.twentytwoW = None


    def btnIzquierda5Clicked(self):
        self.close()

    def btnPanes0Clicked(self):
        self.close()

    def btnMixto0Clicked(self):
        if self.sixteenW is None:
            self.sixteenW = SixteenWindow(self)
        self.sixteenW.show()

    def btnHamburguesa0Clicked(self):
        if self.seventeenW is None:
            self.seventeenW = SeventeenWindow(self)
        self.seventeenW.show()

    def btnPan0Clicked(self):
        if self.eighteenW is None:
            self.eighteenW = EighteenWindow(self)
        self.eighteenW.show()

    def btnFilete0Clicked(self):
        if self.nineteenW is None:
            self.nineteenW = NineteenWindow(self)
        self.nineteenW.show()

    def btnChorizo0Clicked(self):
        if self.twentyW is None:
            self.twentyW = TwentyWindow(self)
        self.twentyW.show()

    def btnCroissant0Clicked(self):
        if self.twentyoneW is None:
            self.twentyoneW = TwentyoneWindow(self)
        self.twentyoneW.show()

    def btnTriple0Clicked(self):
        if self.twentytwoW is None:
            self.twentytwoW = TwentytwoWindow(self)
        self.twentytwoW.show()



class SevenWindow(QtGui.QMainWindow, tercerapantalla.Ui_terceraWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.btnIzquierda3.clicked.connect(self.btnIzquierda3Clicked)
        self.btnMenu3.clicked.connect(self.btnMenu3Clicked)
        self.btnPedido3.clicked.connect(self.btnPedido3Clicked)

    def btnPedido3Clicked(self):
        self.close()

    def btnIzquierda3Clicked(self):
        self.close()

    def btnMenu3Clicked(self):
        self.close()

        
class SixWindow(QtGui.QMainWindow, tercerapantalla1.Ui_tercera1Window):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.btnIzquierda31.clicked.connect(self.btnIzquierda31Clicked)
        self.btnMenu31.clicked.connect(self.btnMenu31Clicked)
        self.btnPedido31_.clicked.connect(self.btnPedido31Clicked)

    def btnPedido31Clicked(self):
        self.close()

    def btnIzquierda31Clicked(self):
        self.close()

    def btnMenu31Clicked(self):
        self.close()

        
class FiveWindow(QtGui.QMainWindow, tercerapantalla2.Ui_tercera2Window):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.btnIzquierda32.clicked.connect(self.btnIzquierda32Clicked)
        self.btnMenu32.clicked.connect(self.btnMenu32Clicked)
        self.btnPedido32.clicked.connect(self.btnPedido32Clicked)

    def btnPedido32Clicked(self):
        self.close()

    def btnIzquierda32Clicked(self):
        self.close()

    def btnMenu32Clicked(self):
        self.close()


class TenWindow(QtGui.QMainWindow, platosalacarta1.Ui_pc1Window):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.btnIzquierda41.clicked.connect(self.btnIzquierda41Clicked)
        self.btnPlatosalacarta1.clicked.connect(self.btnPlatosalacarta1Clicked)
        self.btnPedido41.clicked.connect(self.btnPedido41Clicked)

    def btnPedido41Clicked(self):
        self.close()

    def btnIzquierda41Clicked(self):
        self.close()

    def btnPlatosalacarta1Clicked(self):
        self.close()

class ElevenWindow(QtGui.QMainWindow, platosalacarta2.Ui_pc2Window):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.btnIzquierda42.clicked.connect(self.btnIzquierda42Clicked)
        self.btnPlatosalacarta2.clicked.connect(self.btnPlatosalacarta2Clicked)
        self.btnPedido42.clicked.connect(self.btnPedido42Clicked)

    def btnPedido42Clicked(self):
        self.close()

    def btnIzquierda42Clicked(self):
        self.close()

    def btnPlatosalacarta2Clicked(self):
        self.close()

class TwelveWindow(QtGui.QMainWindow, platosalacarta3.Ui_pc3Window):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.btnIzquierda43.clicked.connect(self.btnIzquierda43Clicked)
        self.btnPlatosalacarta3.clicked.connect(self.btnPlatosalacarta3Clicked)
        self.btnPedido43.clicked.connect(self.btnPedido43Clicked)

    def btnPedido43Clicked(self):
        self.close()

    def btnIzquierda43Clicked(self):
        self.close()

    def btnPlatosalacarta3Clicked(self):
        self.close()

class ThirteenWindow(QtGui.QMainWindow, platosalacarta4.Ui_pc4Window):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.btnIzquierda44.clicked.connect(self.btnIzquierda44Clicked)
        self.btnPlatosalacarta4.clicked.connect(self.btnPlatosalacarta4Clicked)
        self.btnPedido44.clicked.connect(self.btnPedido44Clicked)

    def btnPedido44Clicked(self):
        self.close()

    def btnIzquierda44Clicked(self):
        self.close()

    def btnPlatosalacarta4Clicked(self):
        self.close()

class FourteenWindow(QtGui.QMainWindow, platosalacarta5.Ui_pc5Window):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.btnIzquierda45.clicked.connect(self.btnIzquierda45Clicked)
        self.btnPlatosalacarta5.clicked.connect(self.btnPlatosalacarta5Clicked)
        self.btnPedido45.clicked.connect(self.btnPedido45Clicked)

    def btnPedido45Clicked(self):
        self.close()

    def btnIzquierda45Clicked(self):
        self.close()

    def btnPlatosalacarta5Clicked(self):
        self.close()


class FifteenWindow(QtGui.QMainWindow, platosalacarta6.Ui_pc6Window):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.btnIzquierda46.clicked.connect(self.btnIzquierda46Clicked)
        self.btnPlatosalacarta6.clicked.connect(self.btnPlatosalacarta6Clicked)
        self.btnPedido46.clicked.connect(self.btnPedido46Clicked)

    def btnPedido46Clicked(self):
        self.close()

    def btnIzquierda46Clicked(self):
        self.close()

    def btnPlatosalacarta6Clicked(self):
        self.close()


class SixteenWindow(QtGui.QMainWindow, panes1.Ui_panes1Window):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.btnIzquierda51.clicked.connect(self.btnIzquierda51Clicked)
        self.btnPanes1.clicked.connect(self.btnPanes1Clicked)
        self.btnPedido51.clicked.connect(self.btnPedido51Clicked)

    def btnPedido51Clicked(self):
        self.close()

    def btnIzquierda51Clicked(self):
        self.close()

    def btnPanes1Clicked(self):
        self.close()


class SeventeenWindow(QtGui.QMainWindow, panes2.Ui_panes2Window):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.btnIzquierda52.clicked.connect(self.btnIzquierda52Clicked)
        self.btnPanes2.clicked.connect(self.btnPanes2Clicked)
        self.btnPedido52.clicked.connect(self.btnPedido52Clicked)

    def btnPedido52Clicked(self):
        self.close()

    def btnIzquierda52Clicked(self):
        self.close()

    def btnPanes2Clicked(self):
        self.close()


class EighteenWindow(QtGui.QMainWindow, panes3.Ui_panes3Window):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.btnIzquierda53.clicked.connect(self.btnIzquierda53Clicked)
        self.btnPanes3.clicked.connect(self.btnPanes3Clicked)
        self.btnPedido53.clicked.connect(self.btnPedido53Clicked)

    def btnPedido53Clicked(self):
        self.close()

    def btnIzquierda53Clicked(self):
        self.close()

    def btnPanes3Clicked(self):
        self.close()


class NineteenWindow(QtGui.QMainWindow, panes4.Ui_panes4Window):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.btnIzquierda54.clicked.connect(self.btnIzquierda54Clicked)
        self.btnPanes4.clicked.connect(self.btnPanes4Clicked)
        self.btnPedido54.clicked.connect(self.btnPedido54Clicked)

    def btnPedido54Clicked(self):
        self.close()

    def btnIzquierda54Clicked(self):
        self.close()

    def btnPanes4Clicked(self):
        self.close()


class TwentyWindow(QtGui.QMainWindow, panes5.Ui_panes5Window):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.btnIzquierda55.clicked.connect(self.btnIzquierda55Clicked)
        self.btnPanes5.clicked.connect(self.btnPanes5Clicked)
        self.btnPedido55.clicked.connect(self.btnPedido55Clicked)

    def btnPedido55Clicked(self):
        self.close()

    def btnIzquierda55Clicked(self):
        self.close()

    def btnPanes5Clicked(self):
        self.close()


class TwentyoneWindow(QtGui.QMainWindow, panes6.Ui_panes6Window):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.btnIzquierda56.clicked.connect(self.btnIzquierda56Clicked)
        self.btnPanes6.clicked.connect(self.btnPanes6Clicked)
        self.btnPedido56.clicked.connect(self.btnPedido56Clicked)

    def btnPedido56Clicked(self):
        self.close()

    def btnIzquierda56Clicked(self):
        self.close()

    def btnPanes6Clicked(self):
        self.close()



class TwentytwoWindow(QtGui.QMainWindow, panes7.Ui_panes7Window):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.btnIzquierda57.clicked.connect(self.btnIzquierda57Clicked)
        self.btnPanes7.clicked.connect(self.btnPanes7Clicked)
        self.btnPedido57.clicked.connect(self.btnPedido57Clicked)

    def btnPedido57Clicked(self):
        self.close()

    def btnIzquierda57Clicked(self):
        self.close()

    def btnPanes7Clicked(self):
        self.close()


def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = MainWindow()  # We set the form to be our MainWindow (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function


#Convertir primerapantalla.ui a primerapantalla.py
#En el terminal: (Situado en la carpeta donde está el archivo)
#pyuic4 primerapantalla.ui -o primerapantalla.py
