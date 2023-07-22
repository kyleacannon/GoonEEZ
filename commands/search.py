import psycopg2
# def searchTag(tag):
#     #seperate connection from module
#     conn = psycopg2.connect(dbname="GoonEEZ", user="postgres", password="password", host="localhost", port="5432")
#     conn.autocommit = True
#     cur = conn.cursor()
#     sql=f"""SELECT * FROM userItems WHERE tag={tag}"""
#     cur.execute(sql)
#     results = cur.fetchall()
#     conn.close()
#     return results
#     ##PARSER

def searchParam(type, search):
    #seperate connection from module
    conn = psycopg2.connect(dbname="GoonEEZ", user="postgres", password="password", host="localhost", port="5432")
    conn.autocommit = True
    cur = conn.cursor()
    sql=f"""SELECT * FROM userItems WHERE type={type} AND name LIKE '%{search}%'"""
    cur.execute(sql)
    results = cur.fetchall()
    conn.close()
    return results
    ##PARSER