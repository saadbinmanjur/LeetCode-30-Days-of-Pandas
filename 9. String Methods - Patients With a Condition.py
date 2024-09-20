import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    diab1_patient = patients[patients['conditions'].str.contains(r'\bDIAB1')]
    return diab1_patient