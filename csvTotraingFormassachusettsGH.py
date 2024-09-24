import pandas as pd

data=pd.read_csv('MassachusettsGeneralHospital.csv')

data= data.dropna(subset=['Name'])
s=""
for i in range(len(data)):
    s+=data.iloc[i]['Name']+" is a doctor in "+data.iloc[i]['Hospital']+". "
    if(data.iloc[i]['Speciality']!="[]"):
        s+=data.iloc[i]['Name']+ " is specialised in "
        s+=data.iloc[i]['Speciality']+" and treats "+data.iloc[i]['Treats']+"."
    s+=" Link to doctor's profile is \""+data.iloc[i]['Profile']+"\". "

with open('training_data.txt', 'w') as file:
    # Write the string to the file
    file.write(s)