import random

def merge_sort(lista):
    if len(lista)==1:
        return lista
    else:
        medio=len(lista)//2
        array1=lista[0:medio]
        array2=lista[medio:len(lista)]

        print(f': Before: Izquierda: {array1}, derecha: {array2}')#ejecuta merge sólo cuando el tamaño del vector es 1


        array1=merge_sort(array1)
        array2=merge_sort(array2)

    i=0
    j=0
    k=0

    print(f': Izquierda: {array1}, derecha: {array2}')#ejecuta merge sólo cuando el tamaño del vector es 1


    while i<len(array1) and j<len(array2):
        if array1[i]<array2[j]:
            lista[k]=array1[i]
            #array1.remove(array1[i])
            i+=1
        else:
            lista[k]=array2[j]
            #array2.remove(array2[i])
            j+=1
        k+=1

    
    while i<len(array1):
        lista[k]=array1[i]
        #array1.remove(array1[i])
        i+=1
        k+=1

    while j<len(array2):
        lista[k]=(array2[j])
        #array2.remove(array2[i])
        j+=1
        k+=1

    print(f'{k}, {lista}')

    return lista
    


if __name__ == "__main__":
    tamano_de_lista = int(input('De que tamano sera la lista? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(f'Lista original: {lista}')

    merge_sort(lista)
    print(f'Lista ordenada: {lista}')
 