class Recorrido:

    def __init__(self,coordenadas):
        self.recorrido_x = []
        self.recorrido_y = []
        self.recorrido_x.append(coordenadas.x)
        self.recorrido_y.append(coordenadas.y)


    def agregarParada(self,coordenadas):
        """Agrega las coordenadas actuales del borracho.
        Sirve para llevar un registro de los puntos por los que el borracho ha caminado
        """
        #print('Agrego nuevo punto',self.coordenadas.x,self.coordenadas.y)
        self.recorrido_x.append(coordenadas.x) #Agrega la coordenada de X
        self.recorrido_y.append(coordenadas.y) #Agrega la coordenada de Y
