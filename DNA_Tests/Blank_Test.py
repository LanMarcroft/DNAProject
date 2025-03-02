
import mysql.connector

con = mysql.connector.connect(
        host='host',
        user='user',
        password='password',
        database='database'
        )
cur = con.cursor()
#example parental longevity snps from GWAS
snps = ["rs80357713","rs80359550","rs1042522","rs1801133","rs1801131","rs429358","rs7412","rs6025","rs4343","rs7903146","rs13266634","rs34637584","rs6265","rs2802292","rs5882","rs12778366","rs3792119","rs2229765","rs1800562","rs1799945","rs17580","rs28929474","rs9939609","rs4977574","rs1799963"] 

cur.execute('SHOW TABLES;')
database = cur.fetchall()
database = [t[0] for t in database]
for table in database:
    print(table)
    for snp in snps:
        cur.execute(f"SELECT * FROM {table} WHERE rsid = '{snp}';")
        res = cur.fetchall()
        if res:
            print(res)
        else:
            print(f"No snp:{snp} found.")


cur.close()
con.close()
