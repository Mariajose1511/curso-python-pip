import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A','B','C']
    values = [1,2,3]

    fig,ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    plt.savefig('pie.png')
    plt.close()

