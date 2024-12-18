# Install Mysql on the computer
# 
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

# Conexión a MySQL sin contraseña
import mysql.connector

# Conexión a MySQL con contraseña
data_Base = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Casino1980",  # Usa la misma contraseña que en settings.py
)

# Preparar cursor
cursorObject = data_Base.cursor()

# Crear base de datos
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!!!")
