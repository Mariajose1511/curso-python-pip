

def population_by_country(data, country):
    """
    Filtra la lista de diccionarios 'data' para encontrar el diccionario que corresponde al país especificado.
    
    Args:
    data (list): Lista de diccionarios con datos de países y sus poblaciones.
    country (str): Nombre del país a buscar en la lista.
    
    Returns:
    list: Lista con el diccionario del país encontrado, o una lista vacía si no se encuentra el país.
    """
    # Filtra la lista para encontrar el país especificado
    result = list(filter(lambda item: item['Country/Territory'] == country, data))
    return result  # Devuelve el resultado del filtro

def get_population(country_dict):
    """
    Extrae los datos de población de un diccionario de país y los organiza en un nuevo diccionario.
    
    Args:
    country_dict (dict): Diccionario con datos de población de un país.
    
    Returns:
    tuple: Dos listas, una con las etiquetas (años) y otra con los valores (poblaciones).
    """
    # Crea un diccionario con los datos de población de diferentes años
    population_dict = {
        '2022': int(country_dict['2022 Population']),
        '2020': int(country_dict['2020 Population']),
        '2015': int(country_dict['2015 Population']),
        '2010': int(country_dict['2010 Population']),
        '2000': int(country_dict['2000 Population']),
        '1990': int(country_dict['1990 Population']),
        '1980': int(country_dict['1980 Population']),
        '1970': int(country_dict['1970 Population']),
    }

    labels = population_dict.keys()  # Obtiene las etiquetas (años) del diccionario
    values = population_dict.values()  # Obtiene los valores (poblaciones) del diccionario
    return labels, values  # Devuelve las etiquetas y los valores

def get_continente(data):
    continentes = map(lambda item: item['Continent'],data)
    continentes_unico = set(continentes)
    print(continentes_unico)
    contienente_seleccionado = input('Del listado anterior por favor copie y pegue el continente que desea graficar ==>')
    return contienente_seleccionado
    

def world_population_percentage(data,contienente_seleccionado):
    #continentes = map(lambda item: item['Continent'],data)
    #continentes_unico = set(continentes)
    #print(continentes_unico)
    #contienente_seleccionado = input('Del listado anterior por favor copie y pegue el continente que desea graficar ==>')
    
    continente = filter(lambda item:item['Continent'] == contienente_seleccionado,data)   
    result = {item['Country/Territory']:item['World Population Percentage'] for item in continente}
    labels = result.keys()
    values = result.values()   
   
    return labels, values


