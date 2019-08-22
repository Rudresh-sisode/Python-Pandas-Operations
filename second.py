import pandas
frame=pandas.read_csv('HollywoodMovies.csv',index_col='LeadStudio')
first=frame.loc['Movie']
second=frame.loc['Genre']
print(first,'\n',second)
