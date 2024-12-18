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
    host=config("DB_HOST"),
    user=config("DB_USER"),
    passwd=config("DB_PASSWORD"),
)
# Preparar cursor
cursorObject = data_Base.cursor()

# Crear base de datos
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!!!")
