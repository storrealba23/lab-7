"""
captura.py — Registro de empleados.
 
Contiene las funciones de entrada con validación (reutilizadas por otros
módulos) y el registro de empleados como diccionarios dentro de una lista.
"""
import math
 
EDAD_MINIMA = 16
EDAD_MAXIMA = 100
 
 
def pedir_texto(mensaje):
    """Pide un texto y repite hasta que no esté vacío."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("  El valor no puede estar vacío.")
 
 
def pedir_entero(mensaje, minimo, maximo):
    """Pide un entero dentro del rango [minimo, maximo]."""
    while True:
        try:
            valor = int(input(mensaje).strip())
        except ValueError:
            print("  Ingresa un número entero válido.")
            continue
        if minimo <= valor <= maximo:
            return valor
        print(f"  El valor debe estar entre {minimo} y {maximo}.")
 
 
def pedir_decimal(mensaje):
    """Pide un número finito mayor que cero (acepta coma o punto decimal)."""
    while True:
        texto = input(mensaje).strip().replace(",", ".")
        try:
            valor = float(texto)
        except ValueError:
            print("  ⚠ Ingresa un número válido (ejemplo: 950 o 950.50).")
            continue
        if not math.isfinite(valor) or valor <= 0:
            print("  ⚠ El valor debe ser un número mayor que cero.")
            continue
        return valor
 
 
def pedir_si_no(mensaje):
    """Pide una confirmación s/n y devuelve True o False."""
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta in ("s", "si", "sí"):
            return True
        if respuesta in ("n", "no"):
            return False
        print("  Responde con 's' o 'n'.")
 
 
def capturar_empleado():
    """Solicita los datos de UN empleado y devuelve su diccionario."""
    nombre = pedir_texto("Nombre: ")
    edad = pedir_entero(f"Edad ({EDAD_MINIMA}-{EDAD_MAXIMA}): ",
                        EDAD_MINIMA, EDAD_MAXIMA)
    salario = pedir_decimal("Salario mensual: ")
    dpto = pedir_texto("Departamento: ")
    return {"nombre": nombre, "edad": edad, "salario": salario, "dpto": dpto}
 
 
def ingresar_empleados(empleados):
    """Registra uno o varios empleados y los agrega a la lista recibida."""
    print("\n--- Registro de empleados ---")
    while True:
        empleado = capturar_empleado()
        empleados.append(empleado)
        print(f"  Empleado '{empleado['nombre']}' registrado.")
        if not pedir_si_no("¿Deseas registrar otro empleado? (s/n): "):
            break
 
