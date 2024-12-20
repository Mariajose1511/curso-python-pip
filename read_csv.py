import csv  # Importa el módulo csv para trabajar con archivos CSV

def read_csv(path):
    """
    Lee un archivo CSV y convierte cada fila en un diccionario.
    
    Args:
    path (str): La ruta del archivo CSV a leer.
    """
    with open(path, 'r') as csvfile:  # Abre el archivo CSV en modo lectura ('r')
        reader = csv.reader(csvfile, delimiter=',')  # Crea un objeto reader para leer el archivo CSV, usando ',' como delimitador
        header = next(reader)  # Lee la primera fila del archivo CSV, que contiene los encabezados de las columnas
        data = []  # Inicializa una lista vacía para almacenar los diccionarios
        
        for row in reader:  # Itera sobre cada fila restante en el archivo CSV
            iterable = zip(header, row)  # Combina los encabezados y la fila actual en pares clave-valor
            country_dic = {key: value for key, value in iterable}  # Crea un diccionario a partir de los pares clave-valor
            data.append(country_dic)  # Añade el diccionario a la lista data
        
    return data  # Devuelve la lista de diccionarios
if __name__ == '__main__':
    data = read_csv('./app/data.csv')  # Llama a la función read_csv con la ruta del archivo CSV
    print(data[0])  # Imprime el primer diccionario de la lista data