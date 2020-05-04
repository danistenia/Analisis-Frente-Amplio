from FuncionIteraFrenteAmplio import iterasesiones
import pandas as pd

datafinal=[]

for i in range(0,107):


    print(i)
    a=iterasesiones(i)
    datafinal.append(a)
 
    
    #print(df_final)
    #pd.datadatafinal.append(a)
    
df_final=pd.DataFrame(datafinal[0])
#print(datafinal[1])
#=['Nombre Diputado','Voto','Sesion']
#b=1
for b in datafinal[1:]:

    df_final=df_final.append(b)
    #print(b)

df_final.to_excel(r'C:\Users\Usuario\Desktop\Data science\Proyecto Frente Amplio\Final.xlsx')
#print(datafinal)
