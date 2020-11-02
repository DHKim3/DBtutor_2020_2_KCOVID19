import csv
import pymysql



#mysql server 연결, port 및 host 주의!
conn = pymysql.connect(host='localhost',
                        port = 3306,
                        user='root', 
                        password='julie0928K!', 
                        db='K_COVID19', 
                        charset='utf8')

# Connection 으로부터 Cursor 생성
cursor = conn.cursor()

with open("./data/Case.csv", 'r') as file:
    file_read = csv.reader(file)

    for i,line in enumerate(file_read):
        
        if not i:                           #Skip first line
            continue              
        
        for lidx, c in enumerate(line):
            if (not len(c)) or (c =='-'):
                line[lidx] = None
            else:
                line[lidx] = line[lidx].strip()

        case_id = line[0]                   #case_id 
        province = line[1]                  #province
        city = line[2]                      #city

        #infection_group
        if line[3] == "TRUE":
            line[3] = True
        else:
            line[3] = False
        infection_group = line[3]   
            
        infection_case = line[4]            #infection_case
        confirmed = line[5]                 #confirmed
        langtitude = line[6]                #langtitude
        longitude = line[7]                 #longitude

        query = """INSERT INTO `caseInfo`(case_id, province, city, infection_group, infection_case, confirmed, latitude, longitude) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
        sql_data = (case_id, province, city, infection_group, infection_case, confirmed, langtitude, longitude)
        
        #for debug
        try:
            cursor.execute(query, sql_data)
            print("[OK] Inserting [%s] to CaseINFO"%(case_id))
        except (pymysql.Error, pymysql.Warning) as e :
            # print("[Error]  %s"%(pymysql.IntegrityError))
            if e.args[0] == 1062: continue
            print('[Error] %s | %s'%(case_id,e))
            break


conn.commit()
cursor.close()
