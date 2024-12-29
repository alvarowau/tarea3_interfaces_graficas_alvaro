from model.salon import Salon
from bbdd.data_base_manager import DatabaseManager
from dao.queries.salones_queries import MYSQL_QUERIES, SQLITE_QUERIES

class SalonDAO:
    """
    Clase que gestiona las operaciones de base de datos relacionadas con los salones.
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

    def get_all_salones(self):
        """
        Obtiene todos los salones de la base de datos.

        Retorna:
            list: Una lista de objetos `Salon` con los datos de todos los salones.
            En caso de error, retorna una lista vacía.

        Excepciones:
            Exception: Si ocurre un error durante la ejecución de la consulta.
        """
        if self.connection:
            try:
                cursor = self.data_base_manager.get_cursor()
                cursor.execute(self.queries['get_all_salones'])
                rows = cursor.fetchall()
                salones = [Salon(*row) for row in rows]
                cursor.close()
                return salones, None
            except Exception as e:
                return [], f"Error al obtener todos los salones: {e}"
        else:
            return None, "No hay conexión a la base de datos."

    def get_salones_by_id(self, salon_id):
        """
        Obtiene un salón por su ID.

        Parámetros:
            salon_id (int): El ID del salón a obtener.

        Retorna:
            Salon: Objeto `Salon` con los datos del salón si se encuentra.
            None: Si no se encuentra ningún salón con ese ID.

        Excepciones:
            Exception: Si ocurre un error durante la ejecución de la consulta.
        """
        if self.connection:
            try:
                cursor = self.data_base_manager.get_cursor()
                cursor.execute(self.queries['get_salon_by_id'], (salon_id,))
                row = cursor.fetchone()
                cursor.close()
                if row:
                    return Salon(*row)
                return None
            except Exception as e:
                return None
        else:
            return None

    def verificar_tabla(self):
        """
        Verifica si la tabla existe en la base de datos.

        Retorna:
            bool: True si la tabla existe, False si no, o `None` si ocurre un error.
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

        Retorna:
            list: Una lista con la descripción de las tablas si la consulta es exitosa, o `None`
                  si ocurre un error.
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
