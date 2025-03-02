import mysql.connector

con = mysql.connector.connect(
        host=
        user=
        password=
        database=
        )
cur = con.cursor()

snps = {
    "y_dna_haplogroups_paternal_steppe_related": [
        "rs9786076", "rs13304168", "rs11799226", "rs34276300", "rs13304168", 
        "rs9786910", "rs34062180", "rs116283356", "rs9341296", "rs35080057", 
        "rs17222280", "rs13303774"
    ],
    "mt_dna_haplogroups_maternal_steppe_related": [
        "rs28359178", "rs28359175", "rs28359172", "rs28359168", "rs28359165", 
        "rs28359162", "rs28359159", "rs28359156", "rs28359153", "rs28359150", 
        "rs28359147", "rs28359144", "rs28359141"
    ],
    "autosomal_snps_steppe_ancestry_informative": [
        "rs4988235", "rs1426654", "rs12913832", "rs16891982", "rs3827760"
    ],
    "phenotypic_traits_pigmentation_height_lactase_adaptation": [
        "rs1426654", "rs16891982", "rs12913832", "rs4988235", "rs6440003", 
        "rs16942341", "rs3135388", "rs174546", "rs7940244"
    ],
    "disease_resistance_metabolic_adaptation_snps": [
        "rs2814778", "rs3827760", "rs174546"
    ],
    "african_ancestry": ["rs2814778"],
    "east_asian_ancestry": ["rs3827760"],
    "native_american_ancestry": ["rs3827760"],
    "south_asian_ancestry": ["rs1426654"],
    "middle_eastern_ancestry": ["rs12913832"],
    "european_substructure": [
        "rs1426654", "rs16891982", "rs12913832", "rs705708", 
        "rs9341296", "rs17222280"
    ],
    "regional_differentiation_snps_steppe_subgroups_fine_scale_ancestry": [
        "rs13304168", "rs35080057", "rs13304168", "rs35080057", "rs9847716", 
        "rs9341296", "rs13303774", "rs116283356", "rs3827760", "rs705708", 
        "rs2814778"
    ]
}
 

cur.execute('SHOW TABLES;')
database = cur.fetchall()
database = [t[0] for t in database]
for table in database:
    print(table)
    for trait in snps:
        print(trait)
        for snp in snps[trait]:
            cur.execute(f"SELECT * FROM {table} WHERE rsid = '{snp}';")
            res = cur.fetchall()
            if res:
                print(res)
            else:
                print(f"No snp:{snp} found.")

    
cur.close()
con.close()
