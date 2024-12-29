class ConfiguracionSqlite:
    """
    Clase que representa la configuración de una base de datos SQLite.

    Atributos:
        ruta_archivo_base_datos (str): Ruta al archivo de la base de datos SQLite.

    Métodos:
        a_diccionario(): Convierte el objeto a un diccionario.
        desde_diccionario(datos): Crea un objeto `ConfiguracionSqlite` a partir de un diccionario.
        __str__(): Devuelve una representación en cadena del objeto.
    """
    def __init__(self, ruta_archivo_base_datos=None):
        self.ruta_archivo_base_datos = ruta_archivo_base_datos

    def a_diccionario(self):
        """Convierte el objeto a un diccionario."""
        return {
            "file_path": self.ruta_archivo_base_datos
        }

    @classmethod
    def desde_diccionario(cls, datos):
        """Crea un objeto `ConfiguracionSqlite` a partir de un diccionario."""
        return cls(
            ruta_archivo_base_datos=datos.get("file_path"),
        )

    def __str__(self):
        return f"ConfiguracionSqlite(ruta_archivo_base_datos={self.ruta_archivo_base_datos})"
