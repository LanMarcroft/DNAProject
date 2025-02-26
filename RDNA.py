import mysql.connector

con = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'S2bst4nc3',
        database = 'FFDNA'
        )
cur = con.cursor()

cur.execute('SELECT * FROM person2;')
person1 = cur.fetchall()
cur.execute('SELECT * FROM person3;')
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












