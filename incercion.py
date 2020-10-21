def insertion_sort(some_list):
    for i in range(len(some_list)):
        for j in range(i, 0, -1):
            if some_list[j] < some_list[j - 1]:
                some_list[j], some_list[j - 1] = some_list[j - 1], some_list[j]
                continue
            break
    return print(lista)

def insertion_sort2(lista):
    for i in range(1, len(lista)):
        for j in range(i,0,-1):
            if lista[j]<lista[j-1]: #swap
                va=lista[j]
                lista[j]=lista[j-1]
                lista[j-1]=va
                print(lista)
            else:
                break
    return print(lista)



if __name__ == "__main__":
    lista=[7,3,2,9,8]
    insertion_sort2(lista)

