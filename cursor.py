import mysql.connector
import psycopg2


def cursor():
    conn = psycopg2.connect(
        host="localhost",
        database="stock_analysis",
        user="postgres",
        password="rahul4758")
    mycursor = conn.cursor()
    return conn,mycursor
    

