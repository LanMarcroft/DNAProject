Welcome!

This is my first venture into the DNA data realm and it has been quite an adventure.

This project parses through raw DNA.txt (at the moment only ancestry.com data), uploads them to a mysql database, provides inferences, and allows for further search and inference. This project can also work without a database if needed as I have included the file Raw_File_Trait_Test.py so a user can just run the trait test without having to set up a mysql database.

GWAS FULL DNA TRAIT SEARCH
GWAS_Trait_Search.py - This script goes through every SNP in the database table provided and searches the GWAS API for matches, finding ALL of the traits that are assiciated with that SNP. This file does take a few hours to run even with async working to speed up the process. 

Output looks like this.
circadian rhythm ['rs141175086', 'rs11121022', 'rs2050122', 'rs11162296', 'rs76681500', 'rs10493596', 'rs34714364', 'rs10157197', 'rs9436116', 'rs516134', 'rs1144566', 'rs70944707', 'rs62158211', 'rs3731570', 'rs700641', 'rs1595824', 'rs11684176', 'rs35333999', 'rs75804782', 'rs55694368', 'rs11895698', 'rs11708779', 'rs12487658', 'rs11709706', 'rs10070616', 'rs9357620', 'rs4715491', 'rs35833281', 'rs2653349', 'rs9479402', 'rs62436127', 'rs2948276', 'rs2190422', 'rs2975734', 'rs1481757', 'rs192534763', 'rs1147813', 'rs77641763', 'rs2282300', 'rs10896109', 'rs61931739', 'rs1733410', 'rs1969363', 'rs12822662', 'rs9325144', 'rs4595586', 'rs4547160', 'rs9565309', 'rs2341534', 'rs2239557', 'rs432925', 'rs12927162', 'rs11545787', 'rs12965577', 'rs9961653', 'rs4821940', 'rs196974']]
skin pigmentation ['rs2272756', 'rs7538231', 'rs6792049', 'rs1423300', 'rs7713279', 'rs9292519', 'rs35406', 'rs16891982', 'rs28777', 'rs12203592', 'rs9350204', 'rs2524069', 'rs13198547', 'rs4259415', 'rs895267', 'rs13278114', 'rs4130120', 'rs11198112', 'rs10831496', 'rs1042602', 'rs1126809', 'rs4842464', 'rs4842610', 'rs1290177', 'rs1800414', 'rs4778219', 'rs121918166', 'rs1800407', 'rs1800404', 'rs17652091', 'rs1448484', 'rs7174027', 'rs4778138', 'rs4778241', 'rs12913832', 'rs11636232', 'rs4424881', 'rs1453858', 'rs1426654', 'rs2470102', 'rs11636073', 'rs1805005', 'rs1805006', 'rs11547464', 'rs1805007', 'rs1805008', 'rs885479', 'rs1805009', 'rs2240751', 'rs6059655']]
These SNPs can later be put into GWAS to search for existing studies for further research on a specific trait. These are not all of the SNPs related to the trait on the site, these are YOUR SNPs. You can use this in combination with Blank_Test.py to get the rsid(SNP), chromosome, allele 1, allele 2. This is incredible useful for making inferences.

DATABASE WIDE SNP SEARCH.
Blank_Test.py - Finds rsid(SNP), chromosome, allele 1, allele 2 in database tables and prints them out.

GENERAL TRAIT TEST
DB_Trait_Test.py - A database wide search for preset SNPs that correlate with popular traits like cognitive, and physical ability. It gives the trait associated with the SNP, how it's associated, credibility score, and a link for further research. 

Output looks like.
[('rs762551', 15, 75041917, 'A', 'A')]
CYP1A2 -163C>A
Caffeine metabolism gene variant. The A allele leads to faster caffeine metabolism, classifying individuals as 'fast metabolizers.'
High – demonstrated in pharmacogenetic studies and linked to differential effects of coffee on heart health.
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4738107/
[('rs1801133', 1, 11856378, 'A', 'G')]
MTHFR C677T
A folate metabolism variant. The T allele encodes a less active MTHFR enzyme, resulting in elevated homocysteine levels and increased risk of folate-deficiency complications.
High – very well studied, with known impacts on cardiovascular and pregnancy-related outcomes.
https://www.ahajournals.org/doi/full/10.1161/01.CIR.0000066324.46336.2A

NOTICE - Getting a response for an SNP does not mean that the row ([('rs1801133', 1, 11856378, 'A', 'G')]) correlates. In this example the T allele indicates a less active MTHFR enzyme. This person has A/G, no T. More inferences can be gained by going to the url, pasting your SNP into GWAS, or for fast and possibly inaccurate inferences you can paste the full row or a list of rows into an AI chatbot.

EUROPEAN ANCESTRY TEST 
DB_Euro_Focused_Ancestry_Test.py - I made this for my family so it's not applicable to everyone. Maybe in the future there will be a more comprehensive ancestral section of this project.

ROUGH RELATION TEST
Relation_Test.py - This compares two tables(people) in a database, and checks to see how many rows are exactly alike (rsid(SNP), chromosome, allele 1, allele 2). The closer the result is to 1 the more closely related the two people are. It's a rough estimate but does work.

RAW FILE TRAIT TEST ** NO DATABASE NEEDED
Raw_File_Trait_Test.py - Does the same thing as the trait test but instead of needing to set up a mysql database you can just run it over a raw text file!

You can paste these results into an AI chatbot and get valuable inferences.

Please note - 
As the project stands as of March 2025, it is not very accurate as far as actually real world implications. These scripts do not provide medical advice. Yes, this is based off of real studies, and you can use this to do some serious research and make your own inferences but don't rely on the responses built in.



