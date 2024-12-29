from datetime import date

class Reserva:
    """
    Clase que representa una reserva en el sistema.

    Esta clase contiene todos los detalles relacionados con una reserva, como el ID de la reserva,
    tipo de reserva, salon asignado, tipo de cocina, persona responsable, teléfono, fecha de la reserva,
    ocupación, jornadas y habitaciones (si aplica).

    Atributos:
        reserva_id (int): ID único de la reserva.
        tipo_reserva_id (int): ID que representa el tipo de reserva.
        salon_id (int): ID del salón asignado a la reserva.
        tipo_cocina_id (int): ID del tipo de cocina asignado a la reserva.
        persona (str): Nombre de la persona que hizo la reserva.
        telefono (str): Número de teléfono de la persona responsable de la reserva.
        fecha (date): Fecha de la reserva.
        ocupacion (int): Número de personas ocupando la reserva.
        jornadas (int): Número de jornadas o días que dura la reserva.
        habitaciones (int, opcional): Número de habitaciones asignadas a la reserva (por defecto 0).

    Métodos:
        __repr__(): Devuelve una representación en cadena de la reserva, mostrando el ID, el nombre de la persona
                    y la fecha de la reserva.
    """

    def __init__(
        self,
        reserva_id: int,
        tipo_reserva_id: int,
        salon_id: int,
        tipo_cocina_id: int,
        persona: str,
        telefono: str,
        fecha: date,
        ocupacion: int,
        jornadas: int,
        habitaciones: int = 0
    ) -> None:
        """
        Inicializa los atributos de la clase Reserva.

        Parámetros:
            reserva_id (int): ID único de la reserva.
            tipo_reserva_id (int): ID que representa el tipo de reserva.
            salon_id (int): ID del salón asignado a la reserva.
            tipo_cocina_id (int): ID del tipo de cocina asignado a la reserva.
            persona (str): Nombre de la persona que hizo la reserva.
            telefono (str): Número de teléfono de la persona responsable de la reserva.
            fecha (date): Fecha de la reserva.
            ocupacion (int): Número de personas ocupando la reserva.
            jornadas (int): Número de jornadas o días que dura la reserva.
            habitaciones (int, opcional): Número de habitaciones asignadas a la reserva (por defecto 0).
        """
        if isinstance(fecha, str):
            self.fecha = date.fromisoformat(fecha)  # Convierte la fecha del formato string a date
        else:
            self.fecha = fecha  # Asumimos que ya es un objeto `date` si no es string

        self.reserva_id = reserva_id
        self.tipo_reserva_id = tipo_reserva_id
        self.salon_id = salon_id
        self.tipo_cocina_id = tipo_cocina_id
        self.persona = persona
        self.telefono = telefono
        self.ocupacion = ocupacion
        self.jornadas = jornadas
        self.habitaciones = habitaciones

    def __repr__(self) -> str:
        """
        Devuelve una representación en cadena de la reserva.

        Retorna:
            str: Una cadena con la representación de la reserva, mostrando el ID, el nombre de la persona
                 responsable y la fecha de la reserva.
        """
        return f"Reserva({self.reserva_id}, {self.persona}, {self.fecha})"
