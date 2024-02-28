import sys
import time
import pymysql

def grabar_datos(tiempo):
    db = pymysql.connect(
    host = '192.168.1.21',
    user = 'root',
    password = 'Bryan_admin15',
    db = 'mysql',
    charset = 'utf8')
    
    try:
        usuario = 'bryan'
        sql = f"INSERT INTO log_in (check_in, user) VALUES ('{tiempo}', '{usuario}')"
        cur = db.cursor()
        cur.execute(sql)
        db.commit()
        print("Data inserted successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

def traer_datos():
    db = pymysql.connect(
        host='192.168.1.21',
        user='root',
        password='Bryan_admin15',
        db='mysql',
        charset='utf8'
    )
    try:
        sql = """
            SELECT `check_in`, `user`
            FROM `log_in`
            ORDER BY `check_in` DESC
            LIMIT 20
        """
        cur = db.cursor()
        cur.execute(sql)
        resultado = cur.fetchall()
        return resultado
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()