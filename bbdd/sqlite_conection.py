import sqlite3

class SQLiteConnection:
    """
    Gestiona la conexión a una base de datos SQLite.

    Esta clase permite establecer una conexión con una base de datos SQLite,
    obtener un cursor para ejecutar consultas y cerrar la conexión.

    Atributos:
        db_path (str): Ruta del archivo de la base de datos SQLite.
        connection (sqlite3.Connection): Instancia de conexión con SQLite.

    Métodos:
        connect(): Establece la conexión con la base de datos SQLite.
        get_cursor(): Devuelve un cursor para ejecutar consultas.
        close(): Cierra la conexión con la base de datos SQLite.
        commit(): Confirma una transacción en la base de datos.
    """
    def __init__(self, db_path: str):
        """
        Inicializa la clase con la ruta del archivo de la base de datos SQLite.

        Parámetros:
            db_path (str): Ruta del archivo de la base de datos SQLite.
        """
        self.db_path = db_path
        self.connection = None

    def connect(self):
        """
        Establece la conexión con la base de datos SQLite.

        Esta función crea una conexión con la base de datos SQLite utilizando
        la ruta proporcionada.

        Si la conexión ya está establecida, no hará nada.

        Excepciones:
            sqlite3.Error: Si ocurre un error al intentar conectar con SQLite.
        """
        if not self.connection:
            self.connection = sqlite3.connect(self.db_path)
            print("Conexión establecida con SQLite.")

    def get_cursor(self):
        """
        Devuelve un cursor para ejecutar consultas en la base de datos SQLite.

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
        Cierra la conexión con la base de datos SQLite.

        Asegura que la conexión se cierre de forma adecuada cuando ya no se necesite.
        """
        if self.connection:
            self.connection.close()
            print("Conexión cerrada.")

    def commit(self):
        """
        Confirma la transacción actual en la base de datos SQLite.

        Esto guarda los cambios realizados en la base de datos. Es necesario llamar
        a este método para que las modificaciones sean persistentes.

        Excepciones:
            ValueError: Si la conexión no está establecida correctamente.
        """
        if self.connection:
            self.connection.commit()  # Confirmar la transacción
        else:
            raise ValueError("La conexión no está establecida correctamente.")
