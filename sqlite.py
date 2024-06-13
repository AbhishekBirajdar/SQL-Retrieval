import sqlite3

connection = sqlite3.connect("student.db")

#Creating cursor for inserting record and creating table
cursor = connection.cursor()

table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25));
"""

cursor.execute(table_info)

#Insert some records

cursor.execute('''Insert into STUDENT values('Jayesh','ML','A')''')
cursor.execute('''Insert into STUDENT values('Ram','DL','B')''')
cursor.execute('''Insert into STUDENT values('Jagdish','AI','C')''')
cursor.execute('''Insert into STUDENT values('Jaydeep','NLP','B')''')
cursor.execute('''Insert into STUDENT values('Ramesh','DS','A')''')
cursor.execute('''Insert into STUDENT values('Jay','ML','A')''')


#Display records

print("The inserted records are")

data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)



connection.commit()
connection.close()