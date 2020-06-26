# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here

# Step 1 
#Reading the file
loan_status=data['Loan_Status'].value_counts()
print(loan_status)
#Creating a new variable to store the value counts
loan_status.plot(kind='bar')



# Step 2
#Plotting an unstacked bar plot
property_and_loan=data.groupby(['Property_Area','Loan_Status'])
property_and_loan= property_and_loan.size().unstack()
property_and_loan.plot(kind='bar',stacked=False)
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)

print(property_and_loan['N'][1])
print(property_and_loan["Y"][0])

#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 3
#Plotting a stacked bar plot
education_and_loan=data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar',stacked=True)
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)




# Step 4 
#Subsetting the dataframe based on 'Education' column

graduate=data[data['Education']=="Graduate"]
graduate.plot(kind='density',label='Graduate')
not_graduate=data[data['Education']=='Not Graduate']
not_graduate.plot(kind='density',label='Not Graduate')
#Subsetting the dataframe based on 'Education' column


fig,(ax_1,ax_2,ax_3)=plt.subplots(nrows=3,ncols=1)
data.plot.scatter(x="ApplicantIncome",y='LoanAmount',ax=ax_1)
ax_1.set_title("Application Income")
data.plot.scatter(x='CoapplicantIncome',y='LoanAmount',ax=ax_2)
ax_2.set_title('Coapplicant Income')
#Creating a new column 'TotalIncome'
data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']
data.plot.scatter(x='TotalIncome',y='LoanAmount',ax=ax_3)
ax_3.set_title('Total Income')


