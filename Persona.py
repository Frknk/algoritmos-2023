class Persona:
    """
    Clase que representa a una persona.
    """

    def __init__(self, cod_persona, nombre, apellido_paterno, apellido_materno, fecha_nacimiento):
        """
        Constructor de la clase Persona.

        Args:
            cod_persona (str): Código único de la persona.
            nombre (str): Nombre de la persona.
            apellido_paterno (str): Apellido paterno de la persona.
            apellido_materno (str): Apellido materno de la persona.
            fecha_nacimiento (str): Fecha de nacimiento de la persona en formato YYYY-MM-DD.
        """
        self.cod_persona = cod_persona
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.fecha_nacimiento = fecha_nacimiento
