from hashes import *
import time

def ver_hashes(dir):
    conn = sqlite3.connect("hashes.db")
    conn.text_factory=str

    for file in os.listdir(dir):
        hash = calcula_hash(file)
        cursor = conn.execute("SELECT NAME,HASH FROM HASHES WHERE HASH = ?", (hash,))
        if cursor.fetchone() == None:
            print("se ha modificado el archivo")
            