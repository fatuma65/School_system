import psycopg2
from flask import current_app as app

hostname = 'localhost'
dbname = 'school'
username = 'postgres'
pswd = '123456789'
port_id = '5432'

conn = psycopg2.connect(
    host = hostname,
    database = dbname,
    user = username,
    password = pswd,
    port = port_id
)

cur = conn.cursor()

create = (
    """
        CREATE TABLE IF NOT EXISTS adminss (
        admin_id UUID DEFAULT uuid_generate_v4(),
        first_name VARCHAR(20) NOT NULL,
        last_name VARCHAR(20) NOT NULL,
        username VARCHAR(30) NOT NULL,
        email TEXT NOT NULL,
        role VARCHAR(20),
        password TEXT NOT NULL);
    """,
    """
        CREATE TABLE IF NOT EXISTS teacher (
        teacher_id UUID DEFAULT uuid_generate_v4(),
        first_name VARCHAR(20) NOT NULL,
        last_name VARCHAR(20) NOT NULL,
        username VARCHAR(30) NOT NULL,
        email TEXT NOT NULL,
        role VARCHAR(20),
        password TEXT NOT NULL
        );
    """,
    """
        CREATE TABLE IF NOT EXISTS student (
        student_id UUID DEFAULT uuid_generate_v4(),
        first_name VARCHAR(20) NOT NULL,
        last_name VARCHAR(20) NOT NULL,
        username VARCHAR(30) NOT NULL,
        email TEXT NOT NULL,
        role VARCHAR(20),
        password TEXT NOT NULL
        );
    """  ,
    """
        CREATE TABLE IF NOT EXISTS questions (
        quest_id TEXT PRIMARY KEY,
        created_by TEXT,
        question TEXT
        );
    """ ,

    """
        CREATE TABLE IF NOT EXISTS answers (
        ans_id TEXT PRIMARY KEY,
        answered_by TEXT,
        answer TEXT
        );
    """,
    """
        CREATE TABLE IF NOT EXISTS quizzes (
        quizz_id TEXT PRIMARY KEY,
        created_by TEXT,
        question TEXT
        );
    """ ,
    """
        CREATE TABLE IF NOT EXISTS grades (
        grade_id TEXT PRIMARY KEY,
        graded_by TEXT,
        question_id TEXT,
        score INTEGER
        );
    """ 
)

for crea in create:
    cur.execute(crea)

def select_an_admin(username):
    sql = (""" SELECT * FROM adminss WHERE username = '{}'""".format(username))
    try:
        cur.execute(sql)
    except:
        return{"error": "An error has occured"}
    return cur.fetchone()

def select_a_student(username):
    sql = (""" SELECT * FROM student WHERE username = '{}'""".format(username))
    try:
        cur.execute(sql)
    except:
        return{"error": "An error has occured"}
    return cur.fetchone()

def select_teacher(user_n):
    sql = (""" SELECT * FROM teacher""")
    try:
        cur.execute(sql)
    except:
        return{"error": "An error has occured"}
    return cur.fetchall()

def select_a_teacher(username):
    print("*** This was called")
    sql = (""" SELECT * FROM teacher WHERE username = '{}'""".format(username))
    try:
        cur.execute(sql)
    except Exception as e:
        print(e, "*** Error")
        return
    
    return cur.fetchone()

# conn.commit()
# cur.close()
# conn.close()