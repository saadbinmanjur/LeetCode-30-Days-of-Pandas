import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee.drop_duplicates(subset=['salary'], inplace=True)
    if employee.shape[0] < 2 :
        return pd.DataFrame([[None]], columns=['SecondHighestSalary'])
    employee.sort_values(by='salary', inplace=True, ascending=False)
    employee = employee[['salary']]
    employee.rename(columns={'salary' : 'SecondHighestSalary'}, inplace=True)
    return employee.iloc[1:2]