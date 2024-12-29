from PySide6.QtWidgets import QFileDialog, QDialog

from bbdd.config_mysql import test_bbdd_mysql
from bbdd.config_sqlite import test_bbdd_sqlite
from config.config_mysql import UtilConfigMysqlDatos
from config.config_sqlite import UtilConfigSqliteDatos
from config.configuracion_mysql import ConfiguracionMysql
from config.configuracion_sqlite import ConfiguracionSqlite
from files_ui.edit_bbdd_window import Ui_edit_bbdd_windows
from util.comprobaciones import validar_texto
from util.mostrar_mensajes import mostrar_error, mostrar_informacion


class Controller(QDialog, Ui_edit_bbdd_windows):
    """
    Controlador para la ventana de configuración de bases de datos.

    Maneja la lógica para configurar y probar conexiones a bases de datos MySQL y SQLite.
    """
    configuracion_mysql = UtilConfigMysqlDatos()
    configuracion_sqlite = UtilConfigSqliteDatos()
    datos_config_mysql = ConfiguracionMysql()
    datos_config_sqlite = ConfiguracionSqlite()
    tipo_bbdd_guardada = ""  # Tipo de base de datos guardada: "MYSQL" o "SQLITE"
    datos_config_mysql_modif = ConfiguracionMysql()
    datos_config_sqlite_modif = ConfiguracionSqlite()

    def __init__(self):
        super().__init__()
        self.ui = Ui_edit_bbdd_windows()
        self.ui.setupUi(self)
        self.setWindowTitle("Ventana de Configuración de Base de Datos")
        self.ui.a_button_save.setVisible(False)
        self.cargar_configuracion_mysql()
        self.cargar_configuracion_sqlite()
        self.configurar_botones()

    def mostrar_panel_mysql(self):
        """
        Muestra el panel de configuración para bases de datos MySQL.
        """
        self.tipo_bbdd_guardada = ""
        self.ui.a_button_save.setVisible(False)
        self.actualizar_campos_mysql()
        self.ui.stackedWidget.setCurrentIndex(0)

    def mostrar_panel_sqlite(self):
        """
        Muestra el panel de configuración para bases de datos SQLite.
        """
        self.tipo_bbdd_guardada = ""
        self.ui.a_button_save.setVisible(False)
        self.actualizar_campos_sqlite()
        self.ui.stackedWidget.setCurrentIndex(1)

    def actualizar_campos_sqlite(self):
        """
        Actualiza los campos de la interfaz con la configuración de SQLite actual.

        Muestra un error si no se encuentra la configuración.
        """
        self.ui.a_button_save.setVisible(False)
        if self.datos_config_sqlite:
            self.ui.a_lineEdit_search_file.setText(str(self.datos_config_sqlite.ruta_archivo_base_datos))
        else:
            mostrar_error("No se encontró la configuración de SQLite")

    def seleccionar_archivo_sqlite(self):
        """
        Abre un cuadro de diálogo para seleccionar un archivo SQLite y actualiza el campo correspondiente.
        """
        archivo = QFileDialog.getOpenFileName(
            self, "Buscar Archivo", ".", "SQLite Files (*.sqlite *.db)"
        )
        if archivo[0]:
            self.ui.a_lineEdit_search_file.setText(str(archivo[0]))

    def guardar_cambios(self):
        """
        Guarda los cambios en la configuración de la base de datos seleccionada.

        Muestra un mensaje de error si no se detecta un tipo de base de datos.
        """
        if self.tipo_bbdd_guardada == "MYSQL":
            self.guardar_configuracion_mysql()
        elif self.tipo_bbdd_guardada == "SQLITE":
            self.guardar_configuracion_sqlite()
        else:
            mostrar_error("Error inesperado")
        self.tipo_bbdd_guardada = ""

    def actualizar_campos_mysql(self):
        """
        Actualiza los campos de la interfaz con la configuración de MySQL actual.

        Muestra un error si no se encuentra la configuración.
        """
        self.ui.a_button_save.setVisible(False)
        if self.datos_config_mysql:
            self.ui.a_lineEdit_host.setText(str(self.datos_config_mysql.host))
            self.ui.a_lineEdit_port.setText(str(self.datos_config_mysql.puerto))
            self.ui.a_lineEdit_user.setText(str(self.datos_config_mysql.usuario))
            self.ui.a_lineEdit_password.setText(str(self.datos_config_mysql.contrasena))
            self.ui.a_lineEdit_bbdd.setText(str(self.datos_config_mysql.base_datos))
        else:
            mostrar_error("No se encontró configuración para MySQL.")

    def configurar_botones(self):
        """
        Conecta los botones de la interfaz con sus respectivas funciones.
        """
        self.ui.a_button_mysql.clicked.connect(self.mostrar_panel_mysql)
        self.ui.a_button_sqlite.clicked.connect(self.mostrar_panel_sqlite)
        self.ui.a_button_test.clicked.connect(self.probar_conexion_mysql)
        self.ui.a_button_test_sqlite.clicked.connect(self.probar_conexion_sqlite)
        self.ui.a_pushButton_select_file.clicked.connect(self.seleccionar_archivo_sqlite)
        self.ui.a_button_save.clicked.connect(self.guardar_cambios)

    def probar_conexion_mysql(self):
        """
        Prueba la conexión a la base de datos MySQL con los datos ingresados en la interfaz.

        Muestra un mensaje indicando el éxito o error de la conexión.
        """
        self.ui.a_button_save.setVisible(False)
        success, result = self.obtener_datos_mysql()
        if success:
            if isinstance(result, list):
                self.convertir_lista_a_config_mysql(result)
                success, error = test_bbdd_mysql(self.datos_config_mysql_modif.a_diccionario())
                if success:
                    mostrar_informacion("Test de conexión exitosa")
                    self.ui.a_button_save.setVisible(True)
                    self.tipo_bbdd_guardada = "MYSQL"
                else:
                    mostrar_error(str(error))
        else:
            mostrar_error("Existen campos vacíos")

    def probar_conexion_sqlite(self):
        """
        Prueba la conexión a la base de datos SQLite con los datos ingresados en la interfaz.

        Muestra un mensaje indicando el éxito o error de la conexión.
        """
        self.ui.a_button_save.setVisible(False)
        success, result = self.obtener_datos_sqlite()
        if success:
            success, error = test_bbdd_sqlite({"file_path": result})
            if success:
                self.datos_config_sqlite_modif = ConfiguracionSqlite(result)
                mostrar_informacion("Test de conexión exitosa")
                self.ui.a_button_save.setVisible(True)
                self.tipo_bbdd_guardada = "SQLITE"
            else:
                mostrar_error(str(error))
        else:
            mostrar_error("El campo está vacío")

    def obtener_datos_sqlite(self):
        """
        Obtiene la ruta del archivo SQLite desde la interfaz.

        Verifica si el campo de la ruta del archivo SQLite está lleno. Si está vacío, devuelve False.
        Si está lleno, devuelve la ruta como una cadena.

        Returns:
            (bool, str): `True` y la ruta del archivo si la validación es exitosa, `False` y `None` si falla.
        """
        file_path = self.ui.a_lineEdit_search_file.text().strip()
        if validar_texto(str(file_path)):
            return True, file_path
        return False, None

    def cargar_configuracion_mysql(self):
        """
        Carga la configuración actual de MySQL desde el archivo correspondiente.

        Si la carga es exitosa, actualiza los campos de la interfaz con los valores de configuración.
        Si falla, muestra un mensaje de error.
        """
        success, error = self.configuracion_mysql.cargar()
        if error:
            mostrar_error(str(error))
        elif success:
            self.datos_config_mysql = self.configuracion_mysql.configuracion_actual
            self.actualizar_campos_mysql()
        else:
            mostrar_error("Error inesperado")

    def cargar_configuracion_sqlite(self):
        """
        Carga la configuración actual de SQLite desde el archivo correspondiente.

        Si la carga es exitosa, actualiza los campos de la interfaz con los valores de configuración.
        Si falla, muestra un mensaje de error.
        """
        success, error = self.configuracion_sqlite.load()
        if error:
            mostrar_error(str(error))
        elif success:
            self.datos_config_sqlite = self.configuracion_sqlite.current_config
            self.actualizar_campos_sqlite()
        else:
            mostrar_error("Error inesperado")

    def convertir_lista_a_config_mysql(self, lista):
        """
        Convierte una lista de valores en un objeto `ConfiguracionMysql` para MySQL.

        Toma los valores de la lista y los asigna a un nuevo objeto `ConfiguracionMysql`.
        """
        self.datos_config_mysql_modif = ConfiguracionMysql(
            host=lista[0],
            puerto=lista[1],
            usuario=lista[2],
            contrasena=lista[3],
            base_datos=lista[4],
        )

    def obtener_datos_mysql(self):
        """
        Obtiene los datos ingresados en los campos de la interfaz para la configuración de MySQL.

        Verifica que los campos no estén vacíos. Si todos los campos son válidos, los devuelve en una lista.

        Returns:
            (bool, list): `True` y la lista de valores si la validación es exitosa, `False` y `None` si falla.
        """
        campos = [
            self.ui.a_lineEdit_host.text().strip(),
            self.ui.a_lineEdit_port.text().strip(),
            self.ui.a_lineEdit_user.text().strip(),
            self.ui.a_lineEdit_password.text().strip(),
            self.ui.a_lineEdit_bbdd.text().strip(),
        ]

        for campo in campos:
            if not validar_texto(campo):
                return False, None
        return True, campos

    def guardar_configuracion_mysql(self):
        """
        Guarda la configuración de MySQL en el archivo correspondiente.

        Si la operación es exitosa, actualiza los datos de configuración y muestra un mensaje de éxito.
        Si falla, muestra un mensaje de error.
        """
        success, error = self.configuracion_mysql.actualizar(self.datos_config_mysql_modif)
        if success:
            self.datos_config_mysql = self.configuracion_mysql.configuracion_actual
            mostrar_informacion("Los datos han sido modificados correctamente")
            self.actualizar_campos_mysql()
        else:
            mostrar_error("Error al guardar los valores", str(error))

    def guardar_configuracion_sqlite(self):
        """
        Guarda la configuración de SQLite en el archivo correspondiente.

        Si la operación es exitosa, actualiza los datos de configuración y muestra un mensaje de éxito.
        Si falla, muestra un mensaje de error.
        """
        success, error = self.configuracion_sqlite.update(self.datos_config_sqlite_modif)
        if success:
            self.datos_config_sqlite = self.configuracion_sqlite.current_config
            mostrar_informacion("Los datos han sido modificados correctamente")
            self.actualizar_campos_sqlite()
        else:
            mostrar_error(str(error))
