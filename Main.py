import pandas as pd

df = pd.read_csv("la-county-restaurant-inspections.csv", error_bad_lines=False)

# Q1
print('Q1: The average score is ' + str(df['score'].mean()))

# Q2
res = df[df['facility_address'] == '17660 CHATSWORTH ST']
c = len(res.index)
print('Q2: Address 17660 CHATSWORTH ST was visited ' + str(c) + ' times')

# Q3
res = df[df['facility_city'] == 'LANCASTER']
c = len(res.index)
print('Q3: City Lanchaster was visited ' + str(c) + ' times')

# Q4
res = df[df['employee_id'] == 'EE0000145']
c = (len(res.index) / len(df.index)) * 100
print('Q4: The percentage of EE0000145 visit facility is ' + str(c) + ' %')

# Q5
res = df[df['facility_id'] == 'FA0013858']
c = (len(res.index) / len(df.index)) * 100
print('Q5: The percentage of FA0013858 visited is ' + str(c) + ' %')

# Q6
res = df[df['facility_city'] == 'GRANADA HILLS']
res = res[res['employee_id'] == 'EE0000593']
c = (len(res.index) / len(df.index)) * 100
print('Q6: The percentage of GRANADA HILLS visited by EE0000593 is ' + str(c) + ' %')