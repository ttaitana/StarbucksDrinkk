import pandas as pd
import pygal as pg
from pygal.style import Style
custom_style = Style(
  background='transparent',
  colors=('#1E6B7F', '#0B421A', '#00723F', '#EAC784', '#e5a632', '#604C4C', '#BBBBBB', '#AAAAAA'))

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
    link = [
    #Hot Beverages
    '../html_graph/Classic_Espresso_drinks.html', #Classic_Espresso
    '../html_graph/Signature Espresso Drinks.html', #Signature Espresso Drinks.html
    '../html_graph/Tazo® Tea Drinks.html',    #Tazo® Tea Drinks
    #Cold Beverages
    '../html_graph/Shaken Iced.html',#Shaken Iced Beverages
    '../html_graph/Smoothies.html', #Smoothies
    '../html_graph/Frappuccino® Blended Coffee.html', #Frappuccino® Blended Coffee
    '../html_graph/Frappuccino® Light Blended Coffee.html', #Frappuccino® Light Blended Coffee
    '../html_graph/Frappuccino® Blended Crème.html'] #Frappuccino® Blended Crème
    chart.add('Sugar average', [
        {
        'value' : round(sum([sum(data[i])/len(data[i]) for i in data]) / len(data), 2),
        'lable' : 'Sugar average'
        }
    ])
    for i in range(1, len(data)):
        chart.add(key[i], [{
        'value' : round((sum(data[key[i]])/len(data[key[i]])), 2),
        'label' : key[i],
        'xlink': link[i-1]
        }])

    chart.render_to_file('C:/Users/wAnnO/Desktop/StarbucksDrinkk/docs/graph/amount_of_sugar.svg')



main()
