import pandas as pd
import xlrd



df = pd.read_excel(r'C:\Users\Usuario\Desktop\Data science\Proyecto Frente Amplio\Dictionary.excel.xlsx')
df_last = pd.read_excel(r'C:\Users\Usuario\Desktop\Data science\Proyecto Frente Amplio\Final.xlsx')
dic = {}
libro = xlrd.open_workbook(r'C:\Users\Usuario\Desktop\Data science\Proyecto Frente Amplio\Dictionary.excel.xlsx')
hoja = libro.sheet_by_name('Hoja1')
for i in range(1,hoja.nrows):

    fila = hoja.row_values(i)
    dic[fila[0]]=fila[1]
df_last['Aux']=df_last['Nombre Diputado']
df_last['Aux'].replace(dic,inplace=True)




#df_last['Tendencia']=df_last['Nombre Diputado'].map(dic)

df_last.to_excel(r'C:\Users\Usuario\Desktop\Data science\Proyecto Frente Amplio\BaseFinalAnalisis.xlsx')


#print(df)