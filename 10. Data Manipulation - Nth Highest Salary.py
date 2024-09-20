import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee['salary'].drop_duplicates()
    df = df.sort_values(ascending=False)
    column = 'getNthHighestSalary('+str(N)+')'
    if N > len(df) or N<=0:
        return pd.DataFrame({column:[None]})
    return pd.DataFrame({column:[df.iloc[N-1]]})