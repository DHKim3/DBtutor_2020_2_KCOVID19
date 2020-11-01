import csv
import pymysql



conn = pymysql.connect(host="localhost",port=8889, user="root", password="@ehdgml12",db="K_COVID19", charset="utf8")
cursor = conn.cursor()

f = open('./data/Region.csv','r')

csvReader = csv.reader(f)


for i,row in enumerate(csvReader):

    if not i:
        continue

    code = row[0]
    #province = "'{}'".format(row[1])
    province = row[1]
    #city = "'{}'".format(row[2])
    city = row[2]
    latitude = row[3]
    longtitude = row[4]
    elementary_school_count = row[5]
    kindergarten_count = row[6]
    university_count = row[7]
    academy_ratio = row[8]
    elderly_population_ratio = row[9]
    elderly_alone_ratio = row[10]
    nursing_home_count = row[11]
    print( code, province, city, latitude, longtitude, elementary_school_count, kindergarten_count, university_count, academy_ratio, elderly_population_ratio, elderly_alone_ratio, nursing_home_count)


    region_var = "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s"%(code, '"{}"'.format(province), '"{}"'.format(city), latitude, longtitude, elementary_school_count, kindergarten_count, university_count,academy_ratio, elderly_population_ratio, elderly_alone_ratio,nursing_home_count)
    #print(province +" "+ city)
    #sql = "insert into region (region_code, province, city, latitude, longtitude, elementary_school_count, kindergarten_count, university_count, academy_ratio, elderly_population_ratio, elderly_alone_ratio, nursing_home_count) values (%s %s %s %s %s %s %s %s %s %s %s %s)"
    sql = "Insert into region values(%s);"%region_var
    #cursor.execute(sql, (code,province,city,latitude,longtitude,elementary_school_count,kindergarten_count,university_count,academy_ratio,elderly_population_ratio, elderly_alone_ratio,nursing_home_count))
    cursor.execute(sql)
 
conn.commit()
f.close()
conn.close()