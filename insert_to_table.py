import psycopg2
import json


def connect():
    sql = """INSERT INTO books
             VALUES(%s, %s, %s, %s, %s) RETURNING judul;"""

    try:
      conn = psycopg2.connect(
      host="localhost",
      database="rbti",
      user="postgres",
      password="root")
      cur = conn.cursor()

      dataBuku = loadJson()

      for buku in dataBuku:
        try:
          cur.execute(sql, (buku["id_buku"],
          buku["judul"],buku["penulis"], buku["penerbit"], buku["tahun"]))
          judul = cur.fetchone()[0]
          print(judul)
          conn.commit()
        except(Exception, psycopg2.DatabaseError) as error:
          conn.rollback()
          print(error)
          continue
      

      cur.close()

    except(Exception, psycopg2.DatabaseError) as error:
      print(error)

    finally:
      if conn is not None:
        conn.close()

def loadJson():
  f = open('buku.json',)

  data = json.load(f)
  return data


if __name__ == "__main__":
  connect()