import mysql.connector

con = mysql.connector.connect(
        host = 
        user = 
        password = 
        database = 
        )
cur = con.cursor()
#insert table names
table1 = ''
table2 = ''
cur.execute(f'SELECT * FROM {table1};')
person1 = cur.fetchall()
cur.execute(f'SELECT * FROM {table2};')
person2 = cur.fetchall()
person2_set = set(person2)
same = {}
for row in person1:
    if row in person2_set:
        same[row[0]] = row[1:]
print(same)
print(len(person1))
print(len(same))
print(len(same)/len(person1))
cur.close()
con.close()












