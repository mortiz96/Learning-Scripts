def es_primo(num):
    contador =0

    for i in range(1, num+1):
        if i==1 or i==num:#Excepción dentro del for
            continue
        if num %i ==0:
            contador+=1
    if contador ==0:
        return True
    else: 
        return False

def run():
    num=int(input('Escribe un número: '))
    if es_primo(num):#==true es opcional
        print('Es primo')
    else:
        print('No es primo')
if __name__=='__main__':
    run()