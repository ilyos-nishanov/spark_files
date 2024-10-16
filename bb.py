#%%
import pandas as pd
# get emploee data
employee_data = [
    (1, "John"), (2, "Alice"), (3, "Bob"), (4, "Emily"),
    (5, "David"), (6, "Sarah"), (7, "Michael"), (8, "Lisa"),
    (9, "William")
]
employees=pd.DataFrame(employee_data, columns=["emp_id", "name"])
employees.head()
# %% get salary data
salary_data = [
    ("HR", 1, 60000), ("HR", 2, 55000), ("HR", 3, 58000),
    ("IT", 4, 70000), ("IT", 5, 72000), ("IT", 6, 68000),
    ("Sales", 7, 75000), ("Sales", 8, 78000), ("Sales", 9, 77000)
]
salary =pd.DataFrame(salary_data,columns=["dept","emp_id","salary"])
salary.head()
# %% merge
flat_df = pd.merge(employees,salary, how="inner", on="emp_id")
flat_df.head()
# %% map genders
genders = {'John': 'Male', 
           'Alice': 'Female', 
           'Emily': 'Female', 
           'Bob': 'Male', 
           'David': 'Male'}
flat_df['gender']=flat_df['name'].map(genders)
flat_df.head()
# %% map higher income with function
mean_salary = flat_df['salary'].mean()
def higher(income):
    return income >mean_salary

flat_df['higher']=flat_df['salary'].map(higher)
flat_df.head()
# %%
flat_df[flat_df[salary]>flat_df[salary].mean()]
# %% with lambda
flat_df['higher']=flat_df[salary].map(lambda(x:x>mean_salary))
