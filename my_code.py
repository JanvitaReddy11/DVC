import pandas as pd
import os
data = {'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
    }

df = pd.DataFrame(data)

new_row = {'Name': 'Annie','Age':20,'City':'Mumbai'}
df.loc[len(df.index)] = new_row

new_row = {'Name': 'Alie','Age':25,'City':'Mumbai'}
df.loc[len(df.index)] = new_row

data_dir = 'data'
os.makedirs(data_dir,exist_ok = True)

file_path = os.path.join(data_dir,'sample_data.csv')
df.to_csv(file_path,index = False)
print('CSV file saved')
