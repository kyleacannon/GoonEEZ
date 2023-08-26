import psycopg2
import datetime

def createStep(type, name, rating, description):
    conn = psycopg2.connect(dbname="GoonEEZ", user="postgres", password="password", host="localhost", port="5432")
    conn.autocommit = True
    cur = conn.cursor()
    ct = datetime.datetime.now()
    sql=f"""INSERT INTO userItems(type, name, rating, description, created) \
    VALUES('{type}', '{name}', {rating}, '{description}', '{ct}')"""
    cur.execute(sql)
    conn.close()
    return




#
# # #TEST
# conn = psycopg2.connect(dbname="GoonEEZ", user="postgres", password="password", host="localhost", port="5432")
# conn.autocommit = True
# cur = conn.cursor()
# ct = datetime.datetime.now()
# sql=f"""INSERT INTO userItems(type, name, rating, description, created) \
#     VALUES('type', 'name', 9, 'here is the description 3', '{ct}')"""
# cur.execute(sql)
# conn.close()