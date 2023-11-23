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

class Answer:
    def __init__(self, ans_id, answered_by, answer):
        self.ans_id = ans_id
        self.answered_by = answered_by
        self.answer = answer

    def insert_answer(self):
        conn = get_connection()
        cur = conn.cursor()

        sql = (""" INSERT INTO answers (ans_id, answered_by, answer) VALUES ('{}', '{}','{}')""" \
               .format(self.ans_id, self.answered_by, self.answer))
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()

        return True