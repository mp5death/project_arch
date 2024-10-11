import sys
from PyQt5.QtWidgets import QApplication, QWidget


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from view.test import Ui_MainWindow  # Importamos la clase desde interfaz.py

def abrir_ventana():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()  # Creamos una ventana principal
    ui = Ui_MainWindow()  # Instanciamos la clase que tiene la interfaz
    ui.setupUi(MainWindow)  # Configuramos la UI en la ventana principal
    MainWindow.show()  # Mostramos la ventana
    sys.exit(app.exec_())  # Iniciamos el bucle de eventos

if __name__ == '__main__':
    abrir_ventana()