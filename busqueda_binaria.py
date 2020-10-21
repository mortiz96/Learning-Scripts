import random

def busqueda_lineal(lista, objetivo, iter_l=0):
    match=False

    for elemento in lista:
        iter_l+=1
        if elemento ==objetivo:
            match=True
            break

    return (match, iter_l)


def busqueda_binaria(lista, comienzo, final, objetivo, iter_b=0):
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    iter_b+=1

    if comienzo > final:
        return (False, iter_b)

    medio = (comienzo + final) // 2
    
    if lista[medio] == objetivo:
        return (True, iter_b)
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo, iter_b=iter_b)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo, iter_b=iter_b)


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano es la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])

    print(lista)

    (encontrado, iter_b) = busqueda_binaria(lista, 0, len(lista), objetivo)
    print(f'Bin: El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print('Iter bin: '+ str(iter_b))


    (encontrado, iter_l)=busqueda_lineal(lista, objetivo)
    print(f'Lin: El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print('Iter lin: '+ str(iter_l))
    
