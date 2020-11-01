#For Debug

show tables;

desc patientinfo;

select * from patientinfo as p where p.infection_case ="Itaewon Clubs" and p.province = "Seoul";
select count(*) from caseinfo;

DELETE FROM patientinfo;
drop table patientinfo;
drop table caseinfo;
desc Region;

desc infection;

drop database K_COVID19;  