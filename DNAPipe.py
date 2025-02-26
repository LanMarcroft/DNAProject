import mysql.connector
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv('pass.env')
mpassword = os.getenv('MYSQL_Password')

con = mysql.connector.connect(
        host='localhost',
        user='root',
        password=mpassword,
        database='FFDNA'
        )
cur = con.cursor()
f = Path('/Users/lanmarcroft/Desktop/Projects/DNAProject/FDNA/Brighton\'sDNa.txt')
with open(f, encoding='utf-8', errors='replace') as file:
    for line in file:
        if line.startswith('rs') and not line.startswith('rsid'):
            line = line.split()
            rsid = line[0]
            chromosome = line[1]
            position = line[2]
            allele1 = line[3]
            allele2 = line[4]
            query = f'''INSERT INTO person3 
            (rsid, chromosome, position, allele1, allele2) 
            VALUES (%s,%s,%s,%s,%s)''' 
            cur.execute(query, (rsid, chromosome, position, allele1, allele2))
            print('worked')

#tup = ('K','M')
#directory = Path('/Users/lanmarcroft/Desktop/Projects/DNAProject/FDNA')
#files = [f for f in directory.iterdir() if f.name.startswith(tup)]
#for i, file_path in enumerate(files,start=1):
#    table = 'person' + str(i)
#    with open(file_path, encoding='utf-8', errors='replace') as file:
#        for line in file:
#            if line.startswith('rs') and not line.startswith('rsid'):
#                line = line.split()
#                rsid = line[0]
#                chromosome = line[1]
#                position = line[2]
#                allele1 = line[3]
#                allele2 = line[4]
#                query = f'''INSERT INTO {table} 
#                (rsid, chromosome, position, allele1, allele2) 
#                VALUES (%s,%s,%s,%s,%s)''' 
#                cur.execute(query, (rsid, chromosome, position, allele1, allele2))
#                print('worked')
con.commit()
cur.close()
con.close()
