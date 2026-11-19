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
        
        #Separar las palabras
        textoSeparado = texto.split()
        print(textoSeparado)
        
        print("Se ha presionado el boton")
        
        #contar palabras
        cantidadPalabras = len(textoSeparado)
        self.tvPalabras.setText(f"Palabras: {cantidadPalabras}")     
        
        #contar caracteres   
        totalC = 0
        for palabra in textoSeparado:
            totalC += len (palabra)
        totalC
        self.totalCarc.setText(f"Caracteres: {totalC}")     
        
        "font: 12p"
        #aqui la logica
        if cantidadPalabras >=50:
            self.tvPalabras("color: #ff756b")
        else:
            self.tvPalabras.setStyleSheet("color: #000000")
        if cantidadPalabras >=50:
            self.tvCaracteres("color: #ff756b")
        else:
            self.tvCaracteres.setStyleSheet("color: #000000")
      
        
app = QtWidgets.QApplication(sys.argv)
ventana = ContadorPalabras ()
ventana.show()
sys.exit(app.exec())