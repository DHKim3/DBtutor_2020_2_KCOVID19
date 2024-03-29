# -*- coding: utf-8 -*- 
import pymysql
import csv

#mysql server 연결, port 및 host 주의!
conn = pymysql.connect(host='localhost',
                        port = 3306,
                        user='root', 
                        password='julie0928K!', 
                        db='K_COVID19', 
                        charset='utf8')

# Connection 으로부터 Cursor 생성
cursor = conn.cursor()

# 중복된 case 제거를 위해 checking list
region_code = []
with open("../combine/K_COVID19.csv", 'r') as file:
    file_read = csv.reader(file)

    # Use column 18(case_id), 5(province), 19(case_city), 20(infection_group), 7(infection_city), 21(confirmed), 22(case_latitude), 23(case_longitude)
    # index = column - 1
    col_list = { 
        'region_code' :23,
        'province' :4,
        'city' : 5,
        'latitude' :24,
        'longitude' : 25,
        'elementary_school_count' :26,
        'kindergarten_count' : 27,
        'university_count' : 28,
        'academy_ratio' : 29,
        'elderly_population_ratio' : 30,
        'elderly_alone_ratio' : 31,
        'nursing_home_count' : 32
    }

    for i,line in enumerate(file_read):

        #Skip first line
        if not i:                           
            continue

        # checking duplicate case_id & checking case_id == "NULL"
        if (line[col_list['region_code']] in region_code) or (line[col_list['region_code']] == "NULL") :
            continue
        else:
            region_code.append(line[col_list['region_code']])

        #make sql data & query
        sql_data = []
        #"NULL" -> None (String -> null)
        for idx in col_list.values() :
            if line[idx] == "NULL" :
                line[idx] = None
            else:
                line[idx] = line[idx].strip()

            sql_data.append(line[idx])

        query = """INSERT INTO `region`(region_code, province, city, latitude, longitude, elementary_school_count, kindergarten_count, university_count, academy_ratio, elderly_population_ratio, elderly_alone_ratio, nursing_home_count) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        sql_data = tuple(sql_data)

        #for debug
        try:
            cursor.execute(query, sql_data)
            print("[OK] Inserting [%s] to region"%(line[col_list['region_code']]))
        except (pymysql.Error, pymysql.Warning) as e :
            # print("[Error]  %s"%(pymysql.IntegrityError))
            if e.args[0] == 1062: continue
            print('[Error] %s | %s'%(line[col_list['region_code']],e))
            break

conn.commit()
cursor.close()

print(len(region_code))