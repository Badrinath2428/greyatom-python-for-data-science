# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=np.array([[50,  9,  4,  1,  0,  0, 40,  0]])

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
census=np.concatenate((data,new_record),axis=0)
print(census.shape)
#Code starts here
age=census[:1001,:1]
max_age=age.max()
min_age=age.min()
age_mean=age.mean()
age_std=np.std(age)
print(max_age,min_age,age_mean,age_std)


race=census[:1001,2:3]
print(race.shape)
race_0=race[race==0]
race_1=race[race==1]
race_2=race[race==2]
race_3=race[race==3]
race_4=race[race==4]
len_0=race_0.size
len_1=race_1.size
len_2=race_2.size
len_3=race_3.size
len_4=race_4.size
print(len_0,len_1,len_2,len_3,len_4)
len_race=[len(race_0),len(race_1),len(race_2),len(race_3),len(race_4)]
minority_race=len_race.index(min(len_race))
print(minority_race)


senior_citizen=census[:1001,0:7:6]
print(senior_citizen.shape)
senior_citizens=(senior_citizen[(senior_citizen[:1001,0])>60])
print(senior_citizens.shape)
working_hours=(senior_citizens[:1001,1:2])
working_hours_sum=working_hours.sum()
print(working_hours_sum)
senior_citizens_len=len(senior_citizens)
avg_working_hours=round(working_hours_sum/senior_citizens_len,2)
print(avg_working_hours)


pay=census[:1001,1:8:6]
pay_high=pay[pay[:1001,0]>10]
pay_low=pay[pay[:1001,0]<=10]
avg_pay_high=round((pay_high[:1001,1]).mean(),2)
avg_pay_low=round((pay_low[:1001,1]).mean(),2)
print(avg_pay_high,avg_pay_low)


