#%%
import pandas as pd
# get emploee data
employee_data = [
    (1, "John"), (2, "Alice"), (3, "Bob"), (4, "Emily"),
    (5, "David"), (6, "Sarah"), (7, "Michael"), (8, "Lisa"),
    (9, "William")
]
employees=pd.DataFrame(employee_data, columns=["emp_id", "name"])
employees
# %% get salary data
salary_data = [
    ("HR", 1, 60000), ("HR", 2, 55000), ("HR", 3, 58000),
    ("IT", 4, 70000), ("IT", 5, 72000), ("IT", 6, 68000),
    ("Sales", 7, 75000), ("Sales", 8, 78000), ("Sales", 9, 77000)
]
salary =pd.DataFrame(salary_data,columns=["dept","emp_id","salary"])
salary
# %% merge
flat_df = pd.merge(employees,salary, how="inner", on="emp_id")
flat_df
# %% map genders
genders = {'John': 'Male', 
           'Alice': 'Female', 
           'Emily': 'Female', 
           'Bob': 'Male', 
           'David': 'Male'}
flat_df['gender']=flat_df['name'].map(genders)
flat_df.head()
# %% map higher income with function
mean_salary = flat_df.groupby('dept').mean('salary')
mean_salary.rename(columns={'salary':'avg_salary'}, inplace=True)
mean_salary
def is_above_average(row):
    dept = row['dept']
    salary = row['salary']
    return salary > mean_salary[dept]

flat_df['higher'] = flat_df.apply(is_above_average, axis=1)
flat_df
# %% with lambda
flat_df['higher']=flat_df['salary'].map(lambda x:x>mean_salary)
flat_df.head()
# %%
flat_df[flat_df['salary']>0]
# %%
import pandas as pd

# Employee data
employee_data = [
    (1, "John"), (2, "Alice"), (3, "Bob"), (4, "Emily"),
    (5, "David"), (6, "Sarah"), (7, "Michael"), (8, "Lisa"),
    (9, "William")
]
employees = pd.DataFrame(employee_data, columns=["emp_id", "name"])

# Salary data
salary_data = [
    ("HR", 1, 60000), ("HR", 2, 55000), ("HR", 3, 58000),
    ("IT", 4, 70000), ("IT", 5, 72000), ("IT", 6, 68000),
    ("Sales", 7, 75000), ("Sales", 8, 78000), ("Sales", 9, 77000)
]
salary = pd.DataFrame(salary_data, columns=["dept", "emp_id", "salary"])

# Merge employee and salary data
flat_df = pd.merge(employees, salary, how="inner", on="emp_id")

# Map genders (partial data provided)
genders = {'John': 'Male',
           'Alice': 'Female',
           'Emily': 'Female',
           'Bob': 'Male',
           'David': 'Male',
           'Sarah':'Female',
           'Michael':'Male',
           'Lisa':'Female',
           'William':'Male'}
flat_df['gender'] = flat_df['name'].map(genders)


# Calculate average salary per department
mean_salary = flat_df.groupby('dept')['salary'].mean()

# Function to check if salary is above department average
def is_above_average(row):
    """Checks if an employee's salary is above the department average."""
    dept = row['dept']
    salary = row['salary']
    return salary > mean_salary["dept"]

# Apply the function to create the 'higher' column
flat_df['higher'] = flat_df.apply(is_above_average, axis=1)

print(flat_df)
# %%
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
arr
# %%
