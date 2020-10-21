menu= """
Bienvenido al conversor de monedas 🌏

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    pesos=input("Ingrese pesos colombianos: ")
    pesos = float(pesos)
    valor_dolar=3875
    dolar=pesos/valor_dolar
    dolar=round(dolar, 2)
    dolar=str(dolar)
    print("Tienes $" + dolar + " dolares")
elif opcion == 2:
    pesos=input("Ingrese pesos argentinos: ")
    pesos = float(pesos)
    valor_dolar=65
    dolar=pesos/valor_dolar
    dolar=round(dolar, 2)
    dolar=str(dolar)
elif opcion == 3:
    pesos=input("Ingrese pesos mexicanos: ")
    pesos = float(pesos)
    valor_dolar=24
    dolar=pesos/valor_dolar
    dolar=round(dolar, 2)
    dolar=str(dolar)
    print("Tienes $" + dolar + " dolares")