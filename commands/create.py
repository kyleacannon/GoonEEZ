import psycopg2
#WS CHECK
def create_step(type, name, rating, description):
    conn = psycopg2.connect(dbname="test", user="postgres", password="password", host="localhost", port="5432")
    conn.autocommit = True
    cur = conn.cursor()
    sql=f"""INSERT INTO userTask(type, rating, name, description)
    VALUES({type}, {name}, {rating}, {description})"""
    cur.execute(sql)
    conn.close()
    return

