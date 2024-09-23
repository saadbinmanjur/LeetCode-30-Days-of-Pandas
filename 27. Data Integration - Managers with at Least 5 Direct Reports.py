import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    report_df = employee.groupby('managerId', as_index=False).agg(reporter_count=('managerId','count'))
    return employee[employee.id.isin(report_df[report_df.reporter_count >=5]['managerId'])][['name']]