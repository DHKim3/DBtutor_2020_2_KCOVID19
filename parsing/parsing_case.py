import pymysql
import csv

#mysql server 연결, port 및 host 주의!
conn = pymysql.connect(host='localhost',
                        port = 8889,
                        user='root', 
                        password='@ehdgml12', 
                        db='K_COVID19', 
                        charset='utf8')

# Connection 으로부터 Cursor 생성
cursor = conn.cursor()

# 중복된 case 제거를 위해 checking list
case_id = []
with open("../combine/K_COVID19.csv", 'r') as file:
    file_read = csv.reader(file)

    # Use column 18(case_id), 5(province), 19(case_city), 20(infection_group), 7(infection_city), 21(confirmed), 22(case_latitude), 23(case_longitude)
    # index = column - 1
    col_list = { 
        'case_id' :17,
        'province' :4,
        'case_city' : 18,
        'infection_group' :19,
        'infection_case' : 6,
        'confirmed' :20,
        'case_latitude' : 21,
        'case_longitude' : 22 }

    for i,line in enumerate(file_read):

        #Skip first line
        if not i:                           
            continue

        # checking duplicate case_id & checking case_id == "NULL"
        if (line[col_list['case_id']] in case_id) or (line[col_list['case_id']] == "NULL") :
            continue
        else:
            case_id.append(line[col_list['case_id']])

        #make sql data & query
        sql_data = []
        #"NULL" -> None (String -> null)
        for idx in col_list.values() :
            if line[idx] == "NULL" :
                line[idx] = None
            else:
                line[idx] = line[idx].strip()

            sql_data.append(line[idx])

        query = """INSERT INTO `caseInfo`(case_id, province, city, infection_group, infection_case, confirmed, latitude, longitude) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
        sql_data = tuple(sql_data)

        #for debug
        try:
            cursor.execute(query, sql_data)
            print("[OK] Inserting [%s] to CaseINFO"%(line[col_list['case_id']]))
        except (pymysql.Error, pymysql.Warning) as e :
            # print("[Error]  %s"%(pymysql.IntegrityError))
            if e.args[0] == 1062: continue
            print('[Error] %s | %s'%(line[col_list['case_id']],e))
            break

conn.commit()
cursor.close()