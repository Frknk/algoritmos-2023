from Categoria import Categoria  # Importamos la clase Categoria para poder agregar categorías a los libros

class Libro:  
    """
    Clase que representa un libro.
    """

    def __init__(self, codigo_libro, titulo, año, tomo, autor):
        """
        Constructor de la clase Libro.

        Args:
            codigo_libro (str): Código único del libro.
            titulo (str): Título del libro.
            año (str): Año de publicación del libro.
            tomo (str): Tomo o volumen del libro.
            autor (str): Autor del libro.
        """
        self.codigo_libro = codigo_libro
        self.titulo = titulo
        self.año = año
        self.tomo = tomo
        self.autor = autor
    @staticmethod
    def agregar_libro():
        """
        Permite al usuario agregar un nuevo libro al archivo "REPORTE_LIBROS.txt". Solicita información sobre el
        código del libro, título, año, tomo, categoría y autor del libro, y luego agrega los detalles del libro
        al archivo.

        - Parámetros: Ninguno.
        - Retorno: Ninguno.
        - Excepciones: Puede generar excepciones si ocurre algún error durante la ejecución.
        """
        try:
            print("======NUEVO LIBRO======")
            codigo_libro = input("CÓDIGO: ")
            titulo = input("TÍTULO: ")
            año = input("AÑO: ")
            tomo = input("TOMO: ")

            # Mostrar categorías disponibles
            categorias = Categoria.obtener_categorias()
            print("CATEGORÍAS DISPONIBLES:")
            for i, categoria in enumerate(categorias):
                print(f"{i + 1}. {categoria.cod_categoria} - {categoria.categoria}")

            categoria_index = int(input("Seleccione el número de la categoría: ")) - 1
            categoria_elegida = categorias[categoria_index]

            agregar_autor = input("¿Desea agregar un autor? (S/N): ")
            if agregar_autor.upper() == "S":
                # Mostrar autores disponibles
                with open("autores.txt", "r") as file:
                    autores_disponibles = [line.strip() for line in file.readlines() if line.startswith("NOMBRE:")]

                if autores_disponibles:
                    print("AUTORES DISPONIBLES:")
                    for i, autor in enumerate(autores_disponibles):
                        print(f"{i + 1}. {autor.split(': ')[1]}")
                    autor_index = int(input("Seleccione el número del autor: ")) - 1
                    autor_elegido = autores_disponibles[autor_index].split(': ')[1]
                else:
                    print("No hay autores disponibles.")
                    autor_elegido = input("Ingrese el nombre del autor: ")
            else:
                autor_elegido = "Anónimo"

            with open("REPORTE_LIBROS.txt", "a") as file:
                file.write(f"CÓDIGO: {codigo_libro}\n")
                file.write(f"TÍTULO: {titulo}\n")
                file.write(f"AÑO: {año}\n")
                file.write(f"TOMO: {tomo}\n")
                file.write(f"AUTOR: {autor_elegido}\n")
                file.write(f"CATEGORÍA: {categoria_elegida.categoria}\n")
                file.write(f"COD_CATEGORIA: {categoria_elegida.cod_categoria}\n")
                file.write("================================\n")
            print("Libro agregado exitosamente.")
        except Exception as e:
            print(f"Error al agregar libro: {e}")

    @staticmethod
    def editar_libro():
        """
        Permite al usuario editar la información de un libro existente en el archivo "REPORTE_LIBROS.txt". 
        Solicita el código del libro a editar, muestra los datos actuales y permite ingresar nuevos datos.
        Luego, actualiza la información del libro en el archivo.

        - Parámetros: Ninguno.
        - Retorno: Ninguno.
        - Excepciones: Puede generar excepciones si ocurre algún error durante la ejecución.
        """
        try:
            codigo_libro = input("Ingrese el código del libro que desea editar: ")

            with open("REPORTE_LIBROS.txt", "r") as file:
                lines = file.readlines()

            found = False
            updated_lines = []  # Usaremos una lista para almacenar las líneas actualizadas

            i = 0
            while i < len(lines):
                line = lines[i]
                if line.startswith("CÓDIGO:") and line.strip().split(": ")[1] == codigo_libro:
                    found = True
                    print("Libro encontrado. Ingrese los nuevos datos:")
                    print("========NUEVOS DATOS DEL LIBRO=========")
                    nuevo_codigo_libro = input("NUEVO-> CÓDIGO: ")
                    nuevo_titulo = input("NUEVO-> TÍTULO: ")
                    nuevo_año = input("NUEVO-> AÑO: ")
                    nuevo_tomo = input("NUEVO-> TOMO: ")

                    # Mostrar categorías disponibles
                    categorias = Categoria.obtener_categorias()
                    print("CATEGORÍAS DISPONIBLES:")
                    for j, categoria in enumerate(categorias):
                        print(f"{j + 1}. {categoria.cod_categoria} - {categoria.categoria}")

                    categoria_index = int(input("Seleccione el número de la nueva categoría: ")) - 1
                    nueva_categoria_elegida = categorias[categoria_index]

                    agregar_autor = input("¿Desea agregar un autor? (S/N): ")
                    if agregar_autor.upper() == "S":
                        # Mostrar autores disponibles
                        with open("autores.txt", "r") as autor_file:
                            autores_disponibles = [line.strip() for line in autor_file.readlines() if line.startswith("NOMBRE:")]

                        if autores_disponibles:
                            print("AUTORES DISPONIBLES:")
                            for k, autor in enumerate(autores_disponibles):
                                print(f"{k + 1}. {autor.split(': ')[1]}")
                            autor_index = int(input("Seleccione el número del nuevo autor: ")) - 1
                            nuevo_autor_elegido = autores_disponibles[autor_index].split(': ')[1]
                        else:
                            print("No hay autores disponibles.")
                            nuevo_autor_elegido = input("Ingrese el nombre del nuevo autor: ")
                    else:
                        nuevo_autor_elegido = "Anónimo"

                    # Actualizar los datos del libro en las líneas
                    updated_lines.append(f"CÓDIGO: {nuevo_codigo_libro}\n")
                    updated_lines.append(f"TÍTULO: {nuevo_titulo}\n")
                    updated_lines.append(f"AÑO: {nuevo_año}\n")
                    updated_lines.append(f"TOMO: {nuevo_tomo}\n")
                    updated_lines.append(f"AUTOR: {nuevo_autor_elegido}\n")
                    updated_lines.append(f"CATEGORÍA: {nueva_categoria_elegida.categoria}\n")
                    updated_lines.append(f"COD_CATEGORIA: {nueva_categoria_elegida.cod_categoria}\n")
                    updated_lines.append("================================\n")
                    i += 8  # Saltar las líneas del libro que hemos actualizado
                else:
                    updated_lines.append(line)
                    i += 1

            if not found:
                print("No se encontró ningún libro con ese código.")

            # Escribir las líneas actualizadas en el archivo
            with open("REPORTE_LIBROS.txt", "w") as file:
                file.writelines(updated_lines)
            print("Libro editado exitosamente.")
        except Exception as e:
            print(f"Error al editar libro: {e}")

    @staticmethod
    def eliminar_libro():
        """
        Permite al usuario eliminar un libro existente del archivo "REPORTE_LIBROS.txt" mediante su código.
        Busca el libro por su código, lo elimina y guarda los cambios en el archivo.

        - Parámetros: Ninguno.
        - Retorno: Ninguno.
        - Excepciones: Puede generar excepciones si ocurre algún error durante la ejecución.
        """
        try:
            codigo_libro = input("Ingrese el código del libro que desea eliminar: ")

            with open("REPORTE_LIBROS.txt", "r") as file:
                lines = file.readlines()

            found = False
            updated_lines = []

            i = 0
            while i < len(lines):
                line = lines[i]
                if line.startswith("CÓDIGO:") and line.strip().split(": ")[1] == codigo_libro:
                    found = True
                    print("Libro encontrado y eliminado.")
                    i += 8  # Saltar las líneas del libro que estamos eliminando
                else:
                    updated_lines.append(line)
                    i += 1

            if not found:
                print("No se encontró ningún libro con ese código.")

            # Escribir las líneas actualizadas en el archivo, lo que efectivamente elimina el libro
            with open("REPORTE_LIBROS.txt", "w") as file:
                file.writelines(updated_lines)
        except Exception as e:
            print(f"Error al eliminar libro: {e}")
