# Importa el módulo sys que permite interactuar con el sistema (por  cerrar la aplicación correctamente)
import sys


#Importa la librería math para usar funciones matematicas como seno, coseno, logaritmos, etc.
import math


#Importa los componentes de interfaz gráfica de PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit




# se define una clase llamada CalculadoraCientifica que hereda
# de Qwidget
#QWidget es la clase base de cualquier ventana en PyQt
class CalculadoraCientifica(QWidget):
   
    #constructor de la clase
    def __init__(self):
        #llama al constructor de la clase padre QWidget
        super().__init__()
       
        #Llama al método que construye toda la interfaz gráfica
        self.initUI()
       
    #Metodo que crea la interfaz gráfica
    def initUI(self):
           
        #Define el título de la ventana
        self.setWindowTitle("Calculadora cientifica POO")
       
        # Define la posición y tamaño de la ventana (x, y, ancho, alto)
        self.setGeometry(300, 300, 400, 400)
       
        # Se crea un layout tipo grilla (tabla)
        self.layout = QGridLayout()
       
        #Se crea el campo donde se mostrarán los numeros y resultados
        self.display = QLineEdit()
       
        #Permite que el usuario también pueda escribir manualmente
        self.display.setReadOnly(False)
       
        #Agrega el display al layout
        # (fila 0, columna 0, ocupa 1 fila y 5 columnas)
        self.layout.addWidget(self.display, 0, 0, 1, 5)
       
        #Lista con todos los botones que tendrá la calculadora
        botones = [
            '7', '8', '9', '/', 'sqrt',
            '4', '5', '6', '*','^',
            '1', '2', '3', '-', 'log',
            '0', '.', '=', '+', 'sin',
            'cos', 'tan', 'C'
        ]
       
        #Variable que indica la fila donde se colocará cada botón
        fila = 1
       
        #Variable que indica la columna
        col = 0
       
       
        # Recorre la lista de botones
        for boton in botones:
           
            # Crea un botón con el texto del elemento de la lista
            btn = QPushButton(boton)
           
            # Conecta el botón al metodo click_boton cuando sea presionado
            btn.clicked.connect(self.click_boton)
           
            #Agrega el botón al layout en la fila y columna correspondiente
            self.layout.addWidget(btn, fila, col)
           
            #Avanza una columna
            col += 1
           
            #Si se superan las 5 columnas se pasa a la siguiente fila
            if col > 4:
                col = 0
                fila += 1
           
        #Se asigna el layout a la ventana
        self.setLayout(self.layout)
       
    #Método que se ejecuta cada vez que se presiona un botón
    def click_boton(self):
       
        #Obtiene el texto del botón que fue presionado
        boton = self.sender().text()
       
        #Si el boton presionado es C
        if boton == "C":
           
            #Limpia el display
            self.display.clear()
           
        # Si el botón presionado es "="
        elif boton == "=":
            try:
               
                #Obtiene la expresion escrita en el display
                expresion =self.display.text()
               
                # Reemplaza el simbolo ^ por ** para que python entienda
                expresion = expresion.replace("^", "**")
               
                #Evalúa la expresion matematica
                resultado = eval(expresion)
               
                #Muestra el resultado en el display
                self.display.setText(str(resultado))
               
            # Si ocurre un error muestra "Error"
            except:
                self.display.setText("Error")
       
        # Si se presiona el botón de raíz  cuadrada
        elif boton == "sqrt":
            try:
               
                #Convierte el valor del display a numero
                valor = float(self.display.text())
               
                # Calcula la raíz cuadrada
                self.display.setText(str(math.sqrt(valor)))
           
            except:
                self.display.setText("Error")
               
        #Si se presiona el boton log    
        elif boton == "log":
            try:
               
                #Convierte el valor a número
                valor = float(self.display.text())
               
                # Calcula el algoritmo base 10
                self.display.setText(str(math.log10(valor)))
               
            except:
                self.display.setText("Error")
               
        # Si se presiona el botón seno
        elif boton == "sin":
            try:
               
                #Convierte el valor del display a número
                valor = float(self.display.text())

                #Convierte grados a radianes y calcula el seno
                self.display.setText(str(math.sin(math.radians(valor))))

            except:
                self.display.setText("Error")

            
        #Si se presiona el boton coseno
        elif boton == "cos":

            try:

                #Convierte el valor a número 
                valor = float(self.display.text())
                self.display.setText(str(math.cos(math.radians(valor))))


            except:
                self.display.setText("Error")
    
        #Si se presiona el botón tangente 
        elif boton ==  "tan":
            try: 
                
                #Convierte el valor a número 
                valor = float(self.display.text())

                #Calcula la tangente
                self.display.setText(str(math.tan(math.radians(valor))))

            except:
                self.display.setText("Error")   


  
            
        #Si no es ningún botón especial
        else:

            #Agrega el texto del boton al display
            self.display.setText(self.display.text() + boton)
    

# Punto de inicio del programa 
if __name__ == "__main__":
     
    #Crea la app PyQt
    app = QApplication(sys.argv)

    # Crea una instancia de la ventana de la calculadora 
    ventana = CalculadoraCientifica()

    #Muestra la ventana 
    ventana.show()

    # Ejecuta el loop principal de la app
    sys.exit(app.exec_())


                