#python 2.7.6
from Automata_FD import Automata
import sys
from PyQt4 import QtGui

# Clase Ventana que hereda de QtGui.QMainWindow
class Ventana (QtGui.QMainWindow):
	# Constructor de la Ventana
    def __init__(self):
        # Se ejecuta el Constructor de la clase Padre
        super(Ventana, self).__init__()
        self.setGeometry(500,150,600,500)
        # Se agrega un titulo al Grafico
        self.setWindowTitle("Automata Finito Determinista")
        # Se Agrega un Icono al Grafico
        self.setWindowIcon(QtGui.QIcon('logoturing.jpg'))
        

        # Se agrega un evento Se agrega un atajo, debe ir junto la cadena
        EventoSalir = QtGui.QAction(QtGui.QIcon("salir.png"),"salir",self)         
        EventoSalir.setShortcut("Ctrl+Q")
        EventoSalir.setStatusTip('Sali de la aplicacion')
        EventoSalir.triggered.connect(self.cierra_aplicacion)

        # Menu
        MenuPrincipal = self.menuBar()
        MenuArchivo = MenuPrincipal.addMenu('&Inicio')

         # Se agrega un listener o escuchador de evento, recibe el evento "EventoSalir"
        MenuArchivo.addAction(EventoSalir)

        # Se crea el contenifo del Grafico
        self.elem()


    def elem(self):

        # Configuracion de el Contenido

        # Declaracion de componentes
        
        self.titulo_lbl = QtGui.QLabel('Automata Finito Determinista (ADF)',self)
        self.prop_lbl = QtGui.QLabel('Proporcione una cadena para evaluar',self)
        self.ev_lbl = QtGui.QLabel('Resultado de la evaluacion',self)
        self.imagen = QtGui.QLabel(self)
        self.button = QtGui.QPushButton('Comenzar',self)
        self.entrada_texto = QtGui.QLineEdit(self)      
        self.salida_texto  = QtGui.QLineEdit(self)
        
        
        self.titulo_lbl.resize(300,30)
        self.titulo_lbl.move(220,40)

        self.prop_lbl.resize(300,30)
        self.prop_lbl.move(30,350)

        self.entrada_texto.resize(300,20)
        self.entrada_texto.move(230,355)

        self.button.resize(100,40)
        self.button.move(40,380)
        self.button.clicked.connect(self.evalua)

        self.salida_texto.resize(300,20)
        self.salida_texto.move(230,440)

        self.ev_lbl.resize(300,30)
        self.ev_lbl.move(30,440)

        self.imagen.setPixmap(QtGui.QPixmap("autom.png"))
        self.imagen.resize(600,250)
        self.imagen.move(10,80)
        

        # Hace Visible el Grafico
        self.show()

    def cierra_aplicacion(self):
        sys.exit()
    #Metodo que ejecuta el boton
    def evalua(self):
        contador = 0
        mensaje = self.entrada_texto.text()
        #Recorre la cadena del mensaje y verifica si hay puros ceros y unos, de caso contarario aumenta un contador a uno
        for m in mensaje:
            if m!="0" and m!="1":
                contador = contador+1
        
        if(contador>0 or mensaje==""):
            QtGui.QMessageBox.critical( self , "Error", "Cadena Invalida o vacia")
            self.entrada_texto.setText("")
            contador =0
        else:
            auto = Automata()
            evaluacion = auto.q0(mensaje,contador)
            if(evaluacion==0):
                self.salida_texto.setText("La cadena es aceptada")
            elif(evaluacion==1):
                self.salida_texto.setText("La cadena no es aceptada")

            
            
#Metodo main que correr la aplicacion es como si fuera otra clase 
def main():    
    app = QtGui.QApplication(sys.argv)
    GUI = Ventana()
    sys.exit(app.exec_())

# Se corre el main
main()


