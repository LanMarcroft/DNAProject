import mysql.connector

con = mysql.connector.connect(
        host='host',
        user='user',
        password='password',
        database='database',
        )
cur = con.cursor()

snps = {
    "Cognitive Traits": {
        "rs4680": {
            "Gene": "COMT Val158Met",
            "Effect": "Associated with executive function and memory. The A (Met) allele leads to lower COMT enzyme activity, boosting dopamine in the prefrontal cortex. Met allele carriers often show better working memory but heightened emotional sensitivity, while the G (Val) allele (‘warrior’ variant) has higher enzyme activity and may perform better under stress.",
            "Credibility": "High – extensively studied with multiple studies and meta-analyses confirming cognitive effects.",
            "Source": "http://blog.23andme.com/2008/08/10/snpwatch-genetic-variant-may-increase-risk-for-anxiety-disorders/"
        },
        "rs907094": {
            "Gene": "PPP1R1B/DARPP-32",
            "Effect": "Influences dopamine signaling in the striatum, affecting learning and decision-making. Homozygous A allele carriers have enhanced frontostriatal function and better feedback-based learning performance.",
            "Credibility": "Moderate – several cognitive neuroscience studies link this variant to learning and brain activity, though samples are modest.",
            "Source": "https://www.pnas.org/content/104/41/16311"
        },
        "rs1800497": {
            "Gene": "ANKK1/DRD2 Taq1A",
            "Effect": "Linked to dopamine D2 receptor availability and reward processing. The T (A1) allele is associated with fewer D2 receptors and stronger reward-seeking behavior. C (A2) allele carriers have more D2 receptors, potentially aiding impulse control.",
            "Credibility": "Moderate – well-known in addiction studies, though direct cognitive impact is debated.",
            "Source": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3312578/"
        },
        "rs6314": {
            "Gene": "HTR2A His452Tyr",
            "Effect": "A serotonin 2A receptor variant associated with memory. The T (Tyr) allele was significantly associated with better long-term memory performance in at least one study.",
            "Credibility": "Moderate – some studies report strong effects on memory, but findings need replication.",
            "Source": "https://academic.oup.com/ijnp/article/11/8/1163/696460"
        },
        "rs6265": {
            "Gene": "BDNF Val66Met",
            "Effect": "Affects brain-derived neurotrophic factor and memory. The A (Met) allele impairs activity-dependent BDNF release, linked to poorer learning and memory and higher anxiety. G (Val) allele carriers have normal BDNF and generally better memory retention.",
            "Credibility": "High – over 100 studies; well-replicated effect on memory and neuroticism.",
            "Source": "http://blog.23andme.com/2009/10/30/snpwatch-the-bad-driving-gene/"
        },
        "rs17070145": {
            "Gene": "KIBRA",
            "Effect": "Associated with episodic memory performance. The T allele (minor) is linked to better memory recall, while C allele carriers show slightly lower memory scores.",
            "Credibility": "High – initially identified in a large sample and confirmed by meta-analysis.",
            "Source": "https://www.mayo.edu/research/documents/kibra-snps-pdf/DOC-10027832"
        },
        "rs363050": {
            "Gene": "SNAP25",
            "Effect": "A variant in a synaptic protein gene linked to IQ and cognitive speed. The minor allele reduces SNAP-25 expression, associated with lower cognitive scores and attention control.",
            "Credibility": "Moderate – studies (including mouse models) show functional impact on cognition.",
            "Source": "https://www.nature.com/articles/mp200913"
        },
        "rs17518584": {
            "Gene": "CADM2",
            "Effect": "Identified in a genome-wide study of information processing speed. The G allele is associated with faster processing and better cognitive test scores.",
            "Credibility": "High – found in a large meta-analysis (~53,000 individuals) of cognitive function.",
            "Source": "https://academic.oup.com/hmg/article/26/2/324/2624090"
        },
        "rs2490272": {
            "Gene": "FOXO3 intronic",
            "Effect": "Tags the longevity-associated FOXO3 variant. The C allele is over-represented in people with higher IQ in a large study.",
            "Credibility": "High – a meta-analysis of 78,000 people found this SNP strongly associated with intelligence.",
            "Source": "https://www.nature.com/articles/ng.3869"
        },
        "rs1006737": {
            "Gene": "CACNA1C",
            "Effect": "A calcium-channel gene variant associated with psychiatric disorders and cognitive function. The A (risk) allele is linked to reduced memory performance and elevated risk of bipolar disorder.",
            "Credibility": "Moderate – well-established in psychiatry genetics, with some evidence for cognitive effects.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/24162753/"
        },
        "rs12807809": {
            "Gene": "NRGN",
            "Effect": "A neurogranin gene variant initially linked to schizophrenia risk. The C allele is associated with better episodic memory encoding and structural brain differences, while T is a risk allele for schizophrenia.",
            "Credibility": "Moderate – identified in genome-wide studies of schizophrenia; cognitive effects supported by imaging research.",
            "Source": "https://academic.oup.com/schizophreniabulletin/article/37/5/1001/1878399"
        },
        "rs3851179": {
            "Gene": "PICALM",
            "Effect": "Associated with Alzheimer’s disease risk and cognitive decline. The A allele is protective and linked to slower cognitive decline, whereas G increases AD risk.",
            "Credibility": "High – discovered in large AD GWAS and consistently replicated.",
            "Source": "https://www.frontiersin.org/articles/10.3389/fnagi.2014.00257/full"
        },
        "rs11136000": {
            "Gene": "CLU",
            "Effect": "A variant in the CLU (clusterin) gene linked to Alzheimer’s risk. The C allele is the risk allele; the T allele is associated with lower AD risk and may upregulate protective clusterin.",
            "Credibility": "High – supported by meta-analyses showing influence on AD in multiple populations.",
            "Source": "https://www.frontiersin.org/articles/10.3389/fnagi.2014.00326/full"
        }
    },
        "Physical Traits": {
        "rs1815739": {
            "Gene": "ACTN3 R577X",
            "Effect": "Known as the 'sprint gene.' The C allele (577R) preserves alpha-actinin-3 in fast muscle fibers, enhancing sprint and power performance, while the T allele (577X) causes deficiency of this protein and shifts muscle function towards endurance.",
            "Credibility": "High – robust associations found in athletes across many studies.",
            "Source": "https://journals.physiology.org/doi/full/10.1152/japplphysiol.00036.2007"
        },
        "rs2070744": {
            "Gene": "NOS3 – eNOS promoter",
            "Effect": "Affects nitric oxide production and blood flow. The C allele is linked to lower nitric oxide availability and is more frequent in power athletes. The T allele yields higher eNOS expression, improving endurance vasodilation.",
            "Credibility": "Moderate – consistent effects on eNOS expression and some sports association data.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/19701646/"
        },
        "rs1042713": {
            "Gene": "ADRB2 Arg16Gly",
            "Effect": "Beta-2 adrenergic receptor variant affecting exercise response. The G allele (Gly16) causes receptors to desensitize faster, potentially reducing stamina. The A allele (Arg16) maintains receptor responsiveness longer, associated with better endurance.",
            "Credibility": "Moderate – well-studied in metabolism and asthma; exercise effects documented but somewhat inconsistent.",
            "Source": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5651752/"
        },
        "rs11549465": {
            "Gene": "HIF1A Pro582Ser",
            "Effect": "A hypoxia-inducible factor-1α variant. The T allele (Ser582) increases HIF-1 activity under low oxygen, potentially enhancing anaerobic performance and high-altitude tolerance.",
            "Credibility": "Moderate – mechanistically plausible and observed in some athlete studies.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/21440961/"
        },
        "rs12722": {
            "Gene": "COL5A1",
            "Effect": "A collagen type V gene variant linked to connective tissue flexibility and injury risk. The T allele is associated with greater joint range of motion but higher risk of tendon/ligament injuries. CC genotype is protective against ACL tears.",
            "Credibility": "Moderate – multiple studies connect this SNP to flexibility and tendon properties.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/20083473/"
        },
        "rs2854464": {
            "Gene": "ACVR1B",
            "Effect": "A polymorphism in the activin receptor type I B gene. The A allele is associated with greater muscle strength/power; it was significantly overrepresented in European sprint/power athletes.",
            "Credibility": "Moderate – demonstrated in one large European athlete study, though population differences exist.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/27222353/"
        },
        "rs699": {
            "Gene": "AGT Met235Thr",
            "Effect": "Angiotensinogen gene variant affecting blood pressure and possibly muscle efficiency. The T (Thr235) allele is associated with higher angiotensin II levels and has been linked to power athlete status and hypertension risk.",
            "Credibility": "Moderate – known in cardiovascular genetics and some sports genetic analyses.",
            "Source": "https://www.physiology.org/doi/full/10.1152/japplphysiol.00892.2008"
        },
        "rs1800795": {
            "Gene": "IL6 – 174 G/C",
            "Effect": "An interleukin-6 promoter polymorphism. The G allele is linked to higher IL-6 production and has been found to favor power/sprint performance.",
            "Credibility": "Moderate – IL6-174G is repeatedly associated with various athletic and health outcomes.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/19585441/"
        },
        "rs4994": {
            "Gene": "ADRB3 Trp64Arg",
            "Effect": "A beta-3 adrenergic receptor variant affecting fat metabolism. The C allele (Arg64) reduces receptor function, leading to lower lipolysis and predisposition to weight gain.",
            "Credibility": "High – many studies show Arg64 carriers have higher odds of obesity and metabolic issues.",
            "Source": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3034023/"
        },
        "rs174537": {
            "Gene": "FADS1",
            "Effect": "A fatty acid desaturase variant that alters omega-3/omega-6 fatty acid profiles. The T allele reduces enzyme activity, leading to higher intermediate omega-6 (e.g., DGLA) and lower arachidonic acid.",
            "Credibility": "High – genome-wide associations have established this SNP’s effect on blood fatty acid levels.",
            "Source": "https://academic.oup.com/jn/article/143/12/1968/4561103"
        }
    },
    "Nutrition Traits": {
        "rs5082": {
            "Gene": "APOA2 -265T>C",
            "Effect": "Influences response to saturated fat intake. CC genotype carriers tend to gain more weight on high-saturated-fat diets, whereas TT carriers are relatively protected.",
            "Credibility": "High – consistently replicated gene–diet interaction in multiple populations.",
            "Source": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2768550/"
        },
        "rs662799": {
            "Gene": "APOA5 -1131T>C",
            "Effect": "Associated with triglyceride levels. The C allele is linked to higher plasma triglycerides and greater risk of hypertriglyceridemia.",
            "Credibility": "High – well-established in metabolic syndrome and cardiovascular risk studies.",
            "Source": "https://www.karger.com/Article/FullText/360284"
        },
        "rs9939609": {
            "Gene": "FTO",
            "Effect": "A common obesity-related variant. The A allele is the risk allele associated with increased appetite, higher calorie intake, and greater body fat.",
            "Credibility": "High – confirmed by numerous large studies and meta-analyses.",
            "Source": "https://drc.bmj.com/content/4/1/e000195"
        },
        "rs7903146": {
            "Gene": "TCF7L2",
            "Effect": "The strongest type 2 diabetes risk SNP. The T allele confers increased risk of T2D by impairing insulin secretion.",
            "Credibility": "High – identified in multiple large GWAS; mechanism (reduced incretin effect on insulin) is documented.",
            "Source": "https://diabetes.diabetesjournals.org/content/59/10/2620"
        },
        "rs1044498": {
            "Gene": "ENPP1 K121Q",
            "Effect": "A polymorphism affecting insulin signaling. The A allele (Q variant) impairs insulin receptor function, contributing to insulin resistance.",
            "Credibility": "Moderate – many studies link K121Q to diabetes, though not all populations show an effect.",
            "Source": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2992102/"
        },
        "rs1761667": {
            "Gene": "CD36 -31118G>A",
            "Effect": "Affects oral fat perception. The A allele reduces CD36 expression and is associated with reduced ability to taste fats, often leading to preference for high-fat foods to reach satiety.",
            "Credibility": "Moderate – human taste tests show genotype differences in fat detection.",
            "Source": "https://www.cambridge.org/core/journals/british-journal-of-nutrition/article/abs/cluster-of-differentiation-36-cd36-rs1761667-polymorphism-is-associated-with-perceived-fatty-foods-and-body-mass-index-in-spanish-children/9E0D0A0E4F2A7B32C3BB2814973F5B9F"
        },
        "rs5219": {
            "Gene": "KCNJ11 E23K",
            "Effect": "A potassium channel gene variant in pancreatic beta-cells. The T allele (Lys23) reduces channel sensitivity, which can impair insulin release.",
            "Credibility": "High – a known diabetes susceptibility variant with demonstrated effect on insulin secretion.",
            "Source": "https://diabetes.diabetesjournals.org/content/63/12/4313"
        },
        "rs1801282": {
            "Gene": "PPARG Pro12Ala",
            "Effect": "A peroxisome proliferator-activated receptor gamma variant. The C allele (Ala12) is associated with improved insulin sensitivity and about 20% reduced risk of type 2 diabetes.",
            "Credibility": "High – observed in multiple studies and a meta-analysis confirming protective effect of Ala12.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/10973254/"
        },
        "rs3764261": {
            "Gene": "CETP",
            "Effect": "A cholesteryl ester transfer protein variant affecting HDL cholesterol. The A allele is associated with higher HDL-C levels and possibly decreased heart disease risk.",
            "Credibility": "High – robust GWAS hit for HDL; effect on HDL is well quantified.",
            "Source": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2896769/"
        },
        "rs738409": {
            "Gene": "PNPLA3 I148M",
            "Effect": "A liver fat metabolism gene variant. The G allele greatly increases liver fat accumulation and risk of non-alcoholic fatty liver disease (NAFLD).",
            "Credibility": "High – shown as a major genetic factor for NAFLD across many ethnic groups.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/20185826/"
        },
        "rs174550": {
            "Gene": "FADS1",
            "Effect": "A fatty acid desaturase SNP altering polyunsaturated fatty acid levels. Minor alleles in FADS1 lead to lower synthesis of long-chain omega-3 and omega-6 fats.",
            "Credibility": "High – part of the well-known FADS cluster associations with fatty acid profiles.",
            "Source": "https://www.frontiersin.org/articles/10.3389/fphys.2018.00964/full"
        },
        "rs4988235": {
            "Gene": "LCT -13910C>T",
            "Effect": "The primary European lactase persistence variant. The T allele enables lactase production in adulthood (lactose tolerance), while the C allele causes lactase to shut down, leading to lactose intolerance.",
            "Credibility": "High – a classic example of gene-culture evolution, with strong correlation to dairy tolerance.",
            "Source": "https://medlineplus.gov/genetics/condition/lactose-intolerance/"
        },
        "rs2187668": {
            "Gene": "HLA-DQ2.5 haplotype tag",
            "Effect": "Marks the HLA-DQ2.5 haplotype associated with celiac disease. The T allele indicates presence of HLA-DQA105:01~DQB102:01 (DQ2.5).",
            "Credibility": "High – HLA-DQ2.5 is a necessary genetic factor for most celiac cases.",
            "Source": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2440571/"
        },
        "rs671": {
            "Gene": "ALDH2 Glu487Lys",
            "Effect": "The 'Asian flush' variant in alcohol dehydrogenase. The A (Lys) allele produces an inactive ALDH2 enzyme, causing acetaldehyde buildup.",
            "Credibility": "High – well-known in East Asian populations with clear biochemical effects.",
            "Source": "https://www.nih.gov/news-events/news-releases/study-finds-genetic-link-between-red-hair-fair-skin-pain-tolerance"
        },
        "rs762551": {
            "Gene": "CYP1A2 -163C>A",
            "Effect": "Caffeine metabolism gene variant. The A allele leads to faster caffeine metabolism, classifying individuals as 'fast metabolizers.'",
            "Credibility": "High – demonstrated in pharmacogenetic studies and linked to differential effects of coffee on heart health.",
            "Source": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4738107/"
        },
        "rs1801133": {
            "Gene": "MTHFR C677T",
            "Effect": "A folate metabolism variant. The T allele encodes a less active MTHFR enzyme, resulting in elevated homocysteine levels and increased risk of folate-deficiency complications.",
            "Credibility": "High – very well studied, with known impacts on cardiovascular and pregnancy-related outcomes.",
            "Source": "https://www.ahajournals.org/doi/full/10.1161/01.CIR.0000066324.46336.2A"
        },
        "rs2282679": {
            "Gene": "GC gene",
            "Effect": "A variant in the vitamin D binding protein gene affecting vitamin D status. The C allele is associated with lower circulating 25(OH) vitamin D levels, whereas the A allele is associated with higher vitamin D levels.",
            "Credibility": "High – identified through GWAS as a top determinant of vitamin D variation.",
            "Source": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3798903/"
        },
        "rs1229984": {
            "Gene": "ADH1B Arg48His",
            "Effect": "A variant in the alcohol dehydrogenase gene ADH1B. The T (His48) allele metabolizes ethanol to acetaldehyde much faster, causing flushing if acetaldehyde accumulates.",
            "Credibility": "High – well documented in East Asian populations and alcohol studies.",
            "Source": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3508524/"
        },
        "rs174547": {
            "Gene": "FADS1",
            "Effect": "Another SNP in the FADS1 cluster. The T allele is associated with reduced conversion of short-chain to long-chain polyunsaturated fatty acids.",
            "Credibility": "High – part of the same well-replicated fatty acid metabolism locus.",
            "Source": "https://www.cambridge.org/core/journals/british-journal-of-nutrition/article/association-between-fads1-rs174547-and-levels-of-longchain-pufa-a-metaanalysis/9584A0B4D8D9478B4A2A61F88108F527"
        }
    },
    "Blood Type & Disease Resistance": {
        "rs8176719": {
            "Gene": "ABO gene (O allele)",
            "Effect": "A 1-base deletion producing blood type O (absence of A/B antigens). Homozygous carriers are blood type O, associated with lower thrombosis risk but higher susceptibility to H. pylori ulcers and cholera.",
            "Credibility": "High – ABO blood group effects on disease supported by epidemiological studies.",
            "Source": "https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.109.904084"
        },
        "rs505922": {
            "Gene": "ABO intronic",
            "Effect": "Associated with disease risk. The C allele (non-O) slightly increases risk of pancreatic cancer and venous thrombosis, while T tags type O.",
            "Credibility": "High – identified in GWAS for pancreatic cancer and clotting risk.",
            "Source": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2790694/"
        },
        "rs1136201": {
            "Gene": "ERBB2 (HER2) I655V",
            "Effect": "G (Val) allele investigated for breast cancer susceptibility. Findings are mixed; some reports suggest a slight risk increase or influence on treatment outcomes.",
            "Credibility": "Moderate – many studies and meta-analyses, but no strong consensus.",
            "Source": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6468128/"
        },
        "rs1799964": {
            "Gene": "TNF-α -1031T>C",
            "Effect": "C allele linked to higher TNF-α production and increased susceptibility to severe infections (e.g. malaria) and inflammatory diseases.",
            "Credibility": "Moderate – TNF promoter variants affect cytokine levels; disease associations vary across studies.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/15211088/"
        },
        "rs9264942": {
            "Gene": "HLA-C –35kb",
            "Effect": "C allele associated with higher HLA-C surface expression and slower HIV progression. Often correlates with HLA-B*57/*27 status.",
            "Credibility": "High – discovered in GWAS of HIV controllers; mechanism well understood.",
            "Source": "https://academic.oup.com/jid/article/200/12/1822/2192315"
        },
        "rs601338": {
            "Gene": "FUT2 (secretor status)",
            "Effect": "A allele (non-functional) = non-secretor, resistant to many norovirus strains. G allele = secretor, more prone to certain GI infections.",
            "Credibility": "High – protective effect against norovirus in non-secretors is well documented.",
            "Source": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3130478/"
        },
        "rs2395029": {
            "Gene": "HCP5 (proxy for HLA-B*5701)",
            "Effect": "T allele tags HLA-B57:01, associated with elite HIV control (slow progression) and abacavir drug hypersensitivity.",
            "Credibility": "High – clinically used to predict HLA-B57:01; HLA-B57’s protective effect in HIV is well known.",
            "Source": "https://academic.oup.com/jid/article/196/2/363/2190908"
        },
        "rs3093661": {
            "Gene": "TNF-α upstream",
            "Effect": "G allele linked to higher TNF-α levels and more severe inflammatory responses (e.g. autoimmune thyroid disease).",
            "Credibility": "Moderate – influences TNF levels reliably; disease associations vary.",
            "Source": "https://www.frontiersin.org/articles/10.3389/fgene.2022.830243/full"
        },
        "rs2076530": {
            "Gene": "BTNL2",
            "Effect": "A splice-site variant. The A allele doubles the odds of sarcoidosis, especially in AA homozygotes.",
            "Credibility": "High – multiple studies confirm BTNL2 A as a sarcoidosis risk factor.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/15735647/"
        },
        "rs1800629": {
            "Gene": "TNF-α -308G>A",
            "Effect": "A allele associated with higher TNF-α production, linked to severe infectious disease and autoimmune conditions (e.g. malaria, RA).",
            "Credibility": "High – extensively studied promoter variant with functional impacts.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/15085188/"
        },
        "rs3135388": {
            "Gene": "HLA-DRB1*1501 tag",
            "Effect": "Marks the presence of HLA-DRB1*1501, the main genetic risk factor for multiple sclerosis (3–6× higher MS risk).",
            "Credibility": "High – well established in MS genetic studies.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/15735648/"
        },
        "rs28362491": {
            "Gene": "NFKB1 -94ins/del",
            "Effect": "Deletion allele lowers p50 production, associated with higher risk of ulcerative colitis and inflammatory conditions.",
            "Credibility": "Moderate – del allele linked to autoimmunity, though findings vary.",
            "Source": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3038249/"
        },
        "rs3134774": {
            "Gene": "HLA-DQB1 (DQ8)",
            "Effect": "Risk allele indicates HLA-DQ8 haplotype, conferring susceptibility to type 1 diabetes and celiac disease.",
            "Credibility": "High – HLA-DQ haplotypes firmly established in autoimmune disease risk.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/17404227/"
        }
    },

    "Are Mosquitoes Attracted to You?": {
        "rs505922": {
            "Gene": "ABO",
            "Effect": "T allele tags blood type O, which can attract more mosquito landings vs. CC (non-O).",
            "Credibility": "Moderate – one controlled study showed preference for O secretors, though many factors influence bites.",
            "Source": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2735086/"
        },
        "rs601338": {
            "Gene": "FUT2",
            "Effect": "Secretors (G allele) emit blood-group antigens in sweat, attracting mosquitoes more than non-secretors (A allele).",
            "Credibility": "Moderate – secretors show higher landing rates in certain experiments.",
            "Source": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2735086/"
        },
        "rs2814778": {
            "Gene": "DARC (Duffy antigen null)",
            "Effect": "T allele causes absence of Duffy on RBCs, conferring resistance to P. vivax malaria. Not directly about bites, but relevant to disease.",
            "Credibility": "High – nearly all West Africans are Duffy-null and protected from vivax.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/17463306/"
        }
    },

    "Personality & Behavior": {
        "rs1800955": {
            "Gene": "DRD4 promoter -521 C/T",
            "Effect": "T allele associated with lower DRD4 expression and higher novelty-seeking/impulsivity; C allele more reserved.",
            "Credibility": "Moderate – some studies report strong novelty-seeking links, others less so.",
            "Source": "https://onlinelibrary.wiley.com/doi/10.1002/ajmg.1328"
        },
        "rs53576": {
            "Gene": "OXTR A/G",
            "Effect": "G allele correlates with greater empathy, sociability, secure attachment; A allele linked to lower trust/emotional recognition.",
            "Credibility": "High – replicated associations with social behavior and empathy.",
            "Source": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3613434/"
        },
        "rs25531": {
            "Gene": "5-HTTLPR L-G allele",
            "Effect": "A variant in the serotonin transporter promoter. The G in L_G reduces expression, acting like the S allele (linked to anxiety).",
            "Credibility": "High – well known in anxiety/depression genetics (5-HTTLPR/rs25531).",
            "Source": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4153876/"
        },
        "rs6265": {
            "Gene": "BDNF Val66Met",
            "Effect": "Met allele reduces BDNF secretion, associated with higher anxiety and harm avoidance.",
            "Credibility": "High – robustly studied in anxiety and personality contexts.",
            "Source": "http://blog.23andme.com/2009/10/30/snpwatch-the-bad-driving-gene/"
        },
        "rs1800497": {
            "Gene": "ANKK1/DRD2 Taq1A",
            "Effect": "T (A1) allele linked to fewer D2 receptors, higher addiction risk, and impulsivity/reward craving.",
            "Credibility": "Moderate – well-known in addiction studies; also tied to personality traits.",
            "Source": "https://www.frontiersin.org/articles/10.3389/fpsyt.2017.00279/full"
        },
        "rs1799732": {
            "Gene": "DRD2 -141C Ins/Del",
            "Effect": "Deletion allele reduces D2 expression, associated with increased schizophrenia risk and possibly lower novelty-seeking in healthy individuals.",
            "Credibility": "Moderate – known effect on DRD2 levels; personality link not fully confirmed.",
            "Source": "https://www.nature.com/articles/s41398-018-0295-9"
        },
        "rs1611115": {
            "Gene": "DBH -1021C>T",
            "Effect": "T allele greatly lowers DBH enzyme (norepinephrine production). Linked to higher dopamine, sensation-seeking, and low BP.",
            "Credibility": "High – strong biochemical effect; some behavioral correlations reported.",
            "Source": "https://academic.oup.com/ijnp/article/8/2/255/642070"
        },
        "rs1042778": {
            "Gene": "OXTR",
            "Effect": "Certain genotypes (GG) linked to greater altruism/trust in social tasks; TT or GT can show less prosocial behavior.",
            "Credibility": "Moderate – associations with empathy/generosity in some studies.",
            "Source": "https://www.frontiersin.org/articles/10.3389/fpsyg.2014.00089/full"
        },
        "rs2770304": {
            "Gene": "RPTOR",
            "Effect": "A allele associated with higher subjective wellbeing (optimism) in a large study.",
            "Credibility": "Moderate – found in a GWAS for wellbeing but needs replication.",
            "Source": "https://www.nature.com/articles/ng.3431"
        },
        "rs324420": {
            "Gene": "FAAH Pro129Thr",
            "Effect": "A (Thr129) reduces FAAH activity, raising endocannabinoid levels. Linked to lower anxiety and better fear extinction.",
            "Credibility": "Moderate – functional effect is known; human behavioral evidence growing.",
            "Source": "https://www.pnas.org/content/112/52/16369"
        },
        "rs1076560": {
            "Gene": "DRD2",
            "Effect": "Intron variant altering D2 receptor splicing. T allele shifts toward D2(short) isoform, possibly linked to higher creativity and extraversion.",
            "Credibility": "Moderate – neuroimaging support; personality links need more study.",
            "Source": "https://www.nature.com/articles/mp201110"
        },
        "rs1044396": {
            "Gene": "CHRNA4",
            "Effect": "C allele associated with better attentional performance, possibly lower nicotine dependence risk; T allele carriers may have faster habituation.",
            "Credibility": "Moderate – some links to attention tasks found in studies.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/17369183/"
        },
        "rs4680": {
            "Gene": "COMT Val158Met",
            "Effect": "Met allele (“worrier”) increases dopamine in PFC, associated with higher anxiety and neuroticism. Val (“warrior”) may handle stress better.",
            "Credibility": "High – well replicated for effects on stress response.",
            "Source": "http://blog.23andme.com/2008/08/10/snpwatch-genetic-variant-may-increase-risk-for-anxiety-disorders/"
        },
        "rs644148": {
            "Gene": "GRM3",
            "Effect": "A metabotropic glutamate receptor variant. The C allele has been linked to impulsivity and schizophrenia risk in some reports.",
            "Credibility": "Low/Moderate – limited evidence, needs further validation.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/16801953/"
        }
    },

    "Pain Sensitivity & Dental Anesthesia": {
        "rs6746030": {
            "Gene": "SCN9A (Nav1.7) R1150W",
            "Effect": "A allele linked to reduced pain sensitivity and higher pain tolerance in some chronic pain studies.",
            "Credibility": "Moderate – SCN9A mutations alter pain perception; this common variant has mild effects.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/19786535/"
        },
        "rs1805007": {
            "Gene": "MC1R R151C",
            "Effect": "Red-hair variant. Carriers often need more dental anesthetic and have altered pain sensitivity to some stimuli.",
            "Credibility": "High – multiple studies confirm differences in anesthesia requirements for redheads.",
            "Source": "https://academic.oup.com/jac/article/67/7/1803/791139"
        },
        "rs2229944": {
            "Gene": "SCN9A (Nav1.7) V1184A",
            "Effect": "Minor allele may reduce channel activity slightly, contributing to higher pain tolerance.",
            "Credibility": "Moderate – SCN9A key in pain; evidence is growing for this SNP.",
            "Source": "https://onlinelibrary.wiley.com/doi/full/10.1002/ejp.882"
        },
        "rs6777055": {
            "Gene": "TAFA1",
            "Effect": "Minor allele carriers needed higher lidocaine doses in one dental GWAS, suggesting lower anesthesia efficacy.",
            "Credibility": "Low/Preliminary – single study with modest sample.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/20428735/"
        },
        "rs4793665": {
            "Gene": "COMT 3' UTR",
            "Effect": "A allele linked to higher pain scores, independent of Val158Met. Affects COMT haplotype function.",
            "Credibility": "Moderate – COMT haplotypes can modulate pain processing.",
            "Source": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2755808/"
        },
        "rs11127292": {
            "Gene": "CACNG2 (stargazin)",
            "Effect": "Linked to chronic back pain modulation; one allele showed reduced pain intensity in a study.",
            "Credibility": "Low – single report, not widely replicated.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/20817052/"
        },
        "rs243865": {
            "Gene": "MMP2 promoter",
            "Effect": "T allele upregulates MMP2 expression, possibly reducing disc degeneration pain risk (enhanced tissue remodeling).",
            "Credibility": "Moderate – known effect on enzyme expression; pain relevance under study.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/19714588/"
        },
        "rs4680": {
            "Gene": "COMT Val158Met",
            "Effect": "Met/Met generally correlates with higher pain sensitivity and more analgesic requirement than Val/Val.",
            "Credibility": "High – consistent findings in pain and analgesia research.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/16763601/"
        },
        "rs10875995": {
            "Gene": "OPRM1 promoter",
            "Effect": "A allele linked to higher μ-opioid receptor expression and possibly higher pain threshold.",
            "Credibility": "Low – less studied than coding OPRM1 SNPs, but initial results suggest an effect.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/25929681/"
        },
        "rs7835529": {
            "Gene": "TAOK3",
            "Effect": "Associated with higher morphine requirements after pediatric surgery, implying more post-op pain.",
            "Credibility": "Moderate – found in a GWAS of children's pain medication needs.",
            "Source": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4531117/"
        },
        "rs12414487": {
            "Gene": "CACNA1E",
            "Effect": "Linked to reduced cold pain sensitivity in one study. The C allele correlated with lower pain from cold stimuli.",
            "Credibility": "Low – needs more validation.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/25084033/"
        },
        "rs2234922": {
            "Gene": "MC1R R160W",
            "Effect": "Another red-hair allele. Carriers frequently exhibit altered responses to local anesthetics and pain sensitivity.",
            "Credibility": "High – consistent with MC1R’s known role in pain modulation.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/16870642/"
        },
        "rs80358206": {
            "Gene": "MC1R D294H",
            "Effect": "A less common MC1R loss-of-function variant; similar red-hair/pain modulation traits.",
            "Credibility": "High – MC1R loss-of-function alleles robustly linked to pain differences.",
            "Source": "https://www.mdpi.com/2079-7737/9/12/472"
        }
    },

    "Unbreakable Bones (Bone Density/Strength)": {
        "rs556442": {
            "Gene": "LRP4",
            "Effect": "T allele associated with higher bone mineral density in some GWAS, possibly contributing to stronger bones.",
            "Credibility": "Moderate – LRP4 is a known bone formation regulator.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/21990264/"
        },
        "rs1021188": {
            "Gene": "WNT16",
            "Effect": "G allele strongly linked to higher cortical bone density and lower fracture risk.",
            "Credibility": "High – well replicated in large bone density GWAS.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/22504420/"
        },
        "rs3736228": {
            "Gene": "LRP5 Val667Met",
            "Effect": "T allele (Met) associated with lower bone density and higher fracture risk; C (Val) is protective.",
            "Credibility": "High – LRP5 is key in bone mass regulation, validated in multiple populations.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/20205168/"
        },
        "rs699": {
            "Gene": "AGT Met235Thr",
            "Effect": "T allele (Thr235) can be linked to higher angiotensin II, potentially influencing bone density indirectly. C (Met235) may favor higher BMD.",
            "Credibility": "Moderate – some studies suggest a small bone effect alongside blood pressure.",
            "Source": "https://www.sciencedirect.com/science/article/pii/S0378512210003242"
        },
        "rs2073618": {
            "Gene": "TNFRSF11B (OPG)",
            "Effect": "G allele associated with higher OPG levels and possibly higher bone density, protective against osteoporosis.",
            "Credibility": "Moderate – multiple studies in postmenopausal women; results vary somewhat.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/19172234/"
        },
        "rs4792909": {
            "Gene": "RANKL",
            "Effect": "T allele associated with lower RANKL expression and higher bone density (identified in men with high bone mass).",
            "Credibility": "Moderate – part of the RANK/RANKL/OPG bone pathway.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/20205168/"
        },
        "rs731236": {
            "Gene": "VDR TaqI",
            "Effect": "C allele (t allele) has been linked to slightly higher BMD and lower fracture risk, though findings are inconsistent.",
            "Credibility": "Moderate – widely studied; effect sizes are typically small.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/25516418/"
        },
        "rs4870044": {
            "Gene": "ESR1",
            "Effect": "One genotype correlated with higher peak bone mass in young adults, modulating estrogen sensitivity in bone.",
            "Credibility": "Low/Moderate – ESR1’s significance is established, but this SNP’s specific effect is less confirmed.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/16166218/"
        },
        "rs9533090": {
            "Gene": "SP7 (Osterix)",
            "Effect": "A variant near SP7 transcription factor. A allele linked to increased bone density in a large GWAS.",
            "Credibility": "High – identified in an osteoporosis-focused genome-wide study.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/20004881/"
        },
        "rs2273061": {
            "Gene": "FDPS",
            "Effect": "T allele associated with better response to bisphosphonates and possibly higher baseline BMD.",
            "Credibility": "Moderate – pharmacogenetic evidence in bone density treatment.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/19453261/"
        },
        "rs2297480": {
            "Gene": "SOST",
            "Effect": "G allele may lower sclerostin levels, leading to higher bone mass (since sclerostin inhibits bone formation).",
            "Credibility": "Moderate – consistent with sclerostin’s role, supported by some genetic studies.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/21311589/"
        },
        "rs11246615": {
            "Gene": "FGFR1",
            "Effect": "A allele observed in individuals with unusually high bone density in an outlier study.",
            "Credibility": "Low – preliminary finding; FGFR1 is involved in bone development.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/27235450/"
        },
        "rs678849": {
            "Gene": "COL1A1",
            "Effect": "T allele in intron region linked to better collagen stability and lower fracture risk in some cohorts.",
            "Credibility": "Moderate – COL1A1 is crucial for bone quality, but data on this SNP are limited.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/16491285/"
        },
        "rs87938": {
            "Gene": "LOX",
            "Effect": "C allele potentially increases collagen cross-linking and bone stiffness. Found in one athlete study.",
            "Credibility": "Low – early research linking LOX variant to bone material quality.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/28777264/"
        }
    },

    "Sense of Smell & Taste Sensitivity": {
        "rs72921001": {
            "Gene": "OR6A2",
            "Effect": "Associated with cilantro aversion. C allele perceives a strong soapy taste, leading to dislike of cilantro.",
            "Credibility": "High – found in a large consumer genetics study.",
            "Source": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3637050/"
        },
        "rs713598": {
            "Gene": "TAS2R38 (Ala49Pro)",
            "Effect": "Part of the PTC/PROP bitter-taster genotype. C allele is in the 'taster' haplotype (PAV).",
            "Credibility": "High – classic phenotype-genotype correlation for bitter taste.",
            "Source": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3043155/"
        },
        "rs10246939": {
            "Gene": "TAS2R38 (Val262Ala)",
            "Effect": "Another site in TAS2R38 defining bitter taste. A allele helps form the PAV (taster) haplotype.",
            "Credibility": "High – part of the standard bitter-taster polymorphisms.",
            "Source": "https://academic.oup.com/chemse/article/33/8/685/408546"
        },
        "rs10772420": {
            "Gene": "OR10G4",
            "Effect": "Linked to perception of certain floral scents. One allele confers heightened detection of lily-like odors.",
            "Credibility": "Moderate – found in an exploratory odor perception study.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/28416804/"
        },
        "rs2031920": {
            "Gene": "CYP2E1*1F",
            "Effect": "A promoter SNP affecting enzyme induction. Some evidence links it to differences in sweet preference (via ethanol metabolism).",
            "Credibility": "Low – primarily known for drug metabolism, taste link is peripheral.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/11179016/"
        },
        "rs2274325": {
            "Gene": "TRPV1",
            "Effect": "T allele linked to higher sensitivity to spicy heat (capsaicin). Carriers perceive chili burn more strongly.",
            "Credibility": "Moderate – smaller studies show genotype differences.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/17891356/"
        },
        "rs6489730": {
            "Gene": "OR5AN1",
            "Effect": "Affects detection of trimethylamine (fishy odor). Some alleles make the scent stronger while others barely smell it.",
            "Credibility": "Moderate – identified in trimethylaminuria perception research.",
            "Source": "https://www.monell.org/news/news_releases/smell_fish_odor_genetics"
        },
        "rs2897475": {
            "Gene": "OR2J3",
            "Effect": "Associated with androstenone (musky odor) perception. Certain genotypes find it foul, others sweet or odorless.",
            "Credibility": "High – classic study showing receptor variants alter androstenone smell.",
            "Source": "https://www.nature.com/articles/nature06162"
        },
        "rs11574663": {
            "Gene": "TAS1R2",
            "Effect": "A SNP in the sweet receptor subunit. A allele linked to reduced sweet sensitivity (need higher sugar concentration).",
            "Credibility": "Moderate – some taste preference associations.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/23342145/"
        },
        "rs457567": {
            "Gene": "ANKH",
            "Effect": "Variant possibly linked to 'supertaster' status for certain bitter compounds. Evidence is preliminary.",
            "Credibility": "Low – requires more study.",
            "Source": "N/A (preliminary finding)"
        },
        "rs16969968": {
            "Gene": "CHRNA5 Asp398Asn",
            "Effect": "Primarily known for smoking behavior. A allele also associated with greater bitterness perception of nicotine.",
            "Credibility": "High – strong link to nicotine dependence; taste aspect is secondary.",
            "Source": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3316517/"
        },
        "rs34160932": {
            "Gene": "OR7D4",
            "Effect": "Compound haplotype influences androstenone odor perception (foul vs. sweet/odorless). 'RT/RT' genotype strongly detects sweat odor.",
            "Credibility": "High – well-documented differences in androstenone smell detection.",
            "Source": "https://www.nature.com/articles/nature06162"
        }
    },

    "Cold Tolerance & Heat Sensitivity": {
        "rs1800592": {
            "Gene": "UCP1 -3826A>G",
            "Effect": "G allele increases UCP1 expression and thermogenesis, improving cold tolerance. A allele linked to lower heat production.",
            "Credibility": "Moderate – consistent effect on UCP1; population data on cold adaptation vary.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/14671210/"
        },
        "rs10166942": {
            "Gene": "TRPM8",
            "Effect": "C allele associated with greater cold sensitivity and 'cold pain' at lower temperatures; T allele more tolerant.",
            "Credibility": "Moderate – TRPM8 is the main cold receptor, genotype differences observed in humans.",
            "Source": "https://onlinelibrary.wiley.com/doi/full/10.1002/cjas.140"
        },
        "rs174570": {
            "Gene": "FADS1/FADS2 Arctic-adapted allele",
            "Effect": "Derived allele found in Greenland Inuit, optimizing fatty acid metabolism for high-fat marine diets in cold. Reduces inflammatory omega-6.",
            "Credibility": "High – strong selection signal in Inuit genomes.",
            "Source": "https://science.sciencemag.org/content/349/6254/1343"
        },
        "rs1137101": {
            "Gene": "LEPR Gln223Arg",
            "Effect": "A allele (Arg223) lowers leptin sensitivity, linked to higher fat mass (potentially better insulation).",
            "Credibility": "Moderate – well studied in obesity; cold insulation aspect is speculative.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/18053316/"
        },
        "rs1801260": {
            "Gene": "CLOCK 3111T/C",
            "Effect": "C allele associated with evening preference and altered circadian temperature rhythm. Possibly more heat sensitivity later in the day.",
            "Credibility": "Moderate – well-known in sleep research; temperature link is indirect.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/12270977/"
        },
        "rs1408799": {
            "Gene": "ADRβ3 (nearby variant)",
            "Effect": "May influence basal metabolic rate and non-shivering thermogenesis. Data are limited.",
            "Credibility": "Low – not well characterized for direct cold adaptation.",
            "Source": "N/A"
        },
        "rs601339": {
            "Gene": "TH (tyrosine hydroxylase)",
            "Effect": "An allele that may affect NE production during cold stress, impacting blood pressure response.",
            "Credibility": "Low – evidence is minimal; more research needed.",
            "Source": "N/A"
        },
        "rs925847": {
            "Gene": "UCP3",
            "Effect": "A variant associated with increased resting metabolic rate under cold conditions in a small study.",
            "Credibility": "Low/Moderate – UCP3’s role in muscle thermogenesis is plausible.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/14570764/"
        },
        "rs1205": {
            "Gene": "CRP",
            "Effect": "C allele associated with lower baseline CRP. Potentially less inflammation in cold stress, but not a direct cold-tolerance mechanism.",
            "Credibility": "Moderate – well-known effect on CRP levels; cold-related data are indirect.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/19193623/"
        }
    },

    "Do You Have 'Superhero' DNA?": {
        "rs121913625": {
            "Gene": "PCSK9 null mutation",
            "Effect": "Loss-of-function. Carriers have very low LDL (~40-80% lower) and near immunity to coronary heart disease.",
            "Credibility": "High – discovered in the Dallas Heart Study, led to PCSK9 inhibitor drugs.",
            "Source": "https://www.nejm.org/doi/full/10.1056/NEJMoa040583"
        },
        "rs7463708": {
            "Gene": "HBB",
            "Effect": "G allele linked to elevated fetal hemoglobin levels, reducing sickle cell disease severity and improving oxygen carrying.",
            "Credibility": "Moderate – beneficial modulator in sickle cell patients.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/21957107/"
        },
        "rs2229611": {
            "Gene": "ESR2",
            "Effect": "An estrogen receptor beta variant. Certain genotypes correlated with longevity and better stress resistance.",
            "Credibility": "Low/Moderate – preliminary findings in centenarian studies.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/20156215/"
        },
        "rs1805086": {
            "Gene": "MSTN K153R",
            "Effect": "A (Arg153) allele slightly reduces myostatin’s inhibition of muscle growth, leading to more muscle mass.",
            "Credibility": "Moderate – rare but observed more in power athletes.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/18506300/"
        },
        "rs1042713": {
            "Gene": "ADRB2 Arg16",
            "Effect": "Sometimes considered performance-enhancing. Arg16 allele has been linked to better lung function/endurance capacity.",
            "Credibility": "Moderate – well-studied in exercise physiology.",
            "Source": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5651752/"
        },
        "rs11549465": {
            "Gene": "HIF1A Pro582Ser",
            "Effect": "T (Ser582) can help at altitude (enhanced hypoxic response). Possibly beneficial for elite endurance.",
            "Credibility": "Moderate – observed in some athlete studies.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/21440961/"
        },
        "rs2234693": {
            "Gene": "ESR1 PvuII",
            "Effect": "C allele associated with higher bone density and possibly better muscle recovery (a beneficial 'pp' genotype).",
            "Credibility": "Moderate – known in osteoporosis meta-analyses.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/16275960/"
        },
        "rs11568820": {
            "Gene": "FOXO3",
            "Effect": "G allele enriched in centenarians, linked to longevity and stress resistance via higher FOXO3 expression.",
            "Credibility": "High – multiple studies confirm FOXO3's role in healthy aging.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/18765803/"
        },
        "rs2239681": {
            "Gene": "CHEK2",
            "Effect": "Some rare CHEK2 variants enhance DNA repair, lowering cancer risk. This SNP’s T allele may have protective effect.",
            "Credibility": "Moderate – CHEK2 is a known tumor suppressor; data on this specific variant are limited.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/20301390/"
        },
        "rs12722": {
            "Gene": "COL5A1",
            "Effect": "CC genotype can confer stronger tendons and reduced injury risk (a 'superhero' advantage).",
            "Credibility": "Moderate – multiple studies on ligament injuries link T allele to higher injury risk.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/21227893/"
        },
        "rs13946": {
            "Gene": "COL5A1",
            "Effect": "Part of the protective haplotype with rs12722. The C allele helps reduce ligament rupture risk.",
            "Credibility": "Moderate – typically studied in combination with rs12722.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/21227893/"
        },
        "rs72613567": {
            "Gene": "HSD17B13",
            "Effect": "TA insertion allele protects against fatty liver disease (NAFLD/NASH). ~30% lower risk even under risk factors.",
            "Credibility": "High – a major finding in large liver disease studies.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/30290149/"
        },
        "rs4341": {
            "Gene": "ACE (I/D proxy)",
            "Effect": "A allele tags the 'I' version linked to lower ACE levels, better endurance, and potential longevity benefits.",
            "Credibility": "Moderate – ACE I allele appears more in centenarians and endurance athletes.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/12529356/"
        }
    },

    "Ancestry & Ancient DNA Traits": {
        "rs1421085": {
            "Gene": "FTO",
            "Effect": "A variant frequent in Eurasian populations, potentially under selection for energy storage during famines.",
            "Credibility": "Moderate – geographical distribution known; selection reasons are debated.",
            "Source": "https://www.cell.com/ajhg/fulltext/S0002-9297(09)00173-3"
        },
        "rs1042779": {
            "Gene": "SLC24A5",
            "Effect": "One of the key pigmentation alleles (though the main site is rs1426654). Lightens skin in Europeans.",
            "Credibility": "High – SLC24A5 is crucial for light skin adaptation in high latitudes.",
            "Source": "https://en.wikipedia.org/wiki/SLC24A5"
        },
        "rs1864325": {
            "Gene": "TBX15 region (Inuit adaptation)",
            "Effect": "Associated with cold adaptation and fat distribution in Greenland Inuit. Derived allele helps handle Arctic diet.",
            "Credibility": "Moderate – from a Greenlandic Inuit genome study.",
            "Source": "https://science.sciencemag.org/content/349/6254/1343"
        },
        "rs373863828": {
            "Gene": "EPAS1 (HIF2α)",
            "Effect": "A high-altitude adaptation variant in Tibetans, from Denisovan introgression. Improves oxygen use under hypoxia.",
            "Credibility": "High – one of the strongest known selection signals in Tibetans.",
            "Source": "https://www.nature.com/articles/nature13408"
        },
        "rs731236": {
            "Gene": "VDR TaqI",
            "Effect": "Associated with vitamin D receptor variations; distribution differs among latitudes, possibly for UV adaptation.",
            "Credibility": "Moderate – widely studied in bone and possible latitude-based selection.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/9392426/"
        },
        "rs2229611": {
            "Gene": "ESR2",
            "Effect": "Minor allele frequencies vary among populations; proposed association with longevity in some groups.",
            "Credibility": "Low/Moderate – not definitively linked to ancient selection.",
            "Source": "N/A"
        },
        "rs1885325": {
            "Gene": "ABCC11 region",
            "Effect": "Linked to dry earwax phenotype common in East Asians. Strong population frequency difference.",
            "Credibility": "Moderate – earwax type as an ethnic marker.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/17256055/"
        },
        "rs16891982": {
            "Gene": "SLC45A2 (L374F)",
            "Effect": "C allele (Leu374) significantly lightens skin. Nearly fixed in Europeans; strongly selected in West Eurasia.",
            "Credibility": "High – major contributor to light skin.",
            "Source": "https://en.wikipedia.org/wiki/SLC45A2"
        },
        "rs3827760": {
            "Gene": "EDAR V370A",
            "Effect": "T allele (370A) predominant in East Asians/Native Americans. Causes thicker hair, more sweat glands, shovel incisors.",
            "Credibility": "High – textbook example of recent positive selection.",
            "Source": "https://www.science.org/doi/10.1126/science.1133900"
        },
        "rs17300539": {
            "Gene": "HYAL2 (Tibetan adaptation)",
            "Effect": "A SNP found at higher frequency in Tibetan populations, possibly affecting RBC count at altitude.",
            "Credibility": "Moderate – identified in a selection scan, less studied than EPAS1.",
            "Source": "https://www.pnas.org/content/114/16/4183"
        },
        "rs1834640": {
            "Gene": "OCA2/HERC2 region",
            "Effect": "In LD with the main blue-eye variant; T allele correlates with light eye color in Northern Europeans.",
            "Credibility": "High – part of the well-known HERC2/OCA2 pigmentation haplotype.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/18252222/"
        },
        "rs4939827": {
            "Gene": "SMAD7",
            "Effect": "An allele common in Europeans, associated with colorectal cancer risk. Possibly under selection historically.",
            "Credibility": "Moderate – known health effect; ancestry-related distribution patterns.",
            "Source": "https://pubmed.ncbi.nlm.nih.gov/18372901/"
        },
        "rs17822931": {
            "Gene": "ABCC11 538G>A",
            "Effect": "Determines dry vs. wet earwax. The A allele (common in East Asians) leads to dry earwax and less underarm odor.",
            "Credibility": "High – a famous genetic difference across ethnic groups.",
            "Source": "https://www.nature.com/articles/jhg200810"
        },
        "rs80358206": {
            "Gene": "MC1R (ancient variant)",
            "Effect": "Found in some archaic humans (e.g. Neanderthals) related to red hair/pale skin. Rare in modern populations.",
            "Credibility": "Moderate – known from ancient DNA studies.",
            "Source": "https://www.science.org/doi/10.1126/science.1147417"
        }
    }
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
                for line in snps[trait][snp]:
                    print(snps[trait][snp][line])
                
            else:
                print(f"No snp:{snp} found.")

    
cur.close()
con.close()
