from Autor_Negocio import Autor_Negocio

def menu():
    print("===== MENÚ =====")
    print("1. Agregar Autor")
    print("2. Editar Autor")
    print("3. Eliminar Autor")
    print("4. Salir")

def main():
    autor_negocio = Autor_Negocio()
    autor_negocio.cargar_desde_xlsx()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("===== AGREGAR AUTOR =====")
            cod_autor = input("Código del autor: ")
            nombre = input("Nombre: ")
            apellido_paterno = input("Apellido Paterno: ")
            apellido_materno = input("Apellido Materno: ")
            fecha_nacimiento = input("Fecha de Nacimiento: ")
            pais = input("País: ")
            editorial = input("Editorial: ")
            autor_negocio.agregar_autor(cod_autor, nombre, apellido_paterno, apellido_materno,
                                        fecha_nacimiento, pais, editorial)
        elif opcion == "2":
            print("===== EDITAR AUTOR =====")
            cod_autor = input("Código del autor que desea editar: ")
            nuevo_codigo = input("Nuevo Código: ")
            nuevo_nombre = input("Nuevo Nombre: ")
            nuevo_apellido_paterno = input("Nuevo Apellido Paterno: ")
            nuevo_apellido_materno = input("Nuevo Apellido Materno: ")
            nueva_fecha_nacimiento = input("Nueva Fecha de Nacimiento: ")
            nuevo_pais = input("Nuevo País: ")
            nueva_editorial = input("Nueva Editorial: ")
            if autor_negocio.editar_autor(cod_autor, nuevo_codigo, nuevo_nombre, nuevo_apellido_paterno,
                                          nuevo_apellido_materno, nueva_fecha_nacimiento, nuevo_pais, nueva_editorial):
                print("Autor editado exitosamente.")
            else:
                print("No se encontró ningún autor con ese código.")
        elif opcion == "3":
            print("===== ELIMINAR AUTOR =====")
            cod_autor = input("Código del autor que desea eliminar: ")
            if autor_negocio.eliminar_autor(cod_autor):
                print("Autor eliminado exitosamente.")
            else:
                print("No se encontró ningún autor con ese código.")
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
