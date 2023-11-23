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

class Grade:
    def __init__(self, grade_id, graded_by, question_id, score):
        self.grade_id = grade_id
        self.graded_by = graded_by
        self.question_id = question_id
        self.score = score

    def insert_grade(self):
        conn = get_connection()
        cur = conn.cursor()

        sql = (""" INSERT INTO grades (grade_id, graded_by, question_id, score) VALUES ('{}', '{}','{}', '{}')""" \
               .format(self.grade_id, self.graded_by, self.question_id, self.score))
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()

        return True