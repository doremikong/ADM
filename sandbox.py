from db import Databases
from datetime import date, timedelta,datetime
from utils import analyze, cal_nutrient

# start = datetime.strptime('20220520',"%Y%m%d").date()
# end= datetime.strptime('20220520',"%Y%m%d").date()

# analyze("Ronald", start, end)
d = Databases('u20180475')
food_infos = d.readDB("fdc_id, description", "food", "")
p_amr = d.readDB("amr","personal_amr","where id='{}'".format("bis000"))
print(p_amr)

CREATE TABLE personal_info(id varchar(10) primary key, age integer, gender char(1), height float, weight float, exercise_level integer, disease varchar(50));
CREATE TABLE personal_amr(id varchar(10) primary key, amr float, foreign key (id) references personal_info(id));
CREATE TABLE food(fdc_id integer primary key, description varchar(300));
CREATE TABLE diet_info(id varchar(10), date date, fdc_id integer, amount float, primary key (id,date,fdc_id), foreign key (id) references personal_info(id), foreign key (fdc_id) references food(fdc_id));
CREATE TABLE nutrient(id integer primary key, name varchar(30), unit_name varchar(10));
CREATE TABLE food_nutrient(fdc_id integer, nutrient_id integer, amount float, primary key (fdc_id,nutrient_id), foreign key (fdc_id) references food(fdc_id), foreign key (nutrient_id) references nutrient(id));
CREATE TABLE recommended_nutrient(age char(10), gender char(1), nutrient_id integer, low float, high float, primary key (age,gender,nutrient_id), foreign key (nutrient_id) references nutrient(id));
CREATE TABLE nutrient_disease(id integer, status varchar(10), disease_name varchar(50), primary key (id,status,disease_name), foreign key (id) references nutrient(id));
CREATE TABLE nutrient_info(id varchar(10), date date, nutrient_id integer, amount float, primary key (id,date,nutrient_id))
