import json
import pandas as pd

def convertir_json_a_excel():
    archivo_json = 'datos_usuarios.json'
    archivo_excel = 'datos_usuarios.xlsx'

    # Leer los datos del archivo JSON
    with open(archivo_json, 'r') as file:
        datos = json.load(file)

    # Convertir los datos a un DataFrame de pandas
    df = pd.DataFrame(datos)

    # Guardar los datos en un archivo Excel
    df.to_excel(archivo_excel, index=False)

if __name__ == '__main__':
    convertir_json_a_excel()
    print("Datos convertidos y guardados en 'datos_usuarios.xlsx'")