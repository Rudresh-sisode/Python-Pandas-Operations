import pandas as pd
data=pd.read_csv('HollywoodMovies.csv',index_col='Movie')
first=data['LeadStudio']
second=data['Genre']
print(first,"\n\n\n",second)
