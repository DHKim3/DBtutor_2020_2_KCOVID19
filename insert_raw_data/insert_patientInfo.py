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

#case_list = []
with open("./data/PatientInfo.csv", 'r') as file:
    file_read = csv.reader(file)

    for i,line in enumerate(file_read):
        
        if not i:                           #Skip first line
            continue              
        
        for lidx, c in enumerate(line):
            if (not len(c)) or (c =='-'):
                line[lidx] = None
            else:
                line[lidx] = line[lidx].strip()

        patient_id = line[0]                                    #patient_id 
        sex = line[1]                                           #sex
        age = line[2]                                           #age
        country = line[3]                                       #country
        province = line[4]                                      #province
        city = line[5]                                          #city
        infection_case = line[6]                                #infection_case
        infected_by = line[7]                                   #infected_by
        contact_number = line[8]                                #contact_number
        symptom_onset_date = line[9]                            #symptom_onset_date
        confirmed_date = line[10]                               #confirmed_date
        released_date = line[11]                                #released_date
        deceased_date = line[12]                                #deceased_date
        state   = line[13]                                      #state

        query = """INSERT INTO `patientInfo`(patient_id,sex,age,country,province,city,infection_case,infected_by,contact_number,symptom_onset_date,confirmed_date,released_date,deceased_date,state) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        sql_data = (patient_id, sex,age,country,province,city,infection_case,infected_by,contact_number,symptom_onset_date,confirmed_date,released_date,deceased_date,state)
        
        #for debug
        try:
            cursor.execute(query, sql_data)
            print("[OK] Inserting [%s] to PATIENTINFO"%(patient_id))
        except (pymysql.Error, pymysql.Warning) as e :
            # print("[Error]  %s"%(pymysql.IntegrityError))
            if e.args[0] == 1062: continue
            print('[Error] %s | %s'%(patient_id,e))


conn.commit()
cursor.close()




# import pandas as pd

# # convert case_name into case_id by using province and infected_by
# def case_name2case_id(case_name,infected_by):
    
#     df = pd.read_csv("./Case.csv", usecols = ["case_id", "infection_case"])

#     print(df)

#     return