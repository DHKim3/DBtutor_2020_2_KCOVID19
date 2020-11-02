create database K_COVID19;

show databases;

USE K_COVID19;

create table PatientInfo(
	patient_id BIGINT,
    sex VARCHAR(10),
    age VARCHAR(10),
    country VARCHAR(50),
    province VARCHAR(50),
    city VARCHAR(50),
    infection_case VARCHAR(50),
    infected_by BIGINT,
    contact_number INT,
    symptom_onset_date DATE,
    confirmed_date DATE,
    released_date DATE,
    deceased_date DATE,
    state VARCHAR(20),
    PRIMARY KEY(patient_id)
);

create table Region(
	region_code int,
    province VARCHAR(50),
    city VARCHAR(50),
    latitude float,
    longitude float,
    elementary_school_count int,
    kindergarten_count int,
    university_count int,
    academy_ratio float,
    elderly_population_ratio float,
    elderly_alone_ratio float,
    nursing_home_count int,
    PRIMARY KEY(region_code)
);

create table weather(
	region_code INT,
    province VARCHAR(50),
    wdate DATE,
    avg_temp FLOAT,
    min_temp FLOAT,
    max_temp FLOAT,
    PRIMARY KEY(region_code, wdate)
);

create table caseInfo(
	case_id INT,
    province VARCHAR(50),
    city VARCHAR(50),
    infection_group TINYINT(1),
    infection_case VARCHAR(50),
    confirmed INT,
    latitude FLOAT,
    longitude FLOAT,
    PRIMARY KEY(case_id)
);


create table timeInfo(
	date DATE,
    test int,
    negative int,
    confirmed int,
    released int,
    deceased int,
    PRIMARY KEY(date)
);