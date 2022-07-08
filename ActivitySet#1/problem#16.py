# Databases
# https://www.py4e.com/lessons/database

import sqlite3
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("""CREATE TABLE Ages(
             name VARCHAR(128),
             age INTEGER
             )"""
         )
def add_people(sName, iAge):
    with conn:
        c.execute("INSERT INTO Ages VALUES (:name, :age)", {'name':sName, 'age':iAge})


lPeople = [('Emmy', 29), ('Maanisha', 24), ('Karsyn', 18), ('Elish', 39), ('Kaylan', 31)]
for tItem in lPeople:
    sName, iAge = tItem
    add_people(sName, iAge)

c.execute("SELECT hex(name || age) AS X FROM Ages ORDER BY X")
print(c.fetchall())

conn.commit()
conn.close()