"""
estadisticas.py — Cálculo y visualización de estadísticas generales.
"""
from funcionalidad import obtener_promedio_salarial


def mostrar_estadisticas(empleados):
    """
    Muestra estadísticas generales sobre los empleados.
    """
    if not empleados:
        print("No hay empleados registrados para calcular estadísticas.")
        return

    total = len(empleados)
    edades = [e["edad"]for e in empleados]
    edad_promedio = sum(edades) / total
    menores_30 = len([e for e in empleados if e["edad"] < 30])

    salario_promedio = obtener_promedio_salarial(empleados)
    con_max = max(empleados, key=lambda e: e["salario"])
    con_min = min(empleados, key=lambda e: e["salario"])
    sobre_1000 = [e for e in empleados if e["salario"] > 1000]

    print("\n=== Estadísticas generales ===")
    print(f"Cantidad total de empleados : {total}")
    print(f"Edad promedio               : {edad_promedio:.1f} años")
    print(f"Empleados menores de 30     : {menores_30}")
    print(f"Salario promedio            : {salario_promedio:,.2f}")
    print(f"Salario máximo              : {con_max['salario']:,.2f} "
          f"({con_max['nombre']})")
    print(f"Salario mínimo              : {con_min['salario']:,.2f} "
          f"({con_min['nombre']})")
    if sobre_1000:
        print(f"¿Algún salario supera 1000? : Sí ({len(sobre_1000)} "
              f"empleado(s))")
    else:
        print("¿Algún salario supera 1000? : No")
 