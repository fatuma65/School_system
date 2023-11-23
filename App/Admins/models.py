from flask import current_app as app
import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host = 'localhost',
        database = 'school',
        user = 'postgres',
        password = '123456789',
        port = '5432'
    )
    return conn    

# administrator model
class Admin:
    def __init__(self, admin_id, first_name, last_name, username, email, password):

        self.admin_id = admin_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.role = 'administrator'
        self.password = password

    def insert_admin(self):
        conn = get_connection()
        cur = conn.cursor()

        sql = (""" INSERT INTO adminss (admin_id, first_name, last_name, username, email, role, password) VALUES ('{}','{}','{}','{}','{}','{}','{}')"""
               .format(self.admin_id, self.first_name, self.last_name, self.username, self.email, self.role, self.password))
        
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
        return True