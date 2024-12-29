class TipoCocina:
    """
    Clase que representa un tipo de cocina en el sistema.

    Esta clase contiene los detalles básicos de un tipo de cocina, como su ID único y su nombre.

    Atributos:
        tipo_cocina_id (int): ID único del tipo de cocina.
        nombre (str): Nombre del tipo de cocina.

    Métodos:
        __repr__(): Devuelve una representación en cadena del tipo de cocina, mostrando su ID y nombre.
    """

    def __init__(self, tipo_cocina_id: int, nombre: str) -> None:
        """
        Inicializa los atributos de la clase TipoCocina.

        Parámetros:
            tipo_cocina_id (int): ID único del tipo de cocina.
            nombre (str): Nombre del tipo de cocina.
        """
        self.tipo_cocina_id: int = tipo_cocina_id
        self.nombre: str = nombre

    def __repr__(self) -> str:
        """
        Devuelve una representación en cadena del tipo de cocina.

        Retorna:
            str: Una cadena con la representación del tipo de cocina, mostrando su ID y nombre.
        """
        return f"TipoCocina({self.tipo_cocina_id}, {self.nombre})"
