import psycopg2
import datetime

def deleteStep(tag):
        conn = psycopg2.connect(dbname="GoonEEZ", user="postgres", password="password", host="localhost", port="5432")
        conn.autocommit = True
        cur = conn.cursor()
        ct = datetime.datetime.now()
        sql=f"""DELETE FROM userItems WHERE tag={tag}"""
        cur.execute(sql)
        conn.close()
        return


