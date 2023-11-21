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

class Student:
    def __init__(self, student_id, first_name, last_name, username, email, password):

        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password

    def insert_student(self):
        conn = get_connection()
        cur = conn.cursor()

        sql = (''' INSERT INTO student (student_id, first_name, last_name, username, email, password) VALUES ('{}', '{}', '{}','{}','{}','{}')'''\
                .format(self.student_id, self.first_name, self.last_name, self.username, self.email,self.password)) 
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()