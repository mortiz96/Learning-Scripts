from borracho import Borracho 
from coordenada import Coordenada
from recorrido import Recorrido
from bokeh.plotting import figure
from bokeh.io import show, output_file
import random

def main(pasos, borrachos ):

    dicc = {}
    for cant_p in pasos:
        dicc[cant_p] = realizar_recorridos(cant_p, borrachos)
    
    return dicc     

def realizar_recorridos(cant_p, borrachos):

    recorridos = []
    for _ in range(borrachos):
        inicio =  Coordenada(0, 0)
        borracho = Borracho('Eduardo', inicio)

        recorrido = caminar(borracho, cant_p)
        recorridos.append(recorrido)

    return recorridos    

def caminar(borracho, cant_p):
    for _ in range(cant_p):#_ Significa que itere esa cantidad de veces sin asignar a un indice
        borracho.dar_paso()        
    return borracho.recorrido


def graficar(dicc, borrachos):


    """Grafica todos los casos dentro de un diccionario.

        Obs. El diccionario tiene como llave una cantidad de pasos ej. 10, 100, 1000
        > Cada cantidad de pasos es un caso de 'experimentacion'
        > Cada caso tiene dentro de si una cantidad n de recorridos 
            (obviamente, cada recorrido con esa cantidad de pasos)
        > Cada recorrido se compone de dos listados, uno en recorrido_x y un recorrido_y
            El recorrido_x guarda las coordenadas en x de los puntos visitados en el recorrido
            El recorrido_y hace lo mismo pero con y
    """

    colors = []
#Este for genera n cantidad de colores dependiendo de la n cantidad de borrachos
    for i in range(borrachos):
        colors.append('#%06X' % random.randint(0, 0xFFFFFF))


    output_file('graficado_borrachos.html')
    for caso in dicc.items():
        fig = figure(title=str(f'Camino aleatorio con {caso[0]} pasos '), x_axis_label='X', y_axis_label='Y')
        
        i = 0
        print(f'CASO:{caso[0]} pasos')
        for recorrido in caso[1]:

            #print('Recorrido x',recorrido.recorrido_x)
            #print('Recorrido y',recorrido.recorrido_y)
            #print('COLORES:',colors)

            puntos_x = recorrido.recorrido_x
            puntos_y = recorrido.recorrido_y
             
            fig.line(puntos_x, puntos_y, legend_label=str(f'Borracho {i}'), line_color=colors[i] )

            fig.scatter(puntos_x[len(puntos_x)-1],puntos_y[len(puntos_y)-1], marker='diamond', size=10, fill_color='red' )
            
            i += 1
        fig.scatter(0, 0, marker='circle', size=10, fill_color='yellow', legend_label='Inicio' )

        show(fig)




if __name__ == '__main__':
    pasos = [3000]#, 10]
    borrachos =  5
    dicc = main(pasos, borrachos)
    graficar(dicc,borrachos)