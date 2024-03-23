import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
)

#create cursor
cursorObject = database.cursor()

#create database
cursorObject.execute("CREATE DATABASE dj_crm");

print("database created successfully!!")