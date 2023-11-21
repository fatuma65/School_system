from urllib.parse import urlparse
import psycopg2
from flask import current_app as app

# class Database:

#     def __init__(self, database_url):
#         parsed_url = urlparse(database_url)
#         db = parsed_url[::1]
#         hostname = parsed_url.hostname
#         username = parsed_url.username
#         password = parsed_url.password
#         port = parsed_url.port

#         self.con = psycopg2.connect(database=db, host=hostname, user=username, pswd=password, port_id=port)
#         self.con.autocommit = True
#         self.cursor = self.con.cursor()

#     def create_tables(self):

#         create = (
#             '''
#                 CREATE TABLE IF NOT EXISTS administration (
#                 first_name VARCHAR(20) NOT NULL,
# #                 last_name VARCHAR(20) NOT NULL,
# #                 username VARCHAR(30) NOT NUL,
# #                 email TEXT NOT NULL,
# #                 password TEXT NOT NULL
# #                 );
# #             '''
# #         )
# #         for creat in create:
# #             self.cursor.execute(creat)

# #     def select_user(self):
# #         sql = (''' SELECT * FROM administration''')
# #         self.cursor.execute(sql)
# #         return self.cursor.fetchall()

# # def db_handler():
# #     obj = Database(app.config['DATABASE_URL'])
# #     return obj



# class database:
#     def __init__(self, hostname, username, dbname, password, port):
#         self.hostname = hostname
#         self.username = username
#         self.dbname = dbname
#         self.password = password
#         self.port = port
        
#         self.conn = psycopg2.connect(
#             hostname = 'localhost',
#             username = 'postgres',
#             dbname = 'school',
#             password = '123456789',
#             port = '5432'
#         )
         
#         self.conn.autocommit = True
#         self.cursor = self.conn.cursor()
#     # conn.commit()

#     def create_tables(self):

#         create = (
#             '''
#                 CREATE TABLE IF NOT EXISTS administration (
#                 first_name VARCHAR(20) NOT NULL,
#                 last_name VARCHAR(20) NOT NULL,
#                 username VARCHAR(30) NOT NUL,
#                 email TEXT NOT NULL,
#                 password TEXT NOT NULL
#             );
#             '''
#             )
        

#         for cre in create:
#             self.cursor.execute(cre)

#         self.conn.commit()
#         # cur.close
#         # conn.close()

#     def select_admin(self):
#         sql = (''' SELECT * FROM administration ''')
#         self.cursor.execute(sql)
#         return self.cursor.fetchall()
    
# def db_handler():
#     obj = database(app.config['DATABASE_URL'])
#     # obj = database()
#     return obj

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
        first_name VARCHAR(20) NOT NULL,
        last_name VARCHAR(20) NOT NULL,
        username VARCHAR(30) NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL);
    """,
    """
        CREATE TABLE IF NOT EXISTS teacher (
        teacher_id UUID DEFAULT uuid_generate_v4(),
        first_name VARCHAR(20) NOT NULL,
        last_name VARCHAR(20) NOT NULL,
        username VARCHAR(30) NOT NULL,
        email TEXT NOT NULL,
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
        password TEXT NOT NULL
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