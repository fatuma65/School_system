from flask import current_app as app
# from App.auths.database import db_handler
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

# teacher model
class Teacher:
    def __init__(self, teacher_id, first_name, last_name, username, email, password):
        
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.role = "teacher"
        self.password = password

    def insert_teacher(self):
        conn = get_connection()
        cur = conn.cursor()

        sql = (''' INSERT INTO teacher (teacher_id, first_name, last_name, username, email, role, password) VALUES ('{}','{}','{}','{}','{}','{}','{}')'''\
               .format(self.teacher_id, self.first_name, self.last_name, self.username, self.email,self.role, self.password))
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()

        return True
        