import psycopg2
import datetime

def searchParam(type, search):
    conn = psycopg2.connect(dbname="GoonEEZ", user="postgres", password="password", host="localhost", port="5432")
    conn.autocommit = True
    cur = conn.cursor()
    sql=f"""SELECT * FROM useritems WHERE type='{type}' AND name LIKE '%{search}%'"""
    cur.execute(sql)
    results = cur.fetchall()
    conn.close()
    print(results)
    return results

def searchSpec(tag):
    conn = psycopg2.connect(dbname="GoonEEZ", user="postgres", password="password", host="localhost", port="5432")
    conn.autocommit = True
    cur = conn.cursor()
    sql=f"""SELECT * FROM useritems WHERE tag={tag}"""
    cur.execute(sql)
    results = cur.fetchall()
    conn.close()
    return results

def searchTypes(type) :
    conn = psycopg2.connect(dbname="GoonEEZ", user="postgres", password="password", host="localhost", port="5432")
    conn.autocommit = True
    cur = conn.cursor()
    if type.lower() == 'all':
        sql=f"""SELECT * FROM useritems"""
    else:
        sql=f"""SELECT * FROM useritems WHERE type={type}"""
    cur.execute(sql)
    results = cur.fetchall()
    conn.close()
    return results