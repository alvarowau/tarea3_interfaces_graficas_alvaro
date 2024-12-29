class ConfiguracionMysql:
    """
    Clase que representa la configuración de una base de datos MySQL.

    Atributos:
        host (str): Dirección del servidor MySQL.
        puerto (int): Puerto del servidor MySQL.
        usuario (str): Usuario para la autenticación.
        contrasena (str): Contraseña del usuario.
        base_datos (str): Nombre de la base de datos.

    Métodos:
        a_diccionario(): Convierte el objeto a un diccionario.
        desde_diccionario(datos): Crea un objeto `ConfiguracionMysql` a partir de un diccionario.
    """
    def __init__(self, host=None, puerto=None, usuario=None, contrasena=None, base_datos=None):
        self.host = host
        self.puerto = puerto
        self.usuario = usuario
        self.contrasena = contrasena
        self.base_datos = base_datos

    def a_diccionario(self):
        """Convierte el objeto a un diccionario."""
        return {
            "host": self.host,
            "port": self.puerto,
            "user": self.usuario,
            "password": self.contrasena,
            "database": self.base_datos,
        }

    @classmethod
    def desde_diccionario(cls, datos):
        """Crea un objeto `ConfiguracionMysql` a partir de un diccionario."""
        return cls(
            host=datos.get("host"),
            puerto=datos.get("port"),
            usuario=datos.get("user"),
            contrasena=datos.get("password"),
            base_datos=datos.get("database"),
        )
