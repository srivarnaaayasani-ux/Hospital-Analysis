import pandas as pd

#step 1 Reading files
df_patients = pd.read_csv('patients.csv')
df_doctors = pd.read_csv('doctors.csv')
df_appointments = pd.read_csv('appointments.csv')

#step 2 hospital analysis
print("\n======Hospital Analysis======\n")
print("Total Number of patients : ",df_patients.shape[0])
print("Total No of Male Patients : ", (df_patients["Gender"]== "Male").sum())
print("Total No of Female Patients : ", (df_patients["Gender"]== "Female").sum())
print("Average Age of patients : ",(df_patients["Age"]).mean())

print("\n======Oldest Patient======\n")
oldest_age = (df_patients["Age"]).max()
print(df_patients[df_patients["Age"] == oldest_age])

print("\n======Youngest Patient======\n")
youngest_patient = (df_patients["Age"]).min() 
print(df_patients[df_patients["Age"] == youngest_patient])

common_disease = (df_patients["Disease"].value_counts())
print(common_disease)

max_freq = (common_disease.max())
most_common_disease = common_disease[common_disease == max_freq]
print(most_common_disease)

min_freq = (common_disease.min())
lease_common_disease = common_disease[common_disease == min_freq]
print(lease_common_disease)

#step 3 doctor analysis
print("\n======Doctor Analysis======\n")
print("Total Number of Doctors : ",df_doctors.shape[0])

print("\n======Department wise Doctors======\n")
dept_freq = (df_doctors["Department"].value_counts())
print("No of Doctors in each Department : ", dept_freq)

print("\n======Most doctors Department======\n")
max_dept = (df_doctors["Department"].value_counts()).max()
most_doc = dept_freq[dept_freq == max_dept]
print("Department with most Doctors : ",most_doc)

print("\n======Least Doctors Department======\n")
min_dept = (df_doctors["Department"].value_counts()).min()
fewest_doc = dept_freq[dept_freq == min_dept]
print("Department with most Doctors : ",fewest_doc)

#Appointment analysis
print("\n======Appointment Analysis======\n")
print("Total no of Appointments : ",df_appointments.shape[0])
print("Total revenue : ",df_appointments["Fees"].sum())
print("Average Consultation fees : ",df_appointments["Fees"].mean())
print("Highest consultation fees : ", df_appointments["Fees"].max())
print("Lowest consultation fees : ", df_appointments["Fees"].min())

doctor_freq = df_appointments["DoctorID"].value_counts()
print("Appointment frequency by Doctor",doctor_freq)
busy_doc = doctor_freq.max()
print("Busiest Doctor : ",doctor_freq[doctor_freq==busy_doc])

least_busy_doc = doctor_freq.min()
print("Busiest Doctor : ",doctor_freq[doctor_freq==least_busy_doc])

app_freq = df_appointments["Date"].value_counts()
print("Appointment Frequency by Date : ",app_freq)

high_app = app_freq.max()
print("Busiest Day ",(app_freq[app_freq == high_app]))

#Merge patients and appointments 
merge_df = pd.merge(df_patients,df_appointments,on = "PatientID")
print(merge_df.head())
print("\n ====== Merge ======\n")
merge_3csv = pd.merge(merge_df,df_doctors,on = "DoctorID")
print(merge_3csv)

# Business Insights
most_patients = (merge_3csv["DoctorName"]).value_counts()
max_patient = most_patients.max()
print("Doctor treated most patients :\n",most_patients[most_patients==max_patient])
less_patient = most_patients.min()
print("Doctor treated less patients :\n",most_patients[most_patients==less_patient])

most_dept_freq = (merge_3csv["Department"]).value_counts()
most_treated_dept = most_dept_freq.max()
print("Department treated most patients :\n",most_dept_freq[most_dept_freq==most_treated_dept])
least_treated_dept = most_dept_freq.min()
print("Department treated less patients :\n",most_dept_freq[most_dept_freq==least_treated_dept])

highest_revenue_freq = merge_3csv.groupby("DoctorName")["Fees"].sum()
highest_revenue_doc = highest_revenue_freq.max()
print("Doctor with highest Revenue :\n",(highest_revenue_freq[highest_revenue_freq == highest_revenue_doc]))

highest_revenue_Dept_f = merge_3csv.groupby("Department")["Fees"].sum()
highest_revenue_dept = highest_revenue_Dept_f.max()
print("Highest revenue Department :\n",highest_revenue_Dept_f[highest_revenue_Dept_f==highest_revenue_dept])
print("Average consultation fee : ",merge_3csv.groupby("Department")["Fees"].mean())

department = merge_3csv.groupby("Department")["Disease"].value_counts()

print("Most common diseases in each department :\n",department)

