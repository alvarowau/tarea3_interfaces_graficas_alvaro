from model.tipo_cocina import TipoCocina
from bbdd.data_base_manager import DatabaseManager
from dao.queries.tipo_cocina_queries import MYSQL_QUERIES, SQLITE_QUERIES

class TipoCocinaDAO:
    """
    Clase que gestiona las operaciones de base de datos relacionadas con los tipos de cocina.
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

    def get_all_tipo_cocinas(self):
        """
        Obtiene todos los tipos de cocina de la base de datos.

        Retorna:
            list: Una lista de objetos `TipoCocina` con los datos de todos los tipos de cocina.
            En caso de error, retorna una lista vacía.

        Excepciones:
            Exception: Si ocurre un error durante la ejecución de la consulta.
        """
        if self.connection:
            try:
                cursor = self.data_base_manager.get_cursor()
                cursor.execute(self.queries['get_all_cocinas'])
                rows = cursor.fetchall()
                tipo_cocinas = [TipoCocina(*row) for row in rows]
                cursor.close()
                return tipo_cocinas
            except Exception as e:
                return []
        else:
            return None

    def get_tipo_cocina_by_id(self, tipo_cocina_id):
        """
        Obtiene un tipo de cocina por su ID.

        Parámetros:
            tipo_cocina_id (int): El ID del tipo de cocina a obtener.

        Retorna:
            TipoCocina: Objeto `TipoCocina` con los datos del tipo de cocina si se encuentra.
            None: Si no se encuentra ningún tipo de cocina con ese ID.

        Excepciones:
            Exception: Si ocurre un error durante la ejecución de la consulta.
        """
        if self.connection:
            try:
                cursor = self.data_base_manager.get_cursor()
                cursor.execute(self.queries['get_cocina_by_id'], (tipo_cocina_id,))
                row = cursor.fetchone()
                cursor.close()
                if row:
                    return TipoCocina(*row)
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
