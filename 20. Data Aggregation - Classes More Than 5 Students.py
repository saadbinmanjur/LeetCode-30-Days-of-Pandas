import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    result = courses.groupby(["class"]).student.count().reset_index()
    return result.loc[result["student"] >= 5, ["class"]]