import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    teacher = teacher.drop_duplicates(subset=['teacher_id', 'subject_id'])
    teacher = (teacher
    .pivot_table(index='teacher_id', values='subject_id', aggfunc='count')
    .reset_index())
    teacher.columns = ['teacher_id', 'cnt']
    return teacher