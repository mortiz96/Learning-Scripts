import statistics as stat
import random
import math


def generate_dots(number_dots):
    inside=0

    for _ in range(number_dots):
        x=random.random()*random.choice([-1,1])#Generar coordenada en X
        y=random.random()*random.choice([-1,1])#Generar coordenada en X
        
        distance_origin=math.sqrt(x**2+y**2)

        if distance_origin >=1:
            inside+=1

    return (4**inside/number_dots) #Estimate of pi


def estimate(number_dots, runs):
    estimates=[]

    for _ in range(runs):
        estimation=generate_dots(number_dots)
        estimates.append(estimation)

    avg_estimates=stat.mean(estimates)
    stdev_estimates=stat.stdev(estimates)
    print(f'Estimate={round(avg_estimates,5)}, Sigma={round(stdev_estimates,5)}, Runs: {number_dots}')

    return (avg_estimates,stdev_estimates)


def calc_pi(precision, runs):
    number_dots=1000
    sigma=precision

    while sigma >= precision/1.96:
        mean, sigma=estimate(number_dots,runs)
        number_dots*=2
    
    return mean

if __name__ == '__main__':

    calc_pi(0.01,1000)

      


