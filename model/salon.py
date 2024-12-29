class Salon:
    """
    Clase que representa un salón en el sistema.

    Esta clase contiene los detalles básicos de un salón, como su ID único y su nombre.

    Atributos:
        salon_id (int): ID único del salón.
        nombre (str): Nombre del salón.

    Métodos:
        __repr__(): Devuelve una representación en cadena del salón, mostrando su ID y nombre.
    """

    def __init__(self, salon_id: int, nombre: str) -> None:
        """
        Inicializa los atributos de la clase Salon.

        Parámetros:
            salon_id (int): ID único del salón.
            nombre (str): Nombre del salón.
        """
        self.salon_id: int = salon_id
        self.nombre: str = nombre

    def __repr__(self) -> str:
        """
        Devuelve una representación en cadena del salón.

        Retorna:
            str: Una cadena con la representación del salón, mostrando el ID y el nombre del salón.
        """
        return f"Salon({self.salon_id}, {self.nombre})"
