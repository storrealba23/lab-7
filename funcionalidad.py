"""
funcionalidad.py — Operaciones sobre la lista de empleados.
"""
from captura import pedir_decimal, pedir_entero
 
 
def _mostrar_tabla(lista):
    """Imprime una lista de empleados en formato de tabla."""
    print(f"\n{'#':<4}{'Nombre':<20}{'Edad':<6}{'Salario':>12}  Departamento")
    print("-" * 56)
    for i, emp in enumerate(lista, start=1):
        print(f"{i:<4}{emp['nombre']:<20}{emp['edad']:<6}"
              f"{emp['salario']:>12,.2f}  {emp['dpto']}")
 
 
def listar_empleados(empleados):
    """Muestra la información de todos los empleados registrados."""
    if not empleados:
        print("No hay empleados registrados.")
        return
    _mostrar_tabla(empleados)
 
 
def buscar_por_departamento(empleados, dpto_a_buscar):
    """Muestra los empleados del departamento indicado (sin distinguir
    mayúsculas/minúsculas). Devuelve la lista de coincidencias."""
    buscado = dpto_a_buscar.strip().lower()
    encontrados = [e for e in empleados if e["dpto"].strip().lower() == buscado]
    if not encontrados:
        print(f"No se encontraron empleados en el departamento "
              f"'{dpto_a_buscar}'.")
    else:
        print(f"\nEmpleados del departamento '{dpto_a_buscar}':")
        _mostrar_tabla(encontrados)
    return encontrados
 
 
def aplicar_aumento_salarial(empleados, empleado_a_buscar):
    """Solicita un porcentaje y lo aplica al salario del empleado indicado.
    Si hay varios con el mismo nombre, pide elegir cuál. Devuelve True si
    se aplicó el aumento y False en caso contrario."""
    buscado = empleado_a_buscar.strip().lower()
    coincidencias = [e for e in empleados
                     if e["nombre"].strip().lower() == buscado]
 
    if not coincidencias:
        print(f"No se encontró ningún empleado llamado "
              f"'{empleado_a_buscar}'.")
        return False
 
    if len(coincidencias) == 1:
        empleado = coincidencias[0]
    else:
        print(f"Hay {len(coincidencias)} empleados con ese nombre:")
        _mostrar_tabla(coincidencias)
        indice = pedir_entero(f"Elige cuál (1-{len(coincidencias)}): ",
                              1, len(coincidencias))
        empleado = coincidencias[indice - 1]
 
    porcentaje = pedir_decimal("Porcentaje de aumento (ej. 10 para 10%): ")
    anterior = empleado["salario"]
    empleado["salario"] = round(anterior * (1 + porcentaje / 100), 2)
    print(f"  Salario de {empleado['nombre']}: {anterior:,.2f} → "
          f"{empleado['salario']:,.2f} (+{porcentaje:g}%)")
    return True
 
 
def obtener_promedio_salarial(empleados):
    """Devuelve el salario promedio general (0.0 si no hay empleados)."""
    if not empleados:
        return 0.0
    return sum(e["salario"] for e in empleados) / len(empleados)