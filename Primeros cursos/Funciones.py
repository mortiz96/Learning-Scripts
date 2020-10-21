def conversor(tipo_pesos, valor_dolar):
    pesos=input("Ingrese pesos " + tipo_pesos +": ")
    pesos = float(pesos)
    dolar=pesos/valor_dolar
    dolar=round(dolar, 2)
    dolar=str(dolar)
    print("Tienes "+dolar+" dólares americanos")
menu= """
Bienvenido al conversor de monedas 🌏

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 65)
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print('Escoja una opción válida')