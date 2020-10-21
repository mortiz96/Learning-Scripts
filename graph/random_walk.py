from ant import fireant
from road import road
from coordinates import coord
from bokeh.plotting import figure,show 


def walk(road, ant, steps):
	start=road.get_coordinates(ant)

	for _ in range(steps):
		road.move_ant(ant)

	return start.distance(road.get_coordinates(ant))



def simulate_walk(steps, runs, ant_type):
    ant = ant_type(name='David')
    origen = coord(0, 0)
    distancias = []

    for _ in range(runs):
        road_1 = road()
        road_1.add_ant(ant, origen)
        simulacion_caminata = walk(road_1, ant, steps)
        distancias.append(round(simulacion_caminata, 1))

    return distancias


def graph(x,y):
	grafico=figure(title='Random Walk', x_axis_label='Steps', y_axis_label='distance')
	grafico.line(x,y,legend='Avg. distance')
	show(grafico)


def main(walk_distances, runs, ant_type):
    walk_distances_mean=[]
    for steps in walk_distances:
        distances=simulate_walk(steps, runs, ant_type)
        distance_avg=round(sum(distances)/len(distances),4)
        distance_max=max(distances)
        distance_min=min(distances)
        walk_distances_mean.append(distance_avg)
        print(f'{ant_type.__name__} caminata aleatoria de {steps}')
        print(f'Average={distance_avg}')
        print(f'Max={distance_max}')
        print(f'Min={distance_min}')
    graph(walk_distances, walk_distances_mean)

#****new set of functions"

def walk2(road, pasos, ant_type):

    ant1=ant_type(name='luka')
    origin=coord(0,0)
    road.add_ant(ant1,origin)

    x_val=[]
    y_val=[]

    for _ in range(pasos):
        road.move_ant(ant1)
        x_val.append(road.get_coordinates(ant1).x)
        y_val.append(road.get_coordinates(ant1).y)

    return (x_val, y_val)


def graph2(x,y,pasos):

    names=['Start', 'End']
    x_plot=[x[0], x[-1]]
    y_plot=[y[0],y[-1]]

    grafica=figure(title="Recorrido", x_axis_label="x axis", y_axis_label='y axis')
    grafica.line(x,y,legend_label="Random Walk", color="purple", name='Fire ant')
    #grafica.line(x[0:2],y[0:2],color='black',line_width=10)
    #grafica.line(x[-3:-1],y[-3:-1],color='red',line_width=10) #punto final y final-1
    #grafica.line(x[0:-1:pasos-1],y[0:-1:pasos-1]) #linea de punto inicial a punto final
    grafica.line(x_plot,y_plot, color="firebrick")

    grafica.circle(x_plot, y_plot, size=10,color="slateblue",alpha=0.5)
    #source = ColumnDataSource(data=dict(x=x_plot,y=y_plot,names=names))
    #labels = LabelSet(x='x',y='y',text='names',level='glyph',x_offset=5,y_offset=5,source=source,render_mode='canvas')
    #grafica.add_layout(labels)
    show(grafica)



def main2(pasos, ant_type):
    road_2=road()
    x_coords, y_coords=walk2(road_2, pasos, ant_type)
    graph2(x_coords,y_coords, pasos)


if __name__=='__main__':
    steps=[10,100,1000,10000]
    runs=100
    pasos=5000
    main2(pasos,fireant)
    #main(steps, runs, fireant)
