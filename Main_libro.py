from Libro_Negocio import Libro_Negocio
import openpyxl
# Ejemplo de uso
if __name__ == "__main__":
    negocio_libros = Libro_Negocio()
    negocio_libros.cargar_desde_xlsx()

    while True:
        print("===== MENÚ DE LIBROS =====")
        print("1. Agregar Libro")
        print("2. Editar Libro")
        print("3. Eliminar Libro")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Ingrese el código del libro: ")
            titulo = input("Ingrese el título del libro: ")
            año = input("Ingrese el año de publicación: ")
            tomo = input("Ingrese el tomo o volumen del libro: ")
            autor = input("Ingrese el autor del libro: ")
            negocio_libros.agregar_libro(codigo, titulo, año, tomo, autor)
        elif opcion == "2":
            codigo = input("Ingrese el código del libro que desea editar: ")
            nuevo_codigo = input("Ingrese el nuevo código del libro: ")
            nuevo_titulo = input("Ingrese el nuevo título del libro: ")
            nuevo_año = input("Ingrese el nuevo año de publicación: ")
            nuevo_tomo = input("Ingrese el nuevo tomo o volumen del libro: ")
            nuevo_autor = input("Ingrese el nuevo autor del libro: ")
            if negocio_libros.editar_libro(codigo, nuevo_codigo, nuevo_titulo, nuevo_año, nuevo_tomo, nuevo_autor):
                print("Libro editado exitosamente.")
            else:
                print("No se encontró ningún libro con ese código.")
        elif opcion == "3":
            codigo = input("Ingrese el código del libro que desea eliminar: ")
            if negocio_libros.eliminar_libro(codigo):
                print("Libro eliminado exitosamente.")
            else:
                print("No se encontró ningún libro con ese código.")
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo.")