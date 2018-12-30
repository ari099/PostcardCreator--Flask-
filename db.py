import sqlite3, random
from sqlite3 import Error

def create_connection(db_file):
   """
   Create a database connection to the SQLite database
   specified by the db_file
   :param db_file: database file
   :return: Connection object or None
   """
   try:
      conn = sqlite3.connect(db_file)
      return conn
   except Error as e:
      print(e)

   return None


def select_all_photos(conn):
   """
   Query all rows in the photos table
   :param conn: the Connection object
   :return:
   """
   cur = conn.cursor()
   cur.execute("SELECT * FROM Photos")

   rows = cur.fetchall()

   # for row in rows:
   #    print(row)
   return rows


def select_photo_by_id(conn, id):
   """
   Query photos by ID
   :param conn: the Connection object
   :param id:
   :return:
   """
   cur = conn.cursor()
   cur.execute("SELECT Path FROM Photos WHERE ID=?", (id,))

   rows = cur.fetchall()

   # for row in rows:
   #    print(row)
   return rows


def delete_photo_by_id(conn, id):
   """
   Delete photo by ID
   :param conn: the Connection object
   :param id:
   :return:
   """
   cur = conn.cursor()
   cur.execute("DELETE FROM Photos WHERE ID=?", (id,))

   rows = cur.fetchall()
   return rows


def create_photo(conn, pic, email):
    """
    Create a new pic
    :param conn:
    :param pic:
    :return:
    """
 
    sql = "INSERT INTO Photos (ID, Path, Email, Modified, Directory) VALUES(?,?,?,?,?)"
    cur = conn.cursor()
    cur.execute(sql, (random.randint(1,101), pic, email, 0, './static/',))
    conn.commit()
    return cur.lastrowid