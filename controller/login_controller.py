from PySide6.QtCore import QObject, Slot
from PySide6.QtWidgets import QMessageBox

from util.util_login import login_principal
from files_ui.login_windows import Ui_Login


class ControladorLogin(Ui_Login, QObject):
    """
    Controlador encargado de gestionar el inicio de sesión.
    Maneja la lógica de validación de credenciales y la interacción con la interfaz gráfica de inicio de sesión.
    """

    def __init__(self, login_window):
        """
        Inicializa el controlador de la ventana de login.
        Conecta el botón de login con la función de manejo.

        Args:
            login_window (QWidget): La ventana de login que se va a controlar.
        """
        super().__init__()
        self.setupUi(login_window)
        self.a_button_login.clicked.connect(self.manejar_login)
        self.login_exitoso = False
        self.login_window = login_window  # Guarda la ventana de login

    @Slot()
    def manejar_login(self):
        """
        Maneja la lógica de inicio de sesión, verificando las credenciales ingresadas.
        Si el inicio es exitoso, cierra la ventana de login. Si el inicio de sesión falla,
        muestra un mensaje de error.

        Este método es invocado cuando se hace clic en el botón de login.

        Se utiliza la función `login_principal` para verificar las credenciales.

        Muestra un mensaje de error usando un cuadro de diálogo si las credenciales son incorrectas.
        """
        usuario = self.a_lineEdit_user.text().strip()
        contrasena = self.a_lineEdit_pass.text().strip()

        es_login_exitoso, mensaje_error = login_principal(usuario_entrada=usuario, contrasena_entrada=contrasena)

        if es_login_exitoso:
            # Si el login fue exitoso, cierra la ventana de login
            self.login_exitoso = True
            self.login_window.close()
        else:
            # Si el login falló, muestra un mensaje de error
            QMessageBox.critical(None, "Error de inicio de sesión", mensaje_error)

    def obtener_resultado_login(self):
        """
        Devuelve el estado del login: True si fue exitoso, False en caso contrario.

        Returns:
            bool: El resultado del login, `True` si fue exitoso, `False` si falló.
        """
        return self.login_exitoso
