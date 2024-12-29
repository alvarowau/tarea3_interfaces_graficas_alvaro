from model.tipo_reserva import TipoReserva
from bbdd.data_base_manager import DatabaseManager
from dao.queries.tipo_reservas_queries import MYSQL_QUERIES, SQLITE_QUERIES

class TipoReservaDAO:
    """
    Clase que gestiona las operaciones de base de datos relacionadas con los tipos de reserva.
    """

    def __init__(self, data_manager: DatabaseManager):
        """
        Inicializa la clase con el `DatabaseManager` para gestionar la conexión y consultas de base de datos.

        Parámetros:
            data_manager (DatabaseManager): Instancia de `DatabaseManager` que gestiona la conexión
                                            a la base de datos.
        """
        self.data_base_manager = data_manager
        self.connection = self.data_base_manager.connection
        self.db_type = self.data_base_manager.db_type
        self.queries = MYSQL_QUERIES if self.db_type == 'mysql' else SQLITE_QUERIES

    def get_all_tipo_reservas(self):
        """
        Obtiene todos los tipos de reserva de la base de datos.

        Devuelve:
            list: Una lista de objetos `TipoReserva` con todos los tipos de reserva, o una lista vacía
                  si ocurre un error al recuperar los datos.
        """
        if self.connection:
            try:
                cursor = self.data_base_manager.get_cursor()
                cursor.execute(self.queries['get_all_tipo_reservas'])
                rows = cursor.fetchall()
                tipo_reservas = [TipoReserva(*row) for row in rows]
                cursor.close()
                return tipo_reservas
            except Exception as e:
                return []
        else:
            return None

    def get_tipo_reservas_by_id(self, tipo_reserva_id):
        """
        Obtiene un tipo de reserva por su ID.

        Parámetros:
            tipo_reserva_id (int): El ID del tipo de reserva que se desea obtener.

        Devuelve:
            TipoReserva: Un objeto `TipoReserva` si se encuentra el tipo de reserva, o `None` si no
                         se encuentra o ocurre un error.
        """
        if self.connection:
            try:
                cursor = self.data_base_manager.get_cursor()
                cursor.execute(self.queries['get_tipo_reservas_by_id'], (tipo_reserva_id,))
                row = cursor.fetchone()
                cursor.close()
                if row:
                    return TipoReserva(*row)
                return None
            except Exception as e:
                return None
        else:
            return None

    def verificar_tabla(self):
        """
        Verifica si la tabla existe en la base de datos.

        Devuelve:
            bool: True si la tabla existe, False en caso contrario, o `None` si ocurre un error.
        """
        if self.connection:
            try:
                cursor = self.data_base_manager.get_cursor()
                cursor.execute(self.queries['existe_tabla'])
                rows = cursor.fetchone()
                cursor.close()
                return rows
            except Exception as e:
                return None
        else:
            return None

    def describe_tablas(self):
        """
        Obtiene la descripción de la tabla.

        Devuelve:
            list: Una lista con la descripción de las tablas si la consulta es exitosa, o `None` si
                  ocurre un error.
        """
        if self.connection:
            try:
                cursor = self.data_base_manager.get_cursor()
                cursor.execute(self.queries['describe_tabla'])
                rows = cursor.fetchall()
                cursor.close()
                return rows
            except Exception as e:
                return None
        else:
            return None

    def existe_congreso(self):
        """
        Verifica si existe un congreso en la base de datos.

        Devuelve:
            bool: True si existe un congreso, False si no, o `None` si ocurre un error.
        """
        if self.connection:
            try:
                cursor = self.data_base_manager.get_cursor()
                cursor.execute(self.queries['existe_congreso'])
                rows = cursor.fetchone()
                cursor.close()
                return rows[0] if rows else None
            except Exception as e:
                return None
        else:
            return None
