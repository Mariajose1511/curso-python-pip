import utils  # Importa el módulo utils que contiene funciones auxiliares
import read_csv  # Importa el módulo read_csv que contiene funciones para leer archivos CSV
import chart  # Importa el módulo chart que contiene funciones para graficar datos

def run():

    data = read_csv.read_csv('data.csv')  # Llama a la función read_csv para leer el archivo CSV y obtener los datos
    continente = utils.get_continente(data) # Llama a la función get_continente del módulo utils para obtener el continente a graficar    
    etiqueta,valor = utils.world_population_percentage(data,continente)  # Llama a la función world_population_percentage del módulo utils para obtener las etiquetas y valores de la población
    
    chart.pie_chart(continente,etiqueta,valor)  # Llama a la función pie_chart del módulo chart para graficar los datos

    # Solicita al usuario que ingrese el nombre de un país
    country = input('Type a country => ')

    # Llama a la función population_by_country del módulo utils para obtener la población del país ingresado
    result = utils.population_by_country(data, country) 
     

    if len(result) > 0 :  # Si se encontró el país en la lista
        country_dict = result[0]  # Obtiene el diccionario del país encontrado        
        labels, values = utils.get_population(country_dict)  # Llama a la función get_population para obtener las etiquetas y valores de la población
        chart.generate_bar_chart(country,labels,values)
   



if __name__ == '__main__':
    # Si el script se ejecuta directamente, llama a la función run y guarda el resultado
    run()
    
   
    