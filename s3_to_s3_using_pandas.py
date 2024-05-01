import boto3
import pandas as pd
import numpy as np

s3=boto3.client('s3')
obj = s3.get_object(Bucket='cloudlearn-poc-landing', Key='employee_data/employees.csv')
emp_inp = pd.read_csv(obj['Body'])


req_columns_emp = emp_inp.drop(columns=['Start_Date','Last_Login_Time','Senior_Management'])


name_filt = req_columns_emp['First_Name'].str.startswith('D')
sal_filt = req_columns_emp['Salary']>130000
filter_out_data = req_columns_emp[name_filt & sal_filt]


renamed_columns = filter_out_data.rename(columns={'First_Name':'first_name','Salary':'sal'})


renamed_columns['Team']=np.where(
    (renamed_columns['Team']=='Business Development') & (renamed_columns['sal']>=141000),'B - Develop',renamed_columns['Team']
)

emp_csv_out = renamed_columns.to_csv(index=False)
s3.put_object(Bucket='cloudlearn-poc-landing',Key='employee_data_out/emp_basic_trans_out_data.csv',Body=emp_csv_out)

print('succesfully completed the load')