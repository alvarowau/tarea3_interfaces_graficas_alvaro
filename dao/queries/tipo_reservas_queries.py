MYSQL_QUERIES = {
    'get_all_tipo_reservas': "SELECT * FROM tipos_reservas",
    'get_tipo_reservas_by_id': "SELECT * FROM tipos_reservas WHERE tipo_reserva_id = %s",
    'existe_tabla': "SHOW TABLES LIKE 'tipos_reservas'",
    'describe_tabla': "DESCRIBE tipos_reservas",
    'existe_congreso': "SELECT COUNT(*) AS total FROM tipos_reservas WHERE nombre = 'Congreso'"
}

# Consultas para SQLite
SQLITE_QUERIES = {
    'get_all_tipo_reservas': "SELECT * FROM tipos_reservas",
    'get_tipo_reservas_by_id': "SELECT * FROM tipos_reservas WHERE tipo_reserva_id = ?",
    'existe_tabla': "SELECT name FROM sqlite_master WHERE type='table' AND name='tipos_reservas'",
    'describe_tabla': "PRAGMA table_info(tipos_reservas)",
    'existe_congreso': "SELECT COUNT(*) AS total FROM tipos_reservas WHERE nombre = 'Congreso'"
}
