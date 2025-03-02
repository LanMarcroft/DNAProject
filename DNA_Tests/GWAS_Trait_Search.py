import json
import mysql.connector
import aiohttp
import asyncio
import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

con = mysql.connector.connect(
    host=
    user=
    password=
    database=
)
cur = con.cursor()

tdic = {}
burl = 'https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms'
MAX_REQ = 20
semaphore = asyncio.Semaphore(MAX_REQ)

async def api_snp_search(session, snp):
    url = f"{burl}/{snp}/associations"
    async with semaphore:
        async with session.get(url) as response:
            if response.status != 200:
                print(f"SNP search failed: {url}, Error {response.status}")
                return None
            return snp, await response.json()

async def api_trait_search(session, link):
    async with semaphore:
        async with session.get(link) as response:
            if response.status != 200:
                print(f"Trait search failed: {link}, Error {response.status}")
                return None
            return await response.json()

async def process_snps(session, snps):
    tasks = [asyncio.create_task(api_snp_search(session, snp)) for snp in snps]
    results = await asyncio.gather(*tasks)
    valid_results = [r for r in results if r is not None]

    for snp, data in valid_results:
        if not data or '_embedded' not in data or 'associations' not in data['_embedded']:
            continue

        for assoc in data['_embedded']['associations']:
            link = assoc['_links'].get('efoTraits', {}).get('href')
            if link:
                tdata = await api_trait_search(session, link)
                if tdata:
                    for t in tdata['_embedded']['efoTraits']:
                        trait = t.get('trait')
                        if trait in tdic:
                            if snp not in tdic[trait]:
                                tdic[trait].append(snp)
                        else:
                            tdic[trait] = [snp]

async def main():
    table = #Insert table name
    cur.execute('SELECT COUNT(*) FROM {table};')
    rsIdcount = cur.fetchall()[0][0]
    BATCH = 500

    async with aiohttp.ClientSession() as session:
        for offset in range(0, 500, BATCH):
            cur.execute(f"SELECT rsId FROM {table} LIMIT {BATCH} OFFSET {offset};")
            snps = [row[0] for row in cur.fetchall()]
            await process_snps(session, snps)
            print(f'Processed batch up to offset: {offset}')

    cur.close()
    con.close()

asyncio.run(main())
for key in tdic:
    print(key, tdic[key])

