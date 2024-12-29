MYSQL_QUERIES = {
    'get_all_reservas': "SELECT * FROM reservas ORDER BY fecha DESC",
    'get_all_reservas_by_salon_id': "SELECT * FROM reservas WHERE salon_id = %s ORDER BY fecha DESC",
    'get_reserva_by_id': "SELECT * FROM reservas WHERE reserva_id = %s",
    'add_reserva': """
        INSERT INTO reservas (tipo_reserva_id, salon_id, tipo_cocina_id, persona, telefono, fecha, ocupacion, jornadas, habitaciones) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """,
    'update_reserva': """
        UPDATE reservas 
        SET tipo_reserva_id = %s, 
            salon_id = %s, 
            tipo_cocina_id = %s, 
            persona = %s, 
            telefono = %s, 
            fecha = %s, 
            ocupacion = %s, 
            jornadas = %s, 
            habitaciones = %s
        WHERE reserva_id = %s
    """,
    'delete_reserva': "DELETE FROM reservas WHERE reserva_id = %s",
    'existe_tabla' : "SHOW TABLES LIKE 'reservas'",
    'describe_tabla' : "DESCRIBE reservas"
}

SQLITE_QUERIES = {
    'get_all_reservas': "SELECT * FROM reservas ORDER BY fecha DESC",
    'get_all_reservas_by_salon_id': "SELECT * FROM reservas WHERE salon_id = ? ORDER BY fecha DESC",
    'get_reserva_by_id': "SELECT * FROM reservas WHERE reserva_id = ?",
    'add_reserva': """
        INSERT INTO reservas (tipo_reserva_id, salon_id, tipo_cocina_id, persona, telefono, fecha, ocupacion, jornadas, habitaciones) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    'update_reserva': """
        UPDATE reservas 
        SET tipo_reserva_id = ?, 
            salon_id = ?, 
            tipo_cocina_id = ?, 
            persona = ?, 
            telefono = ?, 
            fecha = ?, 
            ocupacion = ?, 
            jornadas = ?, 
            habitaciones = ? 
        WHERE reserva_id = ?
    """,
    'delete_reserva': "DELETE FROM reservas WHERE reserva_id = ?",
    'existe_tabla': "SELECT name FROM sqlite_master WHERE type='table' AND name='reservas'",
    'describe_tabla': "PRAGMA table_info(reservas)"
}