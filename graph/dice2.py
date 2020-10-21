import random

def tirar_dado(tries):
    run_result = []

    for _ in range(tries):
        output = random.choice([1, 2, 3, 4, 5, 6])
        run_result.append(output)

    return run_result

def main(tries, runs):
    tiros = []
    for _ in range(runs):
        secuencia_de_tiros = tirar_dado(tries)
        tiros.append(secuencia_de_tiros)

    tiros_con_1 = 0
    for tiro in tiros:
        if 1 not in tiro:
            tiros_con_1 += 1

    probabilidad_tiros_con_1 = tiros_con_1 / runs
    print(f'Probabilidad de no obtener por lo menos un 1 en {tries} tiros = {probabilidad_tiros_con_1}')



if __name__ == '__main__':
    tries = int(input('Cuantas tiros del dado: '))
    runs = int(input('Cuantas veces correra la simulacion: '))

    main(tries, runs)