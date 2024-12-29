from config.configuracion_base_datos import ConfiguracionBaseDatos
from config.configuracion_sqlite import ConfiguracionSqlite

class UtilConfigSqliteDatos(ConfiguracionBaseDatos):
    """
    Clase para gestionar la configuración de SQLite.

    Esta clase hereda de `ConfiguracionBaseDatos` y permite cargar y actualizar
    la configuración de SQLite desde un archivo JSON. También valida que la configuración
    contenga las claves necesarias.

    Atributos:
        REQUIRED_KEYS (set): Conjunto de claves requeridas para la configuración de SQLite.
        current_config (ConfiguracionSqlite): Objeto que almacena la configuración actual de SQLite.

    Métodos:
        load(): Carga la configuración de SQLite y crea un objeto `ConfiguracionSqlite`.
        update(): Actualiza la configuración de SQLite utilizando un objeto `ConfiguracionSqlite`.
        _validate_config(): Valida que la configuración contenga las claves requeridas.
    """
    REQUIRED_KEYS = {"file_path"}

    def __init__(self, file_path="file_configuracion/bbdd.json"):
        """
        Inicializa la clase con el archivo de configuración especificado.

        Parámetros:
            file_path (str): Ruta del archivo JSON que contiene la configuración de la base de datos.
        """
        super().__init__(file_path)
        self.current_config = None

    def load(self):
        """
        Carga la configuración de SQLite y crea un objeto `ConfiguracionSqlite`.

        Retorna:
            Tuple[bool, Union[None, str]]: `True` si la carga fue exitosa, `False` y un mensaje de error en caso contrario.
        """
        config, error = self.cargar_configuracion("sqlite")
        if error:
            return False, error

        if not self._validate_config(config):
            return False, "Error: La configuración de SQLite no contiene las claves requeridas."

        self.current_config = ConfiguracionSqlite.desde_diccionario(config)
        return True, None

    def update(self, new_config_obj: ConfiguracionSqlite):
        """
        Actualiza la configuración de SQLite utilizando un objeto `ConfiguracionSqlite`.

        Parámetros:
            new_config_obj (ConfiguracionSqlite): Objeto con la nueva configuración de SQLite.

        Retorna:
            Tuple[bool, Union[None, str]]: `True` si la actualización fue exitosa, `False` y un mensaje de error en caso contrario.
        """
        if not isinstance(new_config_obj, ConfiguracionSqlite):
            return False, "Error: El nuevo valor debe ser un objeto `ConfiguracionSqlite`."

        new_config_dict = new_config_obj.a_diccionario()

        if not self._validate_config(new_config_dict):
            return False, "Error: Las claves no coinciden con las requeridas."

        success, message = self._actualizar_configuracion("sqlite", new_config_dict)
        if success:
            self.current_config = new_config_obj
        return success, message

    def _validate_config(self, config):
        """
        Valida que la configuración contenga las claves requeridas.

        Parámetros:
            config (dict): Diccionario con la configuración de SQLite.

        Retorna:
            bool: `True` si la configuración contiene las claves requeridas, `False` en caso contrario.
        """
        if not isinstance(config, dict):
            return False
        return self.REQUIRED_KEYS <= set(config.keys())
