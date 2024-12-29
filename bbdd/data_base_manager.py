from bbdd.mysql_conection import MySQLConnection
from bbdd.sqlite_conection import SQLiteConnection

class DatabaseManager:
    """
    Gestiona la conexión a una base de datos, ya sea MySQL o SQLite.

    Dependiendo del tipo de base de datos especificado al crear una instancia,
    establece una conexión con la base de datos correspondiente y permite ejecutar
    consultas mediante un cursor.

    Atributos:
        connection_type (str): Tipo de base de datos ('mysql' o 'sqlite').
        connection (MySQLConnection or SQLiteConnection): Instancia de conexión a la base de datos.
        db_type (str): Tipo de base de datos ('mysql' o 'sqlite').

    Métodos:
        connect(): Establece la conexión a la base de datos.
        get_cursor(): Devuelve un cursor para ejecutar consultas en la base de datos.
        close(): Cierra la conexión a la base de datos.
    """
    def __init__(self, connection_type, **kwargs):
        """
        Inicializa el gestor de base de datos, creando una conexión dependiendo
        del tipo de base de datos proporcionado.

        Parámetros:
            connection_type (str): Tipo de base de datos ('mysql' o 'sqlite').
            **kwargs: Parámetros adicionales para configurar la conexión.
                      - Para MySQL: 'host', 'port', 'user', 'password', 'database'.
                      - Para SQLite: 'file_path'.

        Excepciones:
            ValueError: Si el tipo de conexión no es 'mysql' ni 'sqlite'.
        """
        self.connection_type = connection_type
        self.connection = None
        self.db_type = None

        if self.connection_type == 'mysql':
            self.connection = MySQLConnection(
                host=kwargs.get('host'),
                port=kwargs.get('port'),
                user=kwargs.get('user'),
                password=kwargs.get('password'),
                database=kwargs.get('database')
            )
            self.db_type = 'mysql'

        elif self.connection_type == 'sqlite':
            self.connection = SQLiteConnection(
                db_path=kwargs.get('file_path')
            )
            self.db_type = 'sqlite'
        else:
            raise ValueError("Tipo de conexión no soportado")

        self.connect()

    def connect(self):
        """
        Establece la conexión con la base de datos dependiendo del tipo de conexión.

        Si la conexión es válida, establece la conexión con la base de datos.
        """
        if self.connection:
            self.connection.connect()

    def get_cursor(self):
        """
        Devuelve un cursor para ejecutar consultas en la base de datos.

        Retorna:
            cursor: Un objeto cursor para interactuar con la base de datos.

        Excepciones:
            ValueError: Si la conexión no está establecida correctamente.
        """
        if self.connection:
            return self.connection.get_cursor()
        else:
            raise ValueError("La conexión no está establecida correctamente.")

    def close(self):
        """
        Cierra la conexión con la base de datos.

        Asegura que la conexión se cierre de forma adecuada cuando ya no se necesite.
        """
        if self.connection:
            self.connection.close()
