from PySide6.QtWidgets import QFileDialog, QMainWindow, QMessageBox
from bbdd.data_base_manager import DatabaseManager
from PySide6.QtCore import Signal, QObject
from files_ui.ui_window_edit_conexion import Ui_windows_conec
from config.configuracion_base_datos import ConfiguracionBaseDatos
from controller.edit_bbdd_controler import Controller
from util.comprobaciones_tablas_base_datos import test_tablas_base_datos
from controller.window_main_principal_controller import ControladorReservas
from bbdd.config_mysql import test_bbdd_mysql
from bbdd.config_sqlite import test_bbdd_sqlite
from dao.reserva_dao import ReservaDAO
from dao.salon_dao import SalonDAO
from dao.tipo_cocina_dao import TipoCocinaDAO
from dao.tipo_reserva_dao import TipoReservaDAO
from util.mostrar_mensajes import mostrar_error, mostrar_informacion, mostrar_advertencia
from PySide6.QtCore import Qt

class ControladorEditWindows(QMainWindow):
    """
    Controlador encargado de gestionar la configuración de la base de datos.
    Permite conectar, verificar y modificar las conexiones a MySQL y SQLite.
    """
    configuracion_exitosa = Signal(dict)

    def __init__(self):
        """
        Inicializa el controlador de la ventana de configuración de la base de datos.
        Conecta los botones para establecer la conexión y modificar la configuración.
        """
        super().__init__()
        self.ui = Ui_windows_conec()
        self.ui.setupUi(self)
        self.setWindowTitle("Selector base datos")
        self.daos = None
        self.config_database = ConfiguracionBaseDatos()
        self.config_mysql = None
        self.config_sqlite = None
        self.verificar_conexiones_guardadas()

        self.ui.a_button_app.clicked.connect(self.conectar_base_datos)
        self.ui.a_button_conec.clicked.connect(self.modificar_conexion)

    def cargar_daos(self, base_datos):
        """
        Cargar los DAOs necesarios para la conexión a la base de datos.

        Args:
            base_datos (str): El tipo de base de datos ("mysql" o "sqlite").

        Returns:
            dict: Un diccionario con los DAOs para interactuar con las tablas de la base de datos.
            None si ocurre algún error al cargar los DAOs.
        """
        config_database = ConfiguracionBaseDatos()
        config, err = config_database.cargar_configuracion(base_datos)
        if err:
            mostrar_error("Error al cargar la configuración de la base de datos.")
            return None

        conexion = self.crear_conexion(base_datos, config)
        if conexion:
            return self.crear_daos(conexion)
        else:
            mostrar_error("No se han podido crear los DAOs")
            return None

    def crear_conexion(self, base_datos, config):
        """
        Crear una conexión a la base de datos según el tipo.

        Args:
            base_datos (str): El tipo de base de datos ("mysql" o "sqlite").
            config (dict): La configuración de la base de datos.

        Returns:
            DatabaseManager: Una instancia de la clase DatabaseManager configurada para la base de datos especificada.
            None si no se puede crear la conexión.
        """
        if base_datos == "mysql":
            return DatabaseManager("mysql", **config)
        elif base_datos == "sqlite":
            return DatabaseManager("sqlite", **config)
        return None

    def crear_daos(self, conexion):
        """
        Crear los DAOs para interactuar con las tablas de la base de datos.

        Args:
            conexion (DatabaseManager): La conexión a la base de datos.

        Returns:
            dict: Un diccionario con las instancias de los DAOs.
        """
        reserva_dao = ReservaDAO(conexion)
        tipo_cocina_dao = TipoCocinaDAO(conexion)
        tipo_reserva_dao = TipoReservaDAO(conexion)
        salon_dao = SalonDAO(conexion)
        return {
            "reserva_dao": reserva_dao,
            "tipo_cocina_dao": tipo_cocina_dao,
            "tipo_reserva_dao": tipo_reserva_dao,
            "salon_dao": salon_dao
        }

    def conectar_base_datos(self):
        """
        Iniciar la conexión según la base de datos seleccionada por el usuario.
        Verifica qué opción de base de datos está seleccionada y establece la conexión.
        """
        if self.ui.a_radioButton_mysql.isChecked():
            self.probar_conexion("mysql", self.config_mysql, test_bbdd_mysql)
        elif self.ui.a_radioButton_sqlite.isChecked():
            self.probar_conexion("sqlite", self.config_sqlite, test_bbdd_sqlite)
        else:
            mostrar_advertencia("Selecciona una base de datos primero.", "Marca una opción")

    def probar_conexion(self, tipo_bbdd, config, funcion_prueba):
        """
        Probar la conexión a la base de datos utilizando la configuración y función de prueba correspondientes.

        Args:
            tipo_bbdd (str): El tipo de base de datos ("mysql" o "sqlite").
            config (dict): La configuración de la base de datos.
            funcion_prueba (function): La función que realiza la prueba de conexión.

        """
        if config:
            exito, err = funcion_prueba(config)
            if exito:
                daos_dict = self.cargar_daos(tipo_bbdd)
                if daos_dict:
                    exito_tablas, errores = test_tablas_base_datos(
                        tipo_cocina_dao=daos_dict["tipo_cocina_dao"],
                        tipo_reserva_dao=daos_dict["tipo_reserva_dao"],
                        salon_dao=daos_dict["salon_dao"],
                        reserva_dao=daos_dict["reserva_dao"]
                    )
                    mostrar_advertencia(f"Conexión exitosa con la base de datos {tipo_bbdd.capitalize()}")

                    # Emitir los DAOs a la vista principal (main.py)
                    self.configuracion_exitosa.emit(daos_dict)

                    # Cerrar la ventana de configuración después de mostrar la ventana principal
                    self.hide()
                else:
                    mostrar_error("Error al cargar los DAOs.")
            else:
                mostrar_error(f"No se pudo conectar con la base de datos {tipo_bbdd.capitalize()}: {err}")
        else:
            mostrar_error(f"No se puede acceder a la configuración de {tipo_bbdd.capitalize()}")

    def verificar_conexiones_guardadas(self):
        """
        Verifica las conexiones guardadas de MySQL y SQLite.
        Establece el color de los indicadores de conexión según el estado de la conexión.
        """
        config_mysql = self.recuperar_conexion_mysql()
        config_sqlite = self.recuperar_conexion_sqlite()

        self.actualizar_color_conexion_mysql(self.test_conexion(config_mysql, test_bbdd_mysql))
        self.actualizar_color_conexion_sqlite(self.test_conexion(config_sqlite, test_bbdd_sqlite))

    def test_conexion(self, config, funcion_prueba):
        """
        Probar una conexión a la base de datos utilizando una configuración y función de prueba.

        Args:
            config (dict): La configuración de la base de datos.
            funcion_prueba (function): La función que realiza la prueba de conexión.

        Returns:
            bool: True si la conexión es exitosa, False en caso contrario.
        """
        if config:
            exito, err = funcion_prueba(config)
            return exito
        return False

    def recuperar_conexion_sqlite(self):
        """
        Recupera la configuración de conexión SQLite.

        Returns:
            dict: La configuración de conexión SQLite, o None si no se puede recuperar.
        """
        return self.recuperar_conexion("sqlite")

    def recuperar_conexion_mysql(self):
        """
        Recupera la configuración de conexión MySQL.

        Returns:
            dict: La configuración de conexión MySQL, o None si no se puede recuperar.
        """
        return self.recuperar_conexion("mysql")

    def recuperar_conexion(self, tipo_bbdd):
        """
        Recupera la configuración de conexión de una base de datos específica.

        Args:
            tipo_bbdd (str): El tipo de base de datos ("mysql" o "sqlite").

        Returns:
            dict: La configuración de conexión, o None si ocurre algún error.
        """
        config, err = self.config_database.cargar_configuracion(tipo_bbdd)
        if config:
            setattr(self, f"config_{tipo_bbdd}", config)
            return config
        else:
            mostrar_error(f"No se pudo recuperar datos de {tipo_bbdd}", str(err))
            return None

    def actualizar_color_conexion_mysql(self, exito_conexion: bool):
        """
        Establece el color de la conexión MySQL en la interfaz gráfica.

        Args:
            exito_conexion (bool): Indica si la conexión fue exitosa o no.
        """
        self.actualizar_color_conexion(self.ui.a_label_color_mysql, exito_conexion)

    def actualizar_color_conexion_sqlite(self, exito_conexion: bool):
        """
        Establece el color de la conexión SQLite en la interfaz gráfica.

        Args:
            exito_conexion (bool): Indica si la conexión fue exitosa o no.
        """
        self.actualizar_color_conexion(self.ui.a_label_color_sqlite, exito_conexion)

    def actualizar_color_conexion(self, etiqueta, exito_conexion: bool):
        """
        Establece el color de la conexión en el indicador correspondiente.

        Args:
            etiqueta (QLabel): El widget QLabel que muestra el estado de la conexión.
            exito_conexion (bool): Indica si la conexión fue exitosa o no.
        """
        color = "green" if exito_conexion else "red"
        etiqueta.setStyleSheet(f"background-color: {color};")

    def modificar_conexion(self):
        """
        Permite modificar la configuración de la conexión a la base de datos.
        Abre una ventana para editar la configuración de conexión.
        """
        ventana_editar_conexion = Controller()
        ventana_editar_conexion.exec()
        self.verificar_conexiones_guardadas()
