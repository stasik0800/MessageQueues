import sqlite3


def set_connection(db_path):
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.Error as e:
        print (str(e) + ' Please set currect path to db location')


def get_data(conn,sql):
    cur = conn.cursor()
    cur.execute(sql)

    col_names = [i[0] for i in cur.description]
    data = [dict(zip(list(col_names),list(row))) for row in cur.fetchall()]

    return data