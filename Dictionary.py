import pandas as pd
from fuzzywuzzy import process


file1 = r"C:\Users\Usuario\Desktop\Data science\Proyecto Frente Amplio\Diccionario_Version_Nico.xlsx"
df1 = pd.read_excel(file1,sheet_name='Hoja1')
df2 = pd.read_excel(file1,sheet_name='Hoja2')



lista=[]
listaprima=[]

for palabra in df1['Diputado']:
    highest = process.extractOne(palabra,df2['Nombre Diputado'])
    lista.append(palabra)
    listaprima.append(highest)
    

    
dflista = pd.DataFrame(lista)
dfprima = pd.DataFrame(listaprima)
dfinal = pd.concat([dflista, dfprima], axis=1)
dfinal.columns = ['Diputado','Match Name','% Match','Aux']
#dfinal.sort_values(['% Match'],ascending=False,inplace=True)






dfinal.to_excel(r'C:\Users\Usuario\Desktop\Data science\Proyecto Frente Amplio\Diccionario_Final_Mapping.xlsx')