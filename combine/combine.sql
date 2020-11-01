# for join

USE K_COVID19;

# 확진된 날짜의 지역에대한 날씨정보를 patientinfo를 기준으로 join.
# make new table called "result"
create table result AS (
select p.*,  w.avg_temp, w.min_temp, w.max_temp
from patientInfo as p
	Left OUTER JOIN weather as w ON w.province =p.province and w.wdate = p.confirmed_date
);
    

select re.* , i.case_id,i.city, i.infection_group,i.confirmed, i.langtitude, i.longitude, r.region_code, r.latitude, r.longitude, r.elementary_school_count,
r.kindergarten_count, r.university_count, r.academy_ratio, r.elderly_population_ratio, r.elderly_alone_ratio, r.nursing_home_count
from result as re 
	Left OUTER JOIN caseInfo as i ON i.infection_case = re.infection_case and i.province = re.province
    Left OUTER JOIN Region as r ON r.province = re.province and r.city = re.city;