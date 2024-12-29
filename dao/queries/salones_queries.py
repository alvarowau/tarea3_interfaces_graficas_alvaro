
MYSQL_QUERIES = {
    'get_all_salones': "SELECT * FROM salones",
    'get_salon_by_id' : "SELECT * FROM salones WHERE salon_id = %s",
    'existe_tabla' : "SHOW TABLES LIKE 'salones'",
    'describe_tabla' : "DESCRIBE salones"
}

# Consultas para SQLite
SQLITE_QUERIES = {
    'get_all_salones': "SELECT * FROM salones",
    'get_salon_by_id': "SELECT * FROM salones WHERE salon_id = ?",
    'existe_tabla': "SELECT name FROM sqlite_master WHERE type='table' AND name='salones'",
    'describe_tabla': "PRAGMA table_info(salones)"
}