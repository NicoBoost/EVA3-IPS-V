def menu():
    print("1. Depositar")
    print("2. Girar")
    print("3. Transferir")
    print("4. Comprar")
    print("5. Pagar (servicios básicos)")
    print("6. Mostrar Transacciones")
    print("7. Finalizar/Salir")

def leerOpcion():
    while True:
        try:
            opcion = int(input("Cuál es su opción (1-7): "))
            if 1 <= opcion <= 7:
                return opcion
            else:
                print("Opción no válida. Por favor, elija un número entre 1 y 7.")
        except ValueError:
            print("Debes ingresar solo números enteros")

def deposito():
    while True:
        try:
            transaccion = int(input("Ingresar monto a abonar a la cuenta: "))
            if transaccion > 0:
                print(f"Depósito de ${transaccion} ingresado correctamente :)")
                return {"tipo": "abono", "monto": transaccion}
            else:
                print("El monto del depósito debe ser > 0")
        except ValueError:
            print("Debes ingresar solo números enteros")

def giro():
    while True:
        try:
            transaccion = int(input("Ingresar monto a girar de la cuenta: "))
            if transaccion > 0:
                print(f"Giro de ${transaccion} realizado correctamente :)")
                return {"tipo": "retiro", "monto": transaccion}
            else:
                print("El monto del giro debe ser > 0")
        except ValueError:
            print("Debes ingresar solo números enteros")

def transferir():
    while True:
        try:
            transaccion = int(input("Ingresar monto a transferir: "))
            if transaccion > 0:
                print(f"Transferencia de ${transaccion} realizada correctamente :)")
                return {"tipo": "transferencia", "monto": transaccion}
            else:
                print("El monto de la transferencia debe ser > 0")
        except ValueError:
            print("Debes ingresar solo números enteros")

def compra():
    while True:
        try:
            transaccion = int(input("Ingresar monto de la compra: "))
            if transaccion > 0:
                print(f"Compra de ${transaccion} realizada correctamente :)")
                return {"tipo": "compra", "monto": transaccion}
            else:
                print("El monto de la compra debe ser > 0")
        except ValueError:
            print("Debes ingresar solo números enteros")

def pago():
    while True:
        try:
            transaccion = int(input("Ingresar monto del pago de servicios: "))
            if transaccion > 0:
                print(f"Pago de servicios por ${transaccion} realizado correctamente :)")
                return {"tipo": "pago", "monto": transaccion}
            else:
                print("El monto del pago debe ser > 0")
        except ValueError:
            print("Debes ingresar solo números enteros")

def generar_reporte_transacciones(reporte):
    print("Reporte de Transacciones:")
    for linea in reporte:
        print(f"Tipo: {linea['tipo']}, Monto: {linea['monto']}, Saldo Acumulado: {linea['saldo_acumulado']}")

def guardarTrannsaccion(transaccion, saldo_acumulado):
    tipo = transaccion['tipo']
    monto = transaccion['monto']

    if tipo in ['abono', 'transferencia']:
        saldo_acumulado += monto
    else:
        saldo_acumulado -= monto

    reporte.append({
        'tipo': tipo,
        'monto': monto,
        'saldo_acumulado': saldo_acumulado
    })
    return saldo_acumulado

# Programa Principal
saldoInicial = 500000
saldo_acumulado = saldoInicial
reporte = []

while True:
    menu()
    opc = leerOpcion()
    match opc:
        case 1:
            transaccion = deposito()
        case 2:
            transaccion = giro()
        case 3:
            transaccion = transferir()
        case 4:
            transaccion = compra()
        case 5:
            transaccion = pago()
        case 6:
            generar_reporte_transacciones(reporte)
            continue
        case 7:
            break

    if opc in [1, 2, 3, 4, 5]:
        saldo_acumulado = guardarTrannsaccion(transaccion, saldo_acumulado)

print("--- Ha salido del Banco ---")
