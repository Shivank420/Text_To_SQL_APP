import sqlite3

connection = sqlite3.connect('student.db')

cursor = connection.cursor()
 
table_info = """
Create table STUDENT(Name VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);
"""

cursor.execute(table_info)

#insert some more records

cursor.execute('''INSERT INTO STUDENT VALUES('John', 'Data Science', 'A', 85)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Jane', 'Data Science', 'B', 90)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Doe', 'Data Science', 'C', 95)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Alice', 'Data Science', 'A', 80)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Bob', 'Data Science', 'B', 75)''')

# Display all the records
print("The inserted records are")

data = cursor.execute('''SELECT * FROM STUDENT''')

for row in data:
    print(row)
    
## Close the connection

connection.commit()
connection.close()

print("The connection is closed")