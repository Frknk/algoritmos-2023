from Persona import Persona  # Importamos la clase Persona para la herencia

class Autor(Persona):
    """
    Clase que representa a un autor de libros, hereda de la clase Persona.
    """
    contador_personas = 0  # Contador de personas (autores)

    def __init__(self, cod_autor, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, pais, editorial):
        """
        Constructor de la clase Autor.
        Args:
            cod_autor (str): Código único del autor.
            nombre (str): Nombre del autor.
            apellido_paterno (str): Apellido paterno del autor.
            apellido_materno (str): Apellido materno del autor.
            fecha_nacimiento (str): Fecha de nacimiento del autor (formato: "dd/mm/aaaa").
            pais (str): País de origen del autor.
            editorial (str): Editorial asociada al autor.
        """
        Autor.contador_personas += 1
        cod_persona = Autor.contador_personas
        super().__init__(cod_persona, nombre, apellido_paterno, apellido_materno, fecha_nacimiento)
        self.cod_autor = cod_autor
        self.pais = pais
        self.editorial = editorial

    @staticmethod
    def agregar_autor():
        """
        Permite al usuario agregar un nuevo autor al archivo "autores.txt". Solicita información sobre el
        código del autor, nombre, apellidos, fecha de nacimiento, país y editorial del autor, y luego agrega
        los detalles del autor al archivo.

        - Parámetros: Ninguno.
        - Retorno: Ninguno.
        - Excepciones: Puede generar excepciones si ocurre algún error durante la ejecución.
        """
        try:
            print("======NUEVO AUTOR======")
            cod_autor = input("CÓDIGO: ")
            nombre = input("NOMBRE: ")
            apellido_paterno = input("APELLIDO PATERNO: ")
            apellido_materno = input("APELLIDO MATERNO: ")
            fecha_nacimiento = input("FECHA DE NACIMIENTO: ")
            pais = input("PAIS: ")
            editorial = input("EDITORIAL: ")

            autor = Autor(cod_autor, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, pais, editorial)

            with open("autores.txt", "a") as file:
                file.write(f"AUTOR: {autor.cod_persona}\n")
                file.write(f"CÓDIGO: {autor.cod_autor}\n")
                file.write(f"NOMBRE: {autor.nombre}\n")
                file.write(f"APELLIDOS: {autor.apellido_paterno} {autor.apellido_materno}\n")
                file.write(f"FECHA DE NACIMIENTO: {autor.fecha_nacimiento}\n")
                file.write(f"PAIS: {autor.pais}\n")
                file.write(f"EDITORIAL: {autor.editorial}\n")
                file.write(f"================================\n")
            print("Autor agregado exitosamente.")
        except Exception as e:
            mensaje = f"Error al agregar autor: {str(e)}"
            print(mensaje)
            mantenimiento.agregar_error(mensaje)

    @staticmethod
    def editar_autor():
        """
        Permite al usuario editar la información de un autor existente en el archivo "autores.txt". 
        Solicita el código del autor a editar, muestra los datos actuales y permite ingresar nuevos datos.
        Luego, actualiza la información del autor en el archivo.

        - Parámetros: Ninguno.
        - Retorno: Ninguno.
        - Excepciones: Puede generar excepciones si ocurre algún error durante la ejecución.
        """
        try:
            cod_autor = input("Ingrese el código del autor que desea editar: ")

            with open("autores.txt", "r") as file:
                lines = file.readlines()

            found = False
            with open("autores.txt", "w") as file:
                for line in lines:
                    if line.startswith("CÓDIGO:"):
                        autor_data = line.strip().split(": ")[1]
                        if autor_data == cod_autor:
                            found = True
                            print("Autor encontrado. Ingrese los nuevos datos:")
                            print("========NUEVOS DATOS DEL AUTOR=========")
                            nombre = input("NUEVO-> NOMBRE: ")
                            apellido_paterno = input("NUEVO-> APELLIDO PATERNO: ")
                            apellido_materno = input("NUEVO-> APELLIDO MATERNO: ")
                            fecha_nacimiento = input("NUEVA-> FECHA DE NACIMIENTO: ")
                            pais = input("NUEVO-> PAIS: ")
                            editorial = input("NUEVA-> EDITORIAL: ")

                            file.write(f"AUTOR: {autor_data}\n")
                            file.write(f"CÓDIGO: {cod_autor}\n")
                            file.write(f"NOMBRE: {nombre}\n")
                            file.write(f"APELLIDOS: {apellido_paterno} {apellido_materno}\n")
                            file.write(f"FECHA DE NACIMIENTO: {fecha_nacimiento}\n")
                            file.write(f"PAIS: {pais}\n")
                            file.write(f"EDITORIAL: {editorial}\n")
                            file.write(f"================================\n")
                        else:
                            file.write(line)
                    else:
                        file.write(line)

            if not found:
                print("No se encontró ningún autor con ese código.")
            else:
                print("Autor editado exitosamente.")
        except Exception as e:
            print(f"Error al editar autor: {e}")

    @staticmethod
    def eliminar_autor():
        """
        Permite al usuario eliminar un autor existente del archivo "autores.txt" mediante su código.
        Busca al autor por su código, lo elimina y guarda los cambios en el archivo.

        - Parámetros: Ninguno.
        - Retorno: Ninguno.
        - Excepciones: Puede generar excepciones si ocurre algún error durante la ejecución.
        """
        try:
            cod_autor = input("Ingrese el código del autor que desea eliminar: ")

            with open("autores.txt", "r") as file:
                lines = file.readlines()

            found = False
            with open("autores.txt", "w") as file:
                for line in lines:
                    if line.startswith("CÓDIGO:"):
                        autor_data = line.strip().split(": ")[1]
                        if autor_data == cod_autor:
                            found = True
                            print("Autor encontrado y eliminado.")
                        else:
                            file.write(line)
                    else:
                        file.write(line)

            if not found:
                print("No se encontró ningún autor con ese código.")
        except Exception as e:
            print(f"Error al eliminar autor: {e}")