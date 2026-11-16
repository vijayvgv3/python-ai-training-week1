import pandas as pd

# step 1: create employees.csv and load it
csv_data = """id,name,department,salary,city
1,Arun,Sales,30000,Chennai
2,Priya,HR,45000,Chennai
3,Rahul,IT,60000,Bangalore
4,Divya,IT,75000,Chennai
5,karthik,Finance,90000,Mumbai
6,Meena,sales,52000,Bangalore
7,Suresh,IT,68000,Chennai
8,Anitha,HR,48000,Mumbai"""

with open("employees.csv", "w") as f:
    f.write(csv_data)

df = pd.read_csv("employees.csv")
print(df) 


print("---HEAD ---")
print(df.head())

print("\n--- INFO ---")
df.info()

print("n---DESCRIBE ---")
print(df.describe())


print(df['name'])
print(df[['name', 'salary']])


chennai_names = df.loc[df['city'] == 'Chennai', 'name']
print("chennai:", ",".join(chennai_names))

sliced_data = df.iloc[0:3, 1:3]
print("\nSliced Data:\n", sliced_data)


high_salary = df[df['salary'] > 50000]
print(f"Salary above 50000: {len(high_salary)} employees")

it_employees = df[df['department'] == 'IT']
print("IT department:", ", ".join(it_employees['name']))
print(f"IT department count: {len(it_employees)}")


import numpy as np
arr = np.arange(1, 25)
reshaped_arr = arr.reshape(2, 3, 4)

for i in range(reshaped_arr.shape[0]):
    print(f"slice {i} shape:", reshaped_arr[i].shape)
