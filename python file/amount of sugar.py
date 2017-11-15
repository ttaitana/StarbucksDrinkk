import pandas as pd
import pygal as pg
from pygal.style import Style
custom_style = Style(
  background='transparent',
  colors=('#00723F', '#0B421A', '#00723F', '#EAC784', '#e5a632', '#604C4C', '#BBBBBB', '#AAAAAA'))

"""
███╗   ███╗ █████╗ ██╗███╗   ██╗    ███████╗██╗   ██╗███╗   ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗
████╗ ████║██╔══██╗██║████╗  ██║    ██╔════╝██║   ██║████╗  ██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║
██╔████╔██║███████║██║██╔██╗ ██║    █████╗  ██║   ██║██╔██╗ ██║██║        ██║   ██║██║   ██║██╔██╗ ██║
██║╚██╔╝██║██╔══██║██║██║╚██╗██║    ██╔══╝  ██║   ██║██║╚██╗██║██║        ██║   ██║██║   ██║██║╚██╗██║
██║ ╚═╝ ██║██║  ██║██║██║ ╚████║    ██║     ╚██████╔╝██║ ╚████║╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝    ╚═╝      ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
"""
def main():
    data = pd.read_csv('../data/starbucks_drinkMenu_expanded.csv')
    dot_data = dot_filter(data)
    dot_graph(dot_data)
    #print(pd.DataFrame.keys(data))
    #chart.render_to_file('D:/chart.svg')

"""
==================================================================================================================================================================

███████╗██╗██╗  ████████╗███████╗██████╗     ███████╗██╗   ██╗███╗   ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗
██╔════╝██║██║  ╚══██╔══╝██╔════╝██╔══██╗    ██╔════╝██║   ██║████╗  ██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║
█████╗  ██║██║     ██║   █████╗  ██████╔╝    █████╗  ██║   ██║██╔██╗ ██║██║        ██║   ██║██║   ██║██╔██╗ ██║
██╔══╝  ██║██║     ██║   ██╔══╝  ██╔══██╗    ██╔══╝  ██║   ██║██║╚██╗██║██║        ██║   ██║██║   ██║██║╚██╗██║
██║     ██║███████╗██║   ███████╗██║  ██║    ██║     ╚██████╔╝██║ ╚████║╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║
╚═╝     ╚═╝╚══════╝╚═╝   ╚══════╝╚═╝  ╚═╝    ╚═╝      ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
"""
def dot_filter(data):
    filtered_data = dict()
    for i in range(238):
        if data['Beverage_category'][i] not in filtered_data:
            filtered_data[data['Beverage_category'][i]] = [data[' Sugars (g)'][i]]
        else:
            filtered_data[data['Beverage_category'][i]].append(data[' Sugars (g)'][i])

    return filtered_data


"""
=========================================================================================================================================================

 ██████╗ ██████╗  █████╗ ██████╗ ██╗  ██╗    ███╗   ███╗ █████╗ ██╗  ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██║  ██║    ████╗ ████║██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
██║  ███╗██████╔╝███████║██████╔╝███████║    ██╔████╔██║███████║█████╔╝ █████╗  ██████╔╝
██║   ██║██╔══██╗██╔══██║██╔═══╝ ██╔══██║    ██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║  ██║██║     ██║  ██║    ██║ ╚═╝ ██║██║  ██║██║  ██╗███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
"""
def dot_graph(data):
    chart = pg.Bar(style=custom_style,legend_at_bottom=True)#(show_legend=False, style=DefaultStyle)
    chart.title = 'Amount of suger in Starbucks Beverage'
    key = [i for i in data]
    chart.add(key[1], [{
        'value' : round((sum(data[key[1]])/len(data[key[1]])), 2),
        'label' : key[1],
        'xlink': '../html_graph/Classic_Espresso_drinks.html'
        }])
    chart.add(key[2], [{
        'value' : round((sum(data[key[2]])/len(data[key[2]])), 2),
        'label' : key[2],
        'xlink': '#'
        }])
    chart.add(key[3], [{
        'value' : round((sum(data[key[3]])/len(data[key[3]])), 2),
        'label' : key[3],
        'xlink': '#'
        }])
    chart.add(key[4], [{
        'value' : round((sum(data[key[4]])/len(data[key[4]])), 2),
        'label' : key[4],
        'xlink': '#'
        }])
    chart.add(key[5], [{
        'value' : round((sum(data[key[5]])/len(data[key[5]])), 2),
        'label' : key[5],
        'xlink': '#'
        }])
    chart.add(key[6], [{
        'value' : round((sum(data[key[6]])/len(data[key[6]])), 2),
        'label' : key[6],
        'xlink': '#'
        }])
    chart.add(key[7], [{
        'value' : round((sum(data[key[7]])/len(data[key[7]])), 2),
        'label' : key[7],
        'xlink': '#'
        }])
    chart.add(key[8], [{
        'value' : round((sum(data[key[8]])/len(data[key[8]])), 2),
        'label' : key[8],
        'xlink': '#'
        }])
    chart.render_to_file('D:/test.svg')



main()