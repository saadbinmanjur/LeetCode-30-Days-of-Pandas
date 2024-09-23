import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    exam_count = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')
    stu_subs = pd.merge(students, subjects, how='cross')
    
    result_df = pd.merge(stu_subs, exam_count, how='left', on=['student_id', 'subject_name'])
    result_df = result_df[['student_id', 'student_name', 'subject_name', 'attended_exams']].sort_values(by=['student_id', 'subject_name'])
    result_df.attended_exams = result_df.attended_exams.fillna(0)

    return result_df