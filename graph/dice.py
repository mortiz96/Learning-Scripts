import random
from bokeh.plotting import figure,show 

def throw(tries):
    run_result = []

    for i in range(tries):
        output = random.choice([1, 2, 3, 4, 5, 6])
        run_result.append(output)

    return run_result



def plot(data):
    chart=figure(title="Chances of getting 1 in when throwing a dice ", x_axis_label="Runs", y_axis_label="P")
    chart.line(list(range(0,runs)),data)

def main(tries, runs):
    results = []
    probability=[]
    
    run_plot=list(range(1,runs))
    for this in range(runs):
        secuence = throw(tries)
        results.append(secuence)

        is_one=0
        for this in results:
            if 1 in this:
                is_one+=1
        this_try=is_one/int(len(results))
        probability.append(this_try)

    tiros_con_1 = 0
    for actual in results:
        if 1  in actual:
            tiros_con_1 += 1

    plot(probability)
    probabilidad_tiros_con_1 = tiros_con_1 / runs
    print(f'Probabilidad de obtener por lo menos un 1 en {tries} tiros = {probabilidad_tiros_con_1}')



if __name__ == '__main__':
    tries = int(input('Tries: '))
    runs = int(input('Runs: '))

    main(tries, runs)