import pandas as pd

data=pd.read_csv('UCLA.csv')

data= data.dropna(subset=['Name'])

s=""
for i in range(len(data)):
    s+=data.iloc[i]['Name']+" is a doctor in "+data.iloc[i]['Hospital']+". "
    s+=data.iloc[i]['Name']+ " is specialised in department of "
    s+=data.iloc[i]['Departments']
    s+=". Link to doctor's profile is \""+data.iloc[i]['Profile']+"\". "

with open('training_data_UCLA.txt', 'w') as file:
    # Write the string to the file
    file.write(s)