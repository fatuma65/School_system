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

class Quizz:
    def __init__(self, quizz_id, created_by, question):
        self.quizz_id = quizz_id
        self.created_by = created_by
        self.question = question

    def insert_quizz(self):
        conn = get_connection()
        cur = conn.cursor()

        sql = (""" INSERT INTO quizzes (quizz_id, created_by, question) VALUES ('{}', '{}','{}')""" \
               .format(self.quizz_id, self.created_by, self.question))
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()

        return True