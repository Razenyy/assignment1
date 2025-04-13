'''Given the table below

EmployeeID	Name	Department	Age	Salary	JoinDate	ExperienceYears
101	John Smith	IT	30	70000	2018-07-15	5
102	Alice Brown	HR	28	60000	2020-03-10	3
103	Bob White	IT	35	80000	2016-11-01	7
104	Emma Green	Finance	40	90000	2012-05-25	11
105	Charlie Red	HR	25	55000	2021-06-01	2

a.	Write a query to select only the Name and Salary columns.
b.	How would you filter out all employees in the "IT" department?
c.	Write code to select employees who are older than 30 and find the average salary of employees in each department.
d.	Write code to count the number of employees in each department.
e.	Add a new column Bonus which is 10% of each employee's salary.
f.	Replace all occurrences of "HR" in the Department column with "Human Resources."
g.	 Find the employee(s) with the longest tenure (based on JoinDate).
h.	Create a new column SalaryCategory where salaries above 75,000 are categorized as "High" and the rest as "Low."
i.	Write a program to check if there are any duplicate EmployeeIDs and remove them if found.
j.	Use Pandas to calculate the median Age of all employees'''

import pandas as pd


data = {
    'EmployeeID': [101, 102, 103, 104, 105],
    'Name': ['John Smith', 'Alice Brown', 'Bob White', 'Emma Green', 'Charlie Red'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR'],
    'Age': [30, 28, 35, 40, 25],
    'Salary': [70000, 60000, 80000, 90000, 55000],
    'JoinDate': ['2018-07-15', '2020-03-10', '2016-11-01', '2012-05-25', '2021-06-01'],
    'ExperienceYears': [5, 3, 7, 11, 2]
}

df = pd.DataFrame(data)
df['JoinDate'] = pd.to_datetime(df['JoinDate']) 

name_salary_df = df[['Name', 'Salary']]
print(name_salary_df)

it_department_excluded = df[df['Department'] != 'IT']
print(it_department_excluded)


older_than_30 = df[df['Age'] > 30]


average_salary_by_department = df.groupby('Department')['Salary'].mean()
print(older_than_30)
print(average_salary_by_department)

employee_count_by_department = df['Department'].value_counts()
print(employee_count_by_department)

df['Bonus'] = df['Salary'] * 0.10
print(df[['Name', 'Salary', 'Bonus']])

df['Department'] = df['Department'].replace('HR', 'Human Resources')
print(df[['Name', 'Department']])


df['TenureYears'] = (pd.to_datetime('today') - df['JoinDate']).dt.days / 365


longest_tenure = df[df['TenureYears'] == df['TenureYears'].max()]
print(longest_tenure[['Name', 'TenureYears']])

df['SalaryCategory'] = df['Salary'].apply(lambda x: 'High' if x > 75000 else 'Low')
print(df[['Name', 'Salary', 'SalaryCategory']])


df_no_duplicates = df.drop_duplicates(subset='EmployeeID')
print(df_no_duplicates)

median_age = df['Age'].median()
print(f"Median Age of Employees: {median_age}")



