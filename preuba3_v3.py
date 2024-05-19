from datetime import date
import os #En caso de usar clear
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

fecha=date.today()
fechaActual=fecha.strftime("%d/%m/%Y")

saldo = 500000
totalDeposito = 0
totalGiro = 0
totalTrans = 0
totalCompra = 0
#transacciones=[[f"{fechaActual}","Saldo Inicial","",saldo]]

def menu():
    print("-------------------------------------------------------------------------------------------------")
    print("Bienvenido a Python Bank, a continuación ingrese la opción de la operación que desea realizar.")
    print("1. Realizar un Deposito/Abono.")
    print("2. Realizar un Giro.")
    print("3. Realizar una Transferencia.")
    print("4. Realizar una Compra.")
    print("5. Realizar un Pago de Servicio.")
    print("6. Mostrar Saldo.")
    print("7. Mostrar Transacciones")
    print("8. Finalizar")
    print("-------------------------------------------------------------------------------------------------")

def leerOpcion():
    while True:
        try:
            opcion=int(input("Ingresa una opción:"))
            if opcion>=1 or opcion<=8:
                return opcion
            else:
                print("Ingrese una opción válida")
        except:
            print("Ingrese solo números del 1 al 8")

def deposito():
    global saldo
    global totalDeposito
    while True:
        try:
            transaccion=int(input("¿Cuánto desea desea depositar?: "))
            limiteDiario = 100000
            if transaccion>limiteDiario:
                print("Limite de deposito excedido")
            elif totalDeposito + transaccion >limiteDiario:
                print("No es posible realizar la operación, ha superado el monto diario a depositar")
                return
            else:
                saldo += transaccion
                totalDeposito += transaccion
                print(f"Se ha realizado un depósito de ${transaccion} correctamente")
                return {"tipo":"  Deposito   ", "monto":transaccion}
        except:
            print("Error de depósito")

def giro():
    global saldo
    global totalGiro
    while True:
        try:
            transaccion=int(input("¿Cuánto desea girar?: "))
            limiteDiario=200000
            if transaccion>saldo:
                print("No hay saldo suficiente para realizar el giro.")
            elif transaccion>limiteDiario:
                print("Limite de giro excedido")
            elif totalGiro+transaccion>limiteDiario:
                print("No es posible realizar la operación, ha superado el monto diario a depositar")
            else:
                saldo -= transaccion
                totalGiro += transaccion
                print(f"Se ha realizado un giro de ${transaccion} correctamente")
                return {"tipo":"     Giro    ", "monto":transaccion}
        except:
            print("Error de giro")  

def transferencia():
    global saldo
    global totalTrans
    while True:
            try:
                while True:
                    cuenta=int(input("Ingrese el N° de la cuenta a la que desea tranferir: (8 dígitos RUT, sin dígito verificador)"))
                    if cuenta>100 and cuenta<99999999:
                        break
                    else:
                        print("Cuenta no válida")
                while True:
                        transaccion=int(input("¿Cuánto desea transferir?: "))
                        limiteDiario=250000 
                        if transaccion>saldo:
                            print("No hay saldo suficiente para realizar la transferencia.")
                        elif transaccion>limiteDiario:
                            print("Limite de transferencia excedido")
                        elif totalTrans+transaccion>limiteDiario:
                            print("No es posible realizar la operación, ha superado el monto diario a depositar")
                        else:
                            saldo -= transaccion
                            print(f"Se ha realizado la transferencia de ${transaccion} correctamente")
                            return {"tipo": "Transferencia", "monto":transaccion}
            except:
                print("Error de transferencia")

def compras():
    global saldo
    while True:
        try:
            transaccion=int(input("Ingrese el valor de la compra:"))
            if transaccion>saldo:
                print("No hay saldo suficiente para el giro.")
            else:
                saldo -= transaccion
                print(f"Se ha realizado una compra de ${transaccion} correctamente")
                return {"tipo":"   Compra    ", "monto":transaccion}
        except:
            print("Error de compra") 


def pagoServicios():
    global saldo
    print("Pago de Servicios: ")
    print("1. Agua")
    print("2. Telefonía")
    print("3. Energía Eléctrica")
    print("4. Gas")
    print("5. Otros")
    while True:
        try:
            while True:
                cuenta=int(input("Ingrese el Servicio a Pagar: "))
                if cuenta>0 and cuenta<6:
                    break
                else:
                    print("Opción no válida")
            while True:
                    transaccion=int(input("¿Cuánto es el monto a pagar?: "))
                    if transaccion>saldo:
                        print("No hay saldo suficiente para realizar el pago.")
                    else:
                        saldo -= transaccion
                        print(f"Se ha realizado el pago de ${transaccion} correctamente")
                        return {"tipo": "Pago Servicio", "monto":transaccion}
        except:
            print("Error de pago")


def generar_transacciones(reporte):
    print("************************************************************************")
    print("|      Fecha     |       Transacción       |    Monto    |    Saldo    |")
    print("************************************************************************")
    for linea in reporte:
        print(f"|   {linea['fecha']}   |      {linea['tipo']}      |    {linea['monto']}    |    {linea['saldoAcumulado']}   |")


def transacciones(transaccion,saldoAcumulado):
    tipo=transaccion["tipo"]
    monto=transaccion["monto"]
    if tipo in ["Deposito"]:
        saldoAcumulado=saldoAcumulado+monto
    else:
        saldoAcumulado=saldoAcumulado-monto
    reporte.append({"fecha":fechaActual,"tipo":tipo, "monto":monto, "saldoAcumulado":saldoAcumulado})
    return saldoAcumulado
    pass
#PP
saldoAcumulado=saldo
reporte=[]

while True:
    menu()
    opc=leerOpcion()
    match opc:
        case 1: transaccion=deposito()
        case 2: transaccion=giro()
        case 3: transaccion=transferencia()
        case 4: transaccion=compras()
        case 5: transaccion=pagoServicios()
        case 6: print("Su saldo es:",saldo)
        case 7: generar_transacciones(reporte)
        case 8: break

    if opc in [1,2]:
        if transaccion:
            saldoAcumulado = transacciones(transaccion, saldoAcumulado)
    elif opc in [3,4,5]:
        saldoAcumulado = transacciones(transaccion, saldoAcumulado)
print("Gracias por usar los servicios de Python Bank")