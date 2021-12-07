import numpy as np
from Bio import Medline, Entrez  # 一般是通過BioPython的Bio.Entrez模組訪問Entrez
from collections import Counter
 
Entrez.email = "p77101032@gs.ncku.edu.tw"  # 應用自己的賬號訪問NCBI資料庫
 
 # 此處需將伺服器協議指定為1.0，否則會出現報錯。http.client.IncompleteRead: IncompleteRead(0 bytes read)
 # 伺服器http協議1.0，而python的是1.1，解決辦法就是指定客戶端http協議版本
import http.client
http.client.HTTPConnection._http_vsn = 10
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'
 
'''
14 Entrez 是一個檢索系統，可以用其訪問NCBI資料庫，比如說PubMed，GenBank，GEO等。
15 獲得有關 global PBDE 的所有文獻的PubMed IDs
16 
'''
keyword = "Dysautonomia"
#keyword = "COVID-19"

# handle_0 = Entrez.esearch(db="pubmed", term="drug therapy[Subheading] AND adverse effects[Subheading] AND humans[MeSH Terms]", retmax=306431)
handle_0 = Entrez.esearch(db="pubmed", term=str(keyword) + " AND (1990/01/01[Date - Publication] : 2022/11/7[Date - Publication]",
                           ptyp="Review", usehistory="y", retmax=400)
record = Entrez.read(handle_0)  # 獲取檢索條件的所有文獻
idlist = record["IdList"]  # 提取出文獻id
print ("Total: ", record["Count"])
No_Papers = len(idlist)    # 共306431篇文獻 2000-01-01:2021-12-31
webenv = record['WebEnv']
query_key = record['QueryKey']

total = No_Papers
step = 1
i =1
print("Result items:", total)

for start in range(0, total, step):
    with open("./dataset/"+str(keyword)+"_" + str(step*i) +".txt", 'w') as f:
        print("Download record %i to %i" % (start + 1, int(start + step)))
        handle_1 = Entrez.efetch(db="pubmed", retstart=start, rettype="medline", retmode="text",
                                 retmax=step, webenv=webenv, query_key=query_key)  # 獲取上述所有文獻的PubMed IDs
        records = Medline.parse(handle_1)
        records = list(records)  # 將迭代器轉換至列表（list）
        for index in np.arange(len(records)):
            id = records[index].get("PMID", "?")
            title = records[index].get("TI", "?")
            title = title.replace('[', '').replace('].', '')  # 若提取的標題出現[].符號，則去除
            abstract = records[index].get("AB", "?")
            #f.write(id)
            #f.write("\n")
            #f.write(title)
            #f.write("\n")
            f.write(abstract)
            f.write("\n")
        i += 1