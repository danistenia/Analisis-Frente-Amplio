import pandas as pd
import requests
import urllib.request
from bs4 import BeautifulSoup

datafinal=[]

def iterasesiones(x):
    



    df_url = pd.read_excel(r'C:\Users\Usuario\Desktop\Data science\Proyecto Frente Amplio\DataUrl.xlsx')
    #datafinal=[]
    diputados_1=[]
    diputados_2 = []
    diputados_final_a_favor=[]
    diputados_final_en_contra=[]
    


    url = df_url.loc[x].at['Resultado']
    r = requests.get(url)
    html_content = r.text
    soup = BeautifulSoup(html_content,"lxml")
    table = soup.find('table',id='ContentPlaceHolder1_ContentPlaceHolder1_PaginaContent_dtlAFavor')
    titulo = df_url.loc[x].at['Sesion']
    #subti = titulo.div.info.text.strip()
    filas = table.find_all('tr')
    #colum = table.find_all('td')
    for fila in filas:
        colum = fila.find_all('td')
        fil = [fila.text.strip() for fila in colum if fila.text.strip()]
        #print()
        #diputados.append(col_0.replace('\r',''))
        if fil:
            diputados_1.append(fil)
        
    for i in diputados_1:
        for a in i:
            diputados_final_a_favor.append(a)

    #print(diputados_final_a_favor)

    ##################################################################

    try:
        table_1 = soup.find('table',id='ContentPlaceHolder1_ContentPlaceHolder1_PaginaContent_dtlEnContra')
        filas_1 = table_1.find_all('tr')
        
            
        #colum = table.find_all('td')
        for fila_1 in filas_1:
            colum_1 = fila_1.find_all('td')
            fil_1 = [fila_1.text.strip() for fila_1 in colum_1 if fila_1.text.strip()]
            #print()
            #diputados.append(col_0.replace('\r',''))
            if fil_1:
                diputados_2.append(fil)
    except:
        pass            

            
        
    for h in diputados_2:
        for b in h:
            diputados_final_en_contra.append(b)
        
    #print(diputados_final_en_contra)
    #print(len(diputados_final_a_favor)+len(diputados_final_en_contra))
    df_1 = pd.DataFrame(diputados_final_a_favor,columns=["Nombre Diputado"])
    df_1['Voto'] = 1
    df_2 = pd.DataFrame(diputados_final_en_contra,columns=["Nombre Diputado"])
    df_2['Voto'] = 0
    frames = [df_1,df_2]
    eljunte = pd.concat(frames)
    eljunte['Sesion'] = titulo
    #print(eljunte)
    return eljunte

