# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
census=np.concatenate((new_record,data))
age=np.array(census[:,0])
max_age=age.max()
min_age=age.min()
age_mean=round(age.mean(),2)
age_std=round(age.std(),2)

#Code starts here

def race(n):
    l=[]
    for i in range(len(census[:,2])+1):
        for j in census[:,2]:
            if j==n:
                l.append(i)
    return l
race_0=np.array(race(0))
race_1=np.array(race(1))
race_2=np.array(race(2))
race_3=np.array(race(3))
race_4=np.array(race(4))
race_5=np.array(race(5))
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)
len_5=len(race_5)
lens=np.array([len_0,len_1,len_2,len_3,len_4])
for i in range(len(lens)):
    if lens[i]==lens.min():
        minority_race=i

#step4

senior_citizens=np.array(census[:,0][census[:,0]>60])


def work_hour():
    w=[]
    for i in range(len(census[:,0])):
        if census[:,0][i]>60:
            w.append(census[:,6][i])
    return w
working_hours_sum=sum(work_hour())
senior_citizens_len=len(senior_citizens)
avg_working_hours=round(working_hours_sum/senior_citizens_len,2)
print(avg_working_hours)

#step5
high=np.array(census[:,1][census[:,1]>10])
low=np.array(census[:,1][census[:,1]<=10])
def income(n):
    k=[]
    l=[]
    for i in range(len(census[:,1])):
        if census[:,1][i]>10:
            k.append(census[:,7][i])
        elif census[:,1][i]<=10:
            l.append(census[:,7][i])

    if n==0:
        return l
    elif n==1:
        return k
avg_pay_high=np.array(income(1))
avg_pay_high=round(avg_pay_high.mean(),2)

avg_pay_low=np.array(income(0))
avg_pay_low=round(avg_pay_low.mean(),2)
print(avg_pay_high>avg_pay_low)













