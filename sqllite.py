import sqlite3

#connect to sqlite

connection=sqlite3.connect("students.db")

cursor=connection.cursor()

table_info="""
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)"""

cursor.execute(table_info)

cursor.execute('''Insert into STUDENT values ('Sabina','Data Science','A',90)''')
cursor.execute('''Insert into STUDENT values ('John','Data Science','B',100)''')
cursor.execute('''Insert into STUDENT values ('Reetu','Data Science','B',80)''')
cursor.execute('''Insert into STUDENT values ('Caddy','Devops','A',50)''')
cursor.execute('''Insert into STUDENT values ('Vihan','Devops','A',35)''')

#diaplay all records
print("Inserted records are:")
data=cursor.execute(''' Select * from STUDENT''')
for row in data:
    print(row)

#commit thechnages in database
connection.commit()
connection.close()

##python sqlite.py