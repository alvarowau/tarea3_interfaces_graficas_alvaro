class TipoReserva:
    """
    Clase que representa un tipo de reserva en el sistema.

    Esta clase contiene detalles sobre el tipo de reserva, como su ID único, su nombre,
    y si requiere jornadas u habitaciones adicionales.

    Atributos:
        tipo_reserva_id (int): ID único del tipo de reserva.
        nombre (str): Nombre del tipo de reserva.
        requiere_jornadas (bool): Indica si el tipo de reserva requiere jornadas adicionales (por defecto False).
        requiere_habitaciones (bool): Indica si el tipo de reserva requiere habitaciones adicionales (por defecto False).

    Métodos:
        __repr__(): Devuelve una representación en cadena del tipo de reserva, mostrando su ID y nombre.
    """

    def __init__(
        self,
        tipo_reserva_id: int,
        nombre: str,
        requiere_jornadas: bool = False,
        requiere_habitaciones: bool = False
    ) -> None:
        """
        Inicializa los atributos de la clase TipoReserva.

        Parámetros:
            tipo_reserva_id (int): ID único del tipo de reserva.
            nombre (str): Nombre del tipo de reserva.
            requiere_jornadas (bool): Indica si el tipo de reserva requiere jornadas adicionales (por defecto False).
            requiere_habitaciones (bool): Indica si el tipo de reserva requiere habitaciones adicionales (por defecto False).
        """
        self.tipo_reserva_id: int = tipo_reserva_id
        self.nombre: str = nombre
        self.requiere_jornadas: bool = requiere_jornadas
        self.requiere_habitaciones: bool = requiere_habitaciones

    def __repr__(self) -> str:
        """
        Devuelve una representación en cadena del tipo de reserva.

        Retorna:
            str: Una cadena con la representación del tipo de reserva, mostrando su ID y nombre.
        """
        return f"TipoReserva({self.tipo_reserva_id}, {self.nombre})"
