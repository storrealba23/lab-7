"""
main.py — Programa principal: menú interactivo del sistema de empleados.
"""
from captura import ingresar_empleados, pedir_texto
from funcionalidad import (listar_empleados, buscar_por_departamento,
                           aplicar_aumento_salarial)
from estadisticas import mostrar_estadisticas
 
 
def mostrar_menu():
    print("\n=== Menú Principal ===")
    print("1. Ingresar empleados")
    print("2. Mostrar empleados")
    print("3. Buscar por departamento")
    print("4. Aplicar aumento salarial")
    print("5. Mostrar estadísticas")
    print("6. Salir")
 
 
def main():
    empleados = []  # Aquí se almacena la información de todos los empleados
 
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-6): ").strip()
 
        if opcion == "1":
            ingresar_empleados(empleados)
        elif opcion == "2":
            listar_empleados(empleados)
        elif opcion == "3":
            if not empleados:
                print("No hay empleados registrados.")
                continue
            dpto = pedir_texto("Nombre del departamento a buscar: ")
            buscar_por_departamento(empleados, dpto)
        elif opcion == "4":
            if not empleados:
                print("No hay empleados registrados.")
                continue
            nombre = pedir_texto("Nombre del empleado a buscar: ")
            aplicar_aumento_salarial(empleados, nombre)
        elif opcion == "5":
            mostrar_estadisticas(empleados)
        elif opcion == "6":
            print("Hasta luego.")
            break
        else:
            print("  Opción inválida. Elige un número del 1 al 6.")
 
 
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nPrograma interrumpido por el usuario.")
 