from Persona import Persona
from Autor import Autor
from Categoria import Categoria
from Libro import Libro
import os

def clear_screen():
    """
    Limpia la pantalla de la consola, utilizando 'cls' en Windows y 'clear' en Unix/Linux.
    """
    os.system("cls" if os.name == "nt" else "clear")

def Menu_autor():
    """
    Menú de gestión de autores:
    1. Agregar un nuevo autor.
    2. Editar la información de un autor existente.
    3. Eliminar un autor.
    4. Volver al menú principal.
    """
    while True:
        clear_screen()
        print("==== MENU AUTOR ====")
        print("1. AGREGAR")
        print("2. EDITAR")
        print("3. ELIMINAR")
        print("4. <= VOLVER")
        
        op_autor = input("Ingrese una opción: ")
        
        if op_autor == "1":
            clear_screen()
            Autor.agregar_autor()
            input("Enter para continuar...")
        elif op_autor == "2":
            clear_screen()
            Autor.editar_autor()
            input("Enter para continuar...")
        elif op_autor == "3":
            clear_screen()
            Autor.eliminar_autor()
            input("Enter para continuar...")
        elif op_autor == "4":
            break
        else:
            input("Opción incorrecta. Enter para volver a intentar...")
            
def Menu_libro():
    """
    Menú de gestión de libros:
    1. Agregar un nuevo libro.
    2. Editar la información de un libro existente.
    3. Eliminar un libro.
    4. Volver al menú principal.
    """
    while True:
        clear_screen()
        print("==== MENU LIBROS ====")
        print("1. AGREGAR")
        print("2. EDITAR")
        print("3. ELIMINAR")
        print("4. <= VOLVER")
        op_libro = input("Ingrese una opcion: ")
        if op_libro == "1":
            clear_screen()
            Libro.agregar_libro()
            input("Enter para continuar...")
        elif op_libro == "2":
            clear_screen()
            Libro.editar_libro()
            input("Enter para continuar...")
        elif op_libro == "3":
            clear_screen()
            Libro.eliminar_libro()
            input("Enter para continuar...")
        elif op_libro == "4":
            break
        else:
            input("Opción incorrecta. Enter para volver a intentar...")

def main_menu():
    """
    Menú principal del programa:
    1. Gestionar autores.
    2. Gestionar libros.
    3. Realizar búsquedas por categoría.
    4. Mostrar el reporte de libros en orden ascendente del cod_categoria
    5. Salir del programa.
    """
    while True:
        clear_screen()
        print("=== MENÚ PRINCIPAL ===")
        print("1. AUTOR")
        print("2. LIBROS")
        print("3. BUSQUEDA")
        print("4. REPORTE LIBROS")
        print("5. SALIR")
        
        option = input("Ingrese una opción: ")
        
        if option == "1":
            Menu_autor()
        elif option == "2":
            Menu_libro()
        elif option == "3":
            clear_screen()
            cod_categoria_deseado = input("Ingrese el código de la categoría: ")
            Categoria.mostrar_libros_por_categoria(cod_categoria_deseado)
            input("Enter para continuar...")
        elif option == "4":
            clear_screen()
            Categoria.mostrar_libros_por_categoria_ordenados_ascendente()
            input("Enter para continuar...")
        elif option == "5":
            break
        else:
            input("Opción incorrecta. Enter para volver a intentar...")

if __name__ == "__main__":
    main_menu()
