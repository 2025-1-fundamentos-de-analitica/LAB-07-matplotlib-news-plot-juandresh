"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import os
import pandas as pd
import matplotlib.pyplot as plt

def pregunta_01():

    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

    os.makedirs('files/plots', exist_ok=True)

    plt.Figure()

    colors = {
        'Television': 'dimgray',
        'Newspaper': 'grey',
        'Internet': 'tab:blue',
        'Radio': 'lightgrey'
    }

    zorder = {        
        'Television': 1,
        'Newspaper': 1,
        'Internet': 2,
        'Radio': 1
    }

    linewidths = {        
        'Television': 2,
        'Newspaper': 2,
        'Internet': 3,
        'Radio': 2
    }

    data = pd.read_csv('files/input/news.csv', index_col=0)

    for col in data.columns:
        plt.plot(
            data[col],
            color = colors[col],
            label=col,
            zorder = zorder[col],
            linewidth = linewidths[col]
        )

    plt.title('How people get their news', fontsize=16)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)
    
    for col in data.columns:
        first_year = data.index[0]
        plt.scatter(
            x = first_year,
            y = data[col][first_year],
            color = colors[col],
            zorder = zorder[col]
        )

        plt.text(
            first_year - 0.2,
            data[col][first_year],
            col + " " + str(data[col][first_year]) + "%",
            ha = 'right',
            va = 'center',
            color = colors[col]
        )

        last_year = data.index[-1]
        plt.scatter(
            x = last_year,
            y = data[col][last_year],
            color = colors[col],
        )

        plt.text(
            last_year + 0.2,
            data[col][last_year],
            str(data[col][last_year]) + "%",
            ha = 'left',
            va = 'center',
            color = colors[col]
        )

    plt.xticks(
        ticks = data.index,
        labels = data.index,
        ha = 'center'
    )
    
    plt.tight_layout()
    plt.savefig('files/plots/news.png')