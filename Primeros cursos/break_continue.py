def run():
    # for contador in range(1001):
    #     if contador%2 != 0:
    #         continue
        # print(contador)

    # for i in range(10000):
    #     print(i)
    #     if i==5678:
    #         break

    # texto=input('Escribe un texto: ').upper()
    # for letra in texto:
    #     if letra=='O':
    #         break
    #     print(letra)

    # LIMITE=int(input('Ingrese un límite: '))
    # omit=int(input('Omitir multiplos de: '))
    # i=0
    # while i < LIMITE:
    #     i+=1
    #     if i % omit ==0:#i es multiplo 
    #         continue
    #     print(str(i))#omitirlo
    

    print("""
    Contador de vocales y consonantes en una frase
    """)
    frase=input('Ingresa una frase: ').strip()
    largo=(len(frase))
    v=0 #contador de vocales
    e=0 #contador de caracteres especiales
    vocales=("a", "e","i","o","u")
    especiales=("!",'@','$','&','?','¿')
    for i in range(0,largo):
        if frase[i] in vocales:
            v+=1
        if frase[i] in especiales:
            e+=1
    c=largo-v-e
    print('Tu frase tiene: ' +str(v)+' vocales, '+str(c)+ ' consonantes\n'+  'y '+str(e)+' caracteres especiales')  


if __name__=='__main__':
    run()