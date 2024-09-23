import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    result_df = pd.merge(left=employees,right=employee_uni,how='left',on='id')[['unique_id','name']]
    return result_df