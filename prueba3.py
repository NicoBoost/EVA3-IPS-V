def menu():
    print("1. Depositar")
    print("2. Girar")
    print("3. Transferir")
    print("4. Comprar")
    print("5. Pagar(servicios básicos)")
    print("6. Mostrar Transacciones")
    print("7. Finalizar/Salir")

def leerOpcion():
    opcion=int(input("Cuál es su opción (1-7):"))
    return opcion

def deposito():
    while True:
        try:
            while True:
                d=int(input("Ingresar monto a abonar a la cuenta: "))
                if d>0:
                    print(f"Depósito de ${d} ingresado correctamente :)")
                    return d
                else:
                    print("El número del depósito debe ser > 0")
        except:
            print("Debes ingresar sólo número enteros")

def giro():
    pass

def transferir():
    pass

def compra():
    pass

def pago():
    pass

def mostrarTrans():
    pass


##PP
saldo=460000
while True:
    menu()
    opc=leerOpcion()
    match opc:
        case 1: deposito()
        case 2: pass
        case 3: pass
        case 4: pass
        case 5: pass
        case 6: pass
        case 7: break
print("Hasta la vista baby...")