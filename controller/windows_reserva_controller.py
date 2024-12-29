from PySide6.QtCore import QDate
from PySide6.QtGui import QBrush, QColor
from PySide6.QtWidgets import QDialog, QCalendarWidget

from dao.reserva_dao import ReservaDAO
from dao.salon_dao import SalonDAO
from dao.tipo_cocina_dao import TipoCocinaDAO
from dao.tipo_reserva_dao import TipoReservaDAO
from files_ui.ui_window_reserva import Ui_window_reserva
from model.reserva import Reserva
from util.comprobaciones import validar_texto
from util.mostrar_mensajes import mostrar_error, mostrar_advertencia, mostrar_informacion

ID_CONGRESO = 3

class ControladorReserva(QDialog):
    """Controlador para gestionar la creación y edición de reservas."""

    fechas_ocupadas = list()

    def __init__(self, reserva_dao: ReservaDAO, tipo_reserva_dao: TipoReservaDAO,
                 salon_dao: SalonDAO, tipo_cocina_dao: TipoCocinaDAO, reserva_modificacion: Reserva = None, es_editar: bool = False):
        """Inicializa el controlador con DAOs y configuración de modo.

        Args:
            reserva_dao (ReservaDAO): Acceso a datos de reservas.
            tipo_reserva_dao (TipoReservaDAO): Acceso a datos de tipos de reserva.
            salon_dao (SalonDAO): Acceso a datos de salones.
            tipo_cocina_dao (TipoCocinaDAO): Acceso a datos de tipos de cocina.
            reserva_modificacion (Reserva, opcional): Reserva a modificar.
            es_editar (bool, opcional): Indica si se está editando una reserva.
        """
        try:
            super().__init__()
            self.ui = Ui_window_reserva()
            self.ui.setupUi(self)
        except Exception as e:
            mostrar_error("Error al cargar la ventana de reserva", str(e))

        self.es_editar = es_editar
        self.reserva_dao = reserva_dao
        self.tipo_reserva_dao = tipo_reserva_dao
        self.salon_dao = salon_dao
        self.tipo_cocina_dao = tipo_cocina_dao

        self.reserva_modificacion = reserva_modificacion

        self.ui.a_comboBox_tipe_reserva.currentIndexChanged.connect(self.cambiar_widget)
        self.ui.a_pushButton_volver.clicked.connect(self.volver_click)

        self._inicializar_interfaz()

    def _inicializar_interfaz(self):
        """Configura la interfaz dependiendo del estado de la reserva."""
        if self.es_editar:
            if self.reserva_modificacion:
                self.setWindowTitle("Edición de reserva")
                self.ui.a_label_title.setText("Edición de reserva")
                self._preparar_interfaz_para_edicion()
            else:
                mostrar_error("No se ha encontrado la reserva para editar.")
        else:
            self.setWindowTitle("Nueva reserva")
            self.ui.a_label_title.setText("Nueva reserva")
            self._preparar_interfaz_para_nueva_reserva()

    def _preparar_interfaz_comun(self):
        """Configura elementos comunes de la interfaz para cualquier modo."""
        self._llenar_comboboxes()
        self.ui.a_widget_data_congres.setVisible(False)
        self._configurar_boton_fecha()
        self.ui.a_pushButton_reserva.clicked.connect(self.recoger_datos)

    def _preparar_interfaz_para_nueva_reserva(self):
        """Prepara la interfaz para una nueva reserva."""
        self._preparar_interfaz_comun()

    def _preparar_interfaz_para_edicion(self):
        """Prepara la interfaz para editar una reserva existente."""
        if self.reserva_modificacion:
            self.ui.a_label_title.setText("Edición de reserva")
            self.ui.a_pushButton_reserva.setText("Editar")
            self._preparar_interfaz_comun()

            self.ui.a_lineEdit_name.setText(str(self.reserva_modificacion.persona))
            self.ui.a_lineEdit_phone.setText(str(self.reserva_modificacion.telefono))

            self.ui.a_dateEdit_date.setDate(self.reserva_modificacion.fecha)

            self.ui.a_spinBox_asistans.setValue(self.reserva_modificacion.ocupacion)

            self.ui.a_radioButton_habita.setChecked(self.reserva_modificacion.habitaciones == 1)
            self.ui.a_spinBox_jornadas.setValue(self.reserva_modificacion.jornadas)
            self.cambiar_widget()
        else:
            mostrar_error("No se ha encontrado la reserva para editar.")

    def cambiar_widget(self):
        """Muestra u oculta widgets según el tipo de reserva seleccionado."""
        tipo_reserva = self.ui.a_comboBox_tipe_reserva.currentText()
        self.ui.a_widget_data_congres.setVisible(tipo_reserva == "Congreso")

    def _llenar_comboboxes(self):
        """Llena los comboBoxes necesarios para la interfaz."""
        self._llenar_comboBox_salon()
        self._llenar_comboBox_tipo_reservas()
        self._llenar_comboBox_tipo_cocina()

    def _llenar_comboBox_tipo_reservas(self):
        """Llena el comboBox con los tipos de reservas disponibles."""
        tipos_reservas = self.tipo_reserva_dao.get_all_tipo_reservas()
        self.ui.a_comboBox_tipe_reserva.clear()
        for tipo_reserva in tipos_reservas:
            self.ui.a_comboBox_tipe_reserva.addItem(tipo_reserva.nombre, tipo_reserva.tipo_reserva_id)

        if self.es_editar and self.reserva_modificacion:
            tipo_reserva_id = self.reserva_modificacion.tipo_reserva_id
            if tipo_reserva_id:
                index = self.ui.a_comboBox_tipe_reserva.findData(tipo_reserva_id)
                if index != -1:
                    self.ui.a_comboBox_tipe_reserva.setCurrentIndex(index)

    def _llenar_comboBox_tipo_cocina(self):
        """Llena el comboBox con los tipos de cocina disponibles."""
        tipos_cocina = self.tipo_cocina_dao.get_all_tipo_cocinas()
        self.ui.a_comboBox_cocina.clear()
        for cocina in tipos_cocina:
            self.ui.a_comboBox_cocina.addItem(cocina.nombre, cocina.tipo_cocina_id)

        if self.es_editar and self.reserva_modificacion:
            tipo_cocina_id = self.reserva_modificacion.tipo_cocina_id
            if tipo_cocina_id:
                index = self.ui.a_comboBox_cocina.findData(tipo_cocina_id)
                if index != -1:
                    self.ui.a_comboBox_cocina.setCurrentIndex(index)

    def _llenar_comboBox_salon(self):
        """Llena el comboBox con los salones disponibles."""
        salones, err = self.salon_dao.get_all_salones()
        self.ui.a_comboBox_salon.clear()
        for salon in salones:
            self.ui.a_comboBox_salon.addItem(salon.nombre, salon.salon_id)

        if self.es_editar and self.reserva_modificacion:
            salon_id = self.reserva_modificacion.salon_id
            if salon_id:
                index = self.ui.a_comboBox_salon.findData(salon_id)
                if index != -1:
                    self.ui.a_comboBox_salon.setCurrentIndex(index)

    def _configurar_boton_fecha(self):
        """Configura las fechas disponibles en el calendario."""
        fecha_actual = QDate.currentDate()
        self.ui.a_dateEdit_date.setDate(fecha_actual)
        self.ui.a_dateEdit_date.setMinimumDate(fecha_actual)
        self.ui.a_dateEdit_date.setDisplayFormat("yyyy-MM-dd")
        self.ui.a_dateEdit_date.setCalendarPopup(True)

        fechas_ocupadas = self.obtener_fechas_ocupadas()
        calendar = self.ui.a_dateEdit_date.calendarWidget()
        calendar.setSelectionMode(QCalendarWidget.SingleSelection)

        for fecha in fechas_ocupadas:
            formato_desactivado = self._crear_formato_desactivado()
            calendar.setDateTextFormat(fecha, formato_desactivado)

    def obtener_fechas_ocupadas(self):
        """Obtiene las fechas ya ocupadas de las reservas existentes."""
        reservas, error = self.reserva_dao.get_all_reservas()
        self.fechas_ocupadas = [QDate(reserva.fecha.year, reserva.fecha.month, reserva.fecha.day) for reserva in reservas]
        return self.fechas_ocupadas

    def _crear_formato_desactivado(self):
        """Crea un formato visual para deshabilitar fechas en el calendario."""
        formato = self.ui.a_dateEdit_date.calendarWidget().dateTextFormat(QDate.currentDate())
        formato.setForeground(QBrush(QColor(200, 200, 200)))
        return formato

    def recoger_datos(self):
        """Recoge los datos del formulario y crea o actualiza una reserva."""
        nombre = self.ui.a_lineEdit_name.text().strip()
        telefono = self.ui.a_lineEdit_phone.text().strip()

        if not validar_texto(nombre) or not validar_texto(telefono):
            mostrar_advertencia("Por favor, completa todos los campos obligatorios.")
            return

        reserva = self._crear_reserva(nombre, telefono)
        self._guardar_reserva(reserva)

    def _crear_reserva(self, nombre, telefono):
        """Crea un objeto de reserva con los datos del formulario.

        Args:
            nombre (str): Nombre de la persona de la reserva.
            telefono (str): Teléfono de contacto.

        Returns:
            Reserva: Objeto reserva creado con los datos del formulario.
        """
        fecha_str = self.ui.a_dateEdit_date.text()
        fecha = QDate.fromString(fecha_str, "yyyy-MM-dd")

        if not fecha.isValid():
            mostrar_error("Fecha inválida", "La fecha seleccionada no es válida")
            return None

        fecha_sql = fecha.toString("yyyy-MM-dd")
        fecha_disponible = True
        if self.es_editar and fecha == self.reserva_modificacion.fecha:
                fecha_disponible = True
        else:
            for fecha_ciclo in self.obtener_fechas_ocupadas():
                if fecha == fecha_ciclo:
                    fecha_disponible = False
                    break

        if fecha_disponible:
            habitaciones = int(self.ui.a_radioButton_habita.isChecked())
            numero_jornadas = self.ui.a_spinBox_jornadas.value() if self._es_congreso() else 0
            return Reserva(
                reserva_id=-1,
                tipo_reserva_id=self.ui.a_comboBox_tipe_reserva.currentData(),
                tipo_cocina_id=self.ui.a_comboBox_cocina.currentData(),
                salon_id=self.ui.a_comboBox_salon.currentData(),
                persona=nombre,
                telefono=telefono,
                fecha=fecha_sql,
                ocupacion=self.ui.a_spinBox_asistans.value(),
                jornadas=numero_jornadas,
                habitaciones=habitaciones,
            )
        else:
            mostrar_error("La fecha no está disponible", "Elija otra fecha")

    def _guardar_reserva(self, reserva: Reserva):
        """Guarda la reserva en la base de datos.

        Args:
            reserva (Reserva): Objeto reserva a guardar o actualizar.
        """
        if self.es_editar:
            reserva.reserva_id = self.reserva_modificacion.reserva_id
            success, message = self.reserva_dao.update_reserva(reserva)
        else:
            success, message = self.reserva_dao.add_reserva(reserva)

        if success:
            mostrar_informacion("Operación exitosa", message)
        else:
            mostrar_error("Error al procesar la operación", message)

    def _es_congreso(self):
        """Determina si el tipo de reserva es un congreso.

        Returns:
            bool: True si es un congreso, False en caso contrario.
        """
        return self.ui.a_comboBox_tipe_reserva.currentData() == ID_CONGRESO

    def volver_click(self):
        """Cierra la ventana del controlador de reservas."""
        self.close()
