def generar_reporte_transacciones(transacciones):
    """
    Genera un reporte de transacciones mostrando los abonos y el saldo sumado por línea.
    
    Args:
    transacciones (list of dict): Lista de transacciones, donde cada transacción es un diccionario
                                  con las claves 'tipo' (str, 'abono' o 'retiro') y 'monto' (float).
                                  
    Returns:
    list of dict: Lista de reportes de transacciones con las claves 'tipo', 'monto' y 'saldo_acumulado'.
    """
    
    saldo_acumulado = 0
    reporte = []

    for transaccion in transacciones:
        tipo = transaccion['tipo']
        monto = transaccion['monto']

        if tipo == 'abono':
            saldo_acumulado += monto
        elif tipo == 'retiro':
            saldo_acumulado -= monto
        
        reporte.append({
            'tipo': tipo,
            'monto': monto,
            'saldo_acumulado': saldo_acumulado
        })
    
    return reporte

# Ejemplo de uso
transacciones = [
    {'tipo': 'abono', 'monto': 1000.0},
    {'tipo': 'retiro', 'monto': 200.0},
    {'tipo': 'abono', 'monto': 500.0},
    {'tipo': 'retiro', 'monto': 100.0}
]

reporte = generar_reporte_transacciones(transacciones)

for linea in reporte:
    print(f"Tipo: {linea['tipo']}, Monto: {linea['monto']}, Saldo Acumulado: {linea['saldo_acumulado']}")
