import sys
from PyQt5 import QtWidgets,uic

class ContadorPalabras (QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        #Carga de nuestra ventana
        uic.loadUi("contadorPalabras.ui",self)
        self.btContar.clicked.connect(self.ContarPalabras)
        
    def ContarPalabras (self):
        #Recuperar el texto
        texto = self.edtCaracteres.text()
        print(texto)
        
        textoSeparado = texto.split()
        print(textoSeparado)
        
        print("Se ha presionado el boton")
        
app = QtWidgets.QApplication(sys.argv)
ventana = ContadorPalabras ()
ventana.show()
sys.exit(app.exec())