import random 
def busqueda_lineal(lista, objetivo):
    match=False

    for elemento in lista:
        if elemento ==objetivo:
            match=True
            break

    return match

if __name__=='__main__':
    lista_tamaño=int(input('Tamaño lista: '))
    objetivo=int(input('Objetivo :'))

    lista = [random.randint(0,100) for i in range(lista_tamaño)]
    encontrado=busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')