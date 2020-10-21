def esprimo(num, ite):
    import random
    a=random.randint(1,num-1)
    if (a**(num-1))% num==1:
        return True
    else:#¿Fool a?
        return False
            

def run():
    print("""
    Prueba de Primalidad de Fermat

    """)

    num=int(input('Digite un número: '))
    ite=int(input('Digite el # de iteraciones: '))
    if esprimo(num, ite)==True:
        print(str(num)+' es primo')
    else:#Primer resultado sugiere que no es primo
        import random
        contador=0
        for i in range(1,ite):#Inicia el proceso de iteraciones para encontrar Fools y Witnesses
            b=random.randint(1,num-1)
            if (b**num)% num==1:
                contador+=1
            prob=round(2**ite)# p(no witness)<= 1/2**t
        print('Fools: '+str(contador))
        print('Witnesses: '+str(ite-contador))
        print('Es muuy probable que '+str(num)+' no sea primo')
        print('Probabilidad de escoger 100%  fools es de 1 en '+str(prob)+'\n')
        print('Explicación del método')
        print('https://es.wikipedia.org/wiki/Test_de_primalidad_de_Fermat')
        

if __name__ == "__main__":
    run()