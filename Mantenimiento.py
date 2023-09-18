from Persona import Persona
import shutil
import datetime
import os

class Mantenimiento:
    def __init__(self):
        self.errores = []  # Inicializamos una lista para almacenar los errores

    def agregar_error(self, mensaje):
        self.errores.append(mensaje)

    def mostrar_errores(self):
        if self.errores:
            print("==== ERRORES ====")
            for error in self.errores:
                print(error)
        else:
            print("No se han registrado errores.")

    @staticmethod
    def respaldar_archivo():
        try:
            fecha_actual = datetime.datetime.now()
            fecha_formateada = fecha_actual.strftime("%Y%m%d_%H%M%S")
            nombre_archivo_respaldo = f"respaldo_libros_{fecha_formateada}.txt"
            shutil.copy(os.getcwd() + "\\REPORTE_LIBROS.txt", os.getcwd() + f"\\{nombre_archivo_respaldo}")
            print(f"Se ha creado un respaldo del archivo 'REPORTE_LIBROS.txt' como '{nombre_archivo_respaldo}'.")
        except Exception as e:
            mensaje = f"Error al crear el respaldo: {str(e)}"
            print(mensaje)
            self.agregar_error(mensaje)

    @staticmethod
    def vaciar_archivo():
        try:
            with open("REPORTE_LIBROS.txt", "w") as file:
                file.truncate(0)
            print("El archivo 'REPORTE_LIBROS.txt' se ha vaciado correctamente.")
        except Exception as e:
            mensaje = f"Error al vaciar el archivo: {str(e)}"
            print(mensaje)
            self.agregar_error(mensaje)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def main_menu():
    mantenimiento = Mantenimiento()  # Crear una instancia de Mantenimiento

    while True:
        clear_screen()
        print("=== MENÚ PRINCIPAL ===")
        print("1. Vaciar archivo 'REPORTE_LIBROS.txt'")
        print("2. Crear respaldo")
        print("3. Mostrar Errores")

        option = input("Ingrese una opción: ")

        if option == "1":
            clear_screen()
            try:
                Mantenimiento.vaciar_archivo()
            except Exception as e:
                mensaje = f"Error al vaciar archivo: {str(e)}"
                print(mensaje)
                mantenimiento.agregar_error(mensaje)
            input("Enter para continuar...")
        elif option == "2":
            clear_screen()
            try:
                Mantenimiento.respaldar_archivo()
            except Exception as e:
                mensaje = f"Error al crear respaldo: {str(e)}"
                print(mensaje)
                mantenimiento.agregar_error(mensaje)
            input("Enter para continuar...")
        elif option == "3":
            clear_screen()
            mantenimiento.mostrar_errores()  # Mostrar errores almacenados
            input("Enter para continuar...")
        else:
            input("Opción incorrecta. Enter para volver a intentar...")

if __name__ == "__main__":
    main_menu()
