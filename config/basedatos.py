import mysql.connector
class Basedatos:
    
    def conectar_db(self):
        db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': '',
            'database': 'bd_pagweb_cholets'
        }
        try:
            conn = mysql.connector.connect(**db_config)
            print("Conexión a la base de datos MySQL exitosa")
            return conn
        except mysql.connector.Error as err:
            print(f"Error de conexión a la base de datos MySQL: {err}")
            return None