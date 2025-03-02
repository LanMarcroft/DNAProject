import mysql.connector

con = mysql.connector.connect(
        host='host',
        user='user',
        password='password',
        database='database'
        )
cur = con.cursor()

cur.execute("""CREATE TABLE person1
            (rsid VARCHAR(20),
            chromosome SMALLINT,
            position INTEGER,
            allele1 VARCHAR(1),
            allele2 VARCHAR(1)
            );""")
#cur.execute("""CREATE TABLE person2
#            (rsid VARCHAR(20),
#            chromosome SMALLINT,
#            position INTEGER,
#            allele1 VARCHAR(1),
#            allele2 VARCHAR(1)
#            );""")
#cur.execute("""CREATE TABLE person3
#            (rsid VARCHAR(20),
#            chromosome SMALLINT,
#            position INTEGER,
#            allele1 VARCHAR(1),
#            allele2 VARCHAR(1)
#            );""")

