specific def
    query for specific record of type with tag
general def
    if type is all select *
    else:
        select all where type is kfdlnf
def searchSpec(type, tag):
    conn = psycopg2.connect(dbname="GoonEEZ", user="postgres", password="password", host="localhost", port="5432")
    conn.autocommit = True
    cur = conn.cursor()
    sql=f"""SELECT * FROM useritems WHERE type='task' AND name LIKE '%random%'"""
    cur.execute(sql)
    results = cur.fetchall()
    conn.close()