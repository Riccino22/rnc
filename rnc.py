import pandas as pd
import requests
import zipfile
import io

"""# URL del archivo ZIP remoto
url = "https://www.dgii.gov.do/app/WebApps/Consultas/RNC/DGII_RNC.zip"

# Descargar el archivo ZIP en memoria (sin guardar en disco)
response = requests.get(url, verify=False)

# Abre el archivo ZIP en memoria
with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
    # Listar los archivos dentro del ZIP
    print(zip_file.namelist())  # Verifica los archivos dentro del ZIP
    
    # Abrir el archivo TXT dentro del ZIP
    with zip_file.open('TMP/DGII_RNC.TXT') as txt_file:
        # Leer el archivo TXT (ajusta el delimitador según el formato)
        df = pd.read_csv(txt_file, delimiter='|', encoding='latin1', header=None)  # Ejemplo para un archivo TSV (delimitado por tabulaciones
        
# Mostrar las primeras filas del DataFrame
print(df.head())
print(df[df[2].str.contains('DIGITAL GROUP', case=False, na=False)].iloc[0,0])"""

def get():
    # URL del archivo ZIP remoto
    url = "https://www.dgii.gov.do/app/WebApps/Consultas/RNC/DGII_RNC.zip"

    # Descargar el archivo ZIP en memoria (sin guardar en disco)
    response = requests.get(url, verify=False)

    # Abre el archivo ZIP en memoria
    with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
        # Listar los archivos dentro del ZIP
        print(zip_file.namelist())  # Verifica los archivos dentro del ZIP
        
        # Abrir el archivo TXT dentro del ZIP
        with zip_file.open('TMP/DGII_RNC.TXT') as txt_file:
            # Leer el archivo TXT (ajusta el delimitador según el formato)
            column_names = ['rnc', 'reference_name', 'name', 'category', '4', '5', '6', '7', '8', '9', '10']
            df = pd.read_csv(txt_file, delimiter='|', encoding='latin1', header=None, names=column_names)  # Ejemplo para un archivo TSV (delimitado por tabulaciones
            
    # Mostrar las primeras filas del DataFrame
    print(df.head())
    print(df[df['name'].str.contains('DIGITAL GROUP', case=False, na=False)].iloc[0,0])
    
    return df

def search(df, name):
    #return df[df[2].str.contains(name, case=False, na=False)].iloc[1,2]
    return df[df['name'].str.contains(name, case=False, na=False)][:10]