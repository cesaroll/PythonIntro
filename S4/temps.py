import sqlite3 as db

conn  = db.connect('test.db')
cursor = conn.cursor()
cursor.execute("drop table if exists temps")
cursor.execute("create table temps(date text, temp int)")
cursor.execute("insert into temps values('09/01/2015', 35)")
cursor.execute("insert into temps values('09/02/2015', 42)")
cursor.execute("insert into temps values('09/03/2015', 38)")
cursor.execute("insert into temps values('09/04/2015', 41)")
cursor.execute("insert into temps values('09/05/2015', 40)")
cursor.execute("insert into temps values('09/06/2015', 28)")
cursor.execute("insert into temps values('09/07/2015', 45)")
conn.commit()

conn.row_factory = db.Row

cursor.execute("select * from temps")
rows = cursor.fetchall()

for row in rows:
    print("%s %s" % (row[0], row[1]))

cursor.execute("select avg(temp) from temps")
row = cursor.fetchone()
print("The average temperature for the week was %s" % row[0])

cursor.execute("delete from temps where temp = 40")
cursor.execute("select * from temps")
rows = cursor.fetchall()

for row in rows:
    print("%s %s" % (row[0], row[1]))

conn.close()