import csv
import pymysql
conn = pymysql.connect(host="localhost",port=8889, user="root", password="@ehdgml12",db="K_COVID19", charset="utf8")
cursor = conn.cursor()

f = open('./data/Time.csv','r')

csvReader = csv.reader(f)


for i,row in enumerate(csvReader):

    if not i:
        continue
    
    for lidx, c in enumerate(row):
        if(not len(c) or ( c=="-")):
            row[lidx] = None
        else:
            row[lidx]=row[lidx].strip()
            
    print(i)     
    date = row[0]
    time = row[1]
    test = row[2]
    negative = row[3]
    confirmed = row[4]
    released = row[5]
    deceased = row[6]
    
    sql = """Insert into time_info  (date, time, test, negative, confirmed , released , deceased ) values ( %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(sql, (date, time, test, negative , confirmed , released, deceased))
    
conn.commit()
f.close()
conn.close()