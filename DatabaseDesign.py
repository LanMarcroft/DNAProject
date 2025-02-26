import mysql.connector

con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='S2bst4nc3',
        database='FFDNA'
        )
cur = con.cursor()

cur.execute("""CREATE TABLE person1
            (rsid VARCHAR(20),
            chromosome SMALLINT,
            position INTEGER,
            allele1 VARCHAR(1),
            allele2 VARCHAR(1)
            );""")
cur.execute("""CREATE TABLE person2
            (rsid VARCHAR(20),
            chromosome SMALLINT,
            position INTEGER,
            allele1 VARCHAR(1),
            allele2 VARCHAR(1)
            );""")
cur.execute("""CREATE TABLE person3
            (rsid VARCHAR(20),
            chromosome SMALLINT,
            position INTEGER,
            allele1 VARCHAR(1),
            allele2 VARCHAR(1)
            );""")

