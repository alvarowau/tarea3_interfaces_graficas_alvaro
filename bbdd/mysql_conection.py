import mysql.connector

class MySQLConnection:
    """
    Gestiona la conexión a una base de datos MySQL.

    Esta clase permite establecer una conexión con una base de datos MySQL,
    obtener un cursor para ejecutar consultas y cerrar la conexión.

    Atributos:
        host (str): Dirección del host del servidor MySQL.
        port (int): Puerto del servidor MySQL.
        user (str): Usuario para la autenticación.
        password (str): Contraseña del usuario.
        database (str): Nombre de la base de datos a la que conectarse.
        connection (mysql.connector.connection.MySQLConnection): Instancia de conexión con MySQL.

    Métodos:
        connect(): Establece la conexión con el servidor MySQL.
        get_cursor(): Devuelve un cursor para ejecutar consultas.
        close(): Cierra la conexión con el servidor MySQL.
        commit(): Confirma una transacción en la base de datos.
    """
    def __init__(self, host: str, port: int, user: str, password: str, database: str):
        """
        Inicializa la clase con los parámetros necesarios para conectar a la base de datos MySQL.

        Parámetros:
            host (str): Dirección del servidor MySQL.
            port (int): Puerto del servidor MySQL.
            user (str): Nombre de usuario para la autenticación.
            password (str): Contraseña del usuario.
            database (str): Nombre de la base de datos a la que conectarse.
        """
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        """
        Establece la conexión con el servidor MySQL utilizando los parámetros proporcionados.

        Esta función crea una conexión con la base de datos MySQL utilizando
        el conector `mysql.connector`.

        Excepciones:
            mysql.connector.Error: Si ocurre un error al intentar conectar con MySQL.
        """
        self.connection = mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def get_cursor(self):
        """
        Devuelve un cursor para ejecutar consultas en la base de datos MySQL.

        Retorna:
            cursor: Un objeto cursor que permite ejecutar comandos SQL en la base de datos.

        Excepciones:
            ValueError: Si la conexión no está establecida correctamente.
        """
        if self.connection:
            return self.connection.cursor()
        else:
            raise ValueError("La conexión no está establecida correctamente.")

    def close(self):
        """
        Cierra la conexión con el servidor MySQL.

        Asegura que la conexión se cierre de forma adecuada cuando ya no se necesite.
        """
        if self.connection:
            self.connection.close()
            print("Conexión cerrada.")

    def commit(self):
        """
        Confirma la transacción actual en la base de datos MySQL.

        Esto guarda los cambios realizados en la base de datos. Es necesario llamar
        a este método para que las modificaciones sean persistentes.

        Excepciones:
            ValueError: Si la conexión no está establecida correctamente.
        """
        if self.connection:
            self.connection.commit()
        else:
            raise ValueError("La conexión no está establecida correctamente.")
