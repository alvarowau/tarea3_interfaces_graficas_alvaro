from model.reserva import Reserva
from bbdd.data_base_manager import DatabaseManager
from dao.queries.reservas_queries import MYSQL_QUERIES, SQLITE_QUERIES


class ReservaDAO:
    """
    Clase que gestiona las operaciones de base de datos relacionadas con las reservas.
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

    def _execute_query(self, query_key, params=None, fetch_one=False):
        """
        Método genérico para ejecutar consultas en la base de datos.

        Parámetros:
            query_key (str): La clave que representa la consulta en el diccionario de consultas.
            params (tuple): Los parámetros que se pasan a la consulta, por defecto es `None`.
            fetch_one (bool): Si es `True`, obtiene solo una fila. Si es `False`, obtiene todas las filas.

        Retorna:
            tuple: El resultado de la consulta y un mensaje de error (si ocurre).
        """
        if not self.connection:
            return None, "No hay conexión a la base de datos."

        try:
            cursor = self.data_base_manager.get_cursor()
            cursor.execute(self.queries[query_key], params or ())
            if fetch_one:
                result = cursor.fetchone()
            else:
                result = cursor.fetchall()
            cursor.close()
            return result, None
        except Exception as e:
            return None, f"Error al ejecutar la consulta {query_key}: {e}"

    def _map_to_reservas(self, rows):
        """
        Convierte una lista de filas a una lista de objetos `Reserva`.

        Parámetros:
            rows (list): Lista de filas obtenidas de la base de datos.

        Retorna:
            list: Una lista de objetos `Reserva` correspondientes a las filas.
        """
        return [Reserva(*row) for row in rows]

    def get_all_reservas(self):
        """
        Obtiene todas las reservas de la base de datos.

        Retorna:
            tuple: Una lista de objetos `Reserva` con los datos de todas las reservas y un posible mensaje de error.
        """
        rows, error = self._execute_query('get_all_reservas')
        if error:
            return [], error
        return self._map_to_reservas(rows), None

    def get_reserva_by_id(self, reserva_id):
        """
        Obtiene una reserva por su ID.

        Parámetros:
            reserva_id (int): El ID de la reserva a obtener.

        Retorna:
            tuple: Un objeto `Reserva` con los datos de la reserva si se encuentra, o `None` si no se encuentra.
                   También retorna un mensaje de error si ocurre algún problema.
        """
        row, error = self._execute_query('get_reserva_by_id', (reserva_id,), fetch_one=True)
        if error or not row:
            return None, error or "Reserva no encontrada."
        return Reserva(*row), None

    def add_reserva(self, reserva: Reserva):
        """
        Añade una nueva reserva a la base de datos.

        Parámetros:
            reserva (Reserva): Objeto `Reserva` con los datos de la reserva a añadir.

        Retorna:
            tuple: Un valor booleano que indica si la operación fue exitosa, y un mensaje de éxito o error.
        """
        params = (
            reserva.tipo_reserva_id,
            reserva.salon_id,
            reserva.tipo_cocina_id,
            reserva.persona,
            reserva.telefono,
            reserva.fecha,
            reserva.ocupacion,
            reserva.jornadas,
            reserva.habitaciones,
        )
        _, error = self._execute_query('add_reserva', params)
        if error:
            return False, error
        self.connection.commit()
        return True, "Reserva añadida correctamente."

    def update_reserva(self, reserva: Reserva):
        """
        Actualiza los datos de una reserva en la base de datos.

        Parámetros:
            reserva (Reserva): Objeto `Reserva` con los datos actualizados de la reserva.

        Retorna:
            tuple: Un valor booleano que indica si la operación fue exitosa, y un mensaje de éxito o error.
        """
        params = (
            reserva.tipo_reserva_id,
            reserva.salon_id,
            reserva.tipo_cocina_id,
            reserva.persona,
            reserva.telefono,
            reserva.fecha,
            reserva.ocupacion,
            reserva.jornadas,
            reserva.habitaciones,
            reserva.reserva_id,
        )
        _, error = self._execute_query('update_reserva', params)
        if error:
            return False, error
        self.connection.commit()
        return True, "Reserva actualizada correctamente."

    def delete_reserva(self, reserva_id):
        """
        Elimina una reserva de la base de datos.

        Parámetros:
            reserva_id (int): El ID de la reserva a eliminar.

        Retorna:
            tuple: Un valor booleano que indica si la operación fue exitosa, y un mensaje de éxito o error.
        """
        _, error = self._execute_query('delete_reserva', (reserva_id,))
        if error:
            return False, error
        self.connection.commit()
        return True, "Reserva eliminada correctamente."

    def get_all_reservas_by_salon_id(self, salon_id):
        """
        Obtiene todas las reservas de un salón específico.

        Parámetros:
            salon_id (int): El ID del salón del que obtener las reservas.

        Retorna:
            tuple: Una lista de objetos `Reserva` con las reservas del salón, o un mensaje de error si ocurre uno.
        """
        rows, error = self._execute_query('get_all_reservas_by_salon_id', (salon_id,))
        if error:
            return [], error
        return self._map_to_reservas(rows), None

    def _verificar_tabla(self, query_key):
        """
        Método genérico para verificar si la tabla existe o describir la tabla.

        Parámetros:
            query_key (str): La clave que representa la consulta a ejecutar.

        Retorna:
            result: El resultado de la consulta, que puede ser las filas de la tabla o un error.
        """
        if self.connection:
            try:
                cursor = self.data_base_manager.get_cursor()
                cursor.execute(self.queries[query_key])
                rows = cursor.fetchone() if query_key == 'existe_tabla' else cursor.fetchall()
                cursor.close()
                return rows
            except Exception as e:
                return None
        else:
            return None

    def verificar_tabla(self):
        """
        Verifica si la tabla de reservas existe en la base de datos.

        Retorna:
            result: El resultado de la consulta para verificar la existencia de la tabla.
        """
        return self._verificar_tabla('existe_tabla')

    def describe_tablas(self):
        """
        Obtiene la descripción de las tablas de reservas.

        Retorna:
            result: El resultado de la consulta para describir las tablas.
        """
        return self._verificar_tabla('describe_tabla')
