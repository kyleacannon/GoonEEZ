import psycopg2
import datetime

#pull record
# set item completed to true
# time stamp complete date
# throw statu
# return

def completeStep(tag):
    conn = psycopg2.connect(dbname="GoonEEZ", user="postgres", password="password", host="localhost", port="5432")
    conn.autocommit = True
    cur = conn.cursor()
    ct = datetime.datetime.now()
    sql=f"""UPDATE userItems SET completed='{ct}' WHERE tag={tag} AND completed IS NULL"""
    cur.execute(sql)
    conn.close()
    return
