# %%
import matplotlib.pylab as plt
import numpy as np

# %% 

def generate_bar_chart(name,labels,values):
    
    fig, ax = plt.subplots()  # Crea una figura y un eje
    ax.bar(labels, values)  # Crea un gráfico de barras con las etiquetas y los valores dados
    plt.savefig(f'./imgs/{name}.png')  # Guarda el gráfico en un archivo
    plt.close()  # Cierra el gráfico
    


def pie_chart(name,labels,values):
    fig, ax = plt.subplots()  # Crea una figura y un eje
    ax.pie(values,labels = labels)  # Crea un gráfico de pastel con las etiquetas y los valores dados
    ax.axis('equal')  # Hace que el gráfico sea un círculo
    plt.savefig(f'./imgs/{name}.png')  # Guarda el gráfico en un archivo
    plt.close()  # Cierra el gráfico

if __name__ == '__main__':
    labels = ['A', 'G', 'C', 'H', 'E']  # Etiquetas para cada barra
    values = [20, 10, 15, 40, 25]  # Alturas de las barras
    #generate_bar_chart(labels,values)  # Llama a la función generate_bar_chart
    pie_chart(labels,values)  # Llama a la función pie_chart
