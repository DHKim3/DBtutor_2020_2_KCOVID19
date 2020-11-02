import csv
import pymysql



conn = pymysql.connect(host="localhost",port=3306, user="root", password="julie0928K!",db="K_COVID19", charset="utf8")
cursor = conn.cursor()

f = open('./data/Weather.csv','r')

csvReader = csv.reader(f)


for i,row in enumerate(csvReader):

    if not i:
        continue
    
    for lidx, c in enumerate(row):
        if(not len(c) or ( c=="-")):
            row[lidx] = None
        else:
            row[lidx]=row[lidx].strip()
    
    # if (not len(row)) or (row =='-'):
    #     line[i] = None
    # else:
    #     line[i] = line[i].strip()

    print(i)
        
    code = row[0]
    province = row[1]
    date = row[2]
    avg_temp = row[3]
    min_temp = row[4]
    max_temp = row[5]

    
    sql = """Insert into weather  (region_code, province, wdate, avg_temp, min_temp, max_temp) values ( %s, %s, %s, %s, %s, %s )"""
    cursor.execute(sql, (code, province, date, avg_temp, min_temp, max_temp))
    
 
conn.commit()
f.close()
conn.close()