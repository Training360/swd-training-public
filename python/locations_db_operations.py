import mariadb


def init():
    conn = mariadb.connect(user="locations", password="locations",
        host="localhost", database="locations")
    cur = conn.cursor()
    cur.execute("delete from location")
    conn.commit()
    conn.close()
