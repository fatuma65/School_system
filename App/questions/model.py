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

class Question:
    def __init__(self, quest_id, created_by, question):
        self.quest_id = quest_id
        self.created_by = created_by
        self.question = question

    def insert_question(self):
        conn = get_connection()
        cur = conn.cursor()

        sql = (""" INSERT INTO questions (quest_id, created_by, question) VALUES ('{}', '{}','{}')""" \
               .format(self.quest_id, self.created_by, self.question))
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()

        return True