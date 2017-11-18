import pandas as pd
import pygal as pg
from pygal.style import DarkSolarizedStyle

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
    #filered_data = dict()
    #filered_data = catagories(data, filered_data)
    #scatter = dict()
    #scatter = scatter_filter(data, scatter)
    #scatter_graph(scatter)
    #pie_graph(filered_data)
    #dot_graph(filered_data)
    bar_sugar = bar_filter(data, dict())
    result = dict()
    for i in bar_sugar:
        result[i] = sum(bar_sugar[i])/len(bar_sugar[i])
    bar_graph(result)
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
def catagories(data, filered_data):
    for i in range(len(data['Beverage_category'])):
        if data['Beverage_category'][i] not in filered_data:
            filered_data[data['Beverage_category'][i]] = [data['Calories'][i]]
        else:
            filered_data[data['Beverage_category'][i]].append(data['Calories'][i])
    return filered_data


def scatter_filter(data, scatter):
    for i in range(len(data['Calories'])):
        if data['Beverage_category'][i] not in scatter:
            scatter[data['Beverage_category'][i]] = [data['Calories'][i], data[' Sugars (g)'][i]]
        else:
            scatter[data['Beverage_category'][i]].append((data['Calories'][i], data[' Sugars (g)'][i]))
    return scatter

def bar_filter(data, bar):
    for i in range(len(data[' Sugars (g)'])):
        if data['Beverage_category'][i] not in bar:
            bar[data['Beverage_category'][i]] = [data[' Sugars (g)'][i]]
        else:
            bar[data['Beverage_category'][i]].append(data[' Sugars (g)'][i])
    return bar

"""
=========================================================================================================================================================

 ██████╗ ██████╗  █████╗ ██████╗ ██╗  ██╗    ███╗   ███╗ █████╗ ██╗  ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██║  ██║    ████╗ ████║██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
██║  ███╗██████╔╝███████║██████╔╝███████║    ██╔████╔██║███████║█████╔╝ █████╗  ██████╔╝
██║   ██║██╔══██╗██╔══██║██╔═══╝ ██╔══██║    ██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║  ██║██║     ██║  ██║    ██║ ╚═╝ ██║██║  ██║██║  ██╗███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
"""
def pie_graph(data):
    pie_chart = pg.Pie()
    pie_chart.title = 'Amount of calcories in each Starbucks Beverage calcories'
    for i in data:
        pie_chart.add(i, max(data[i]))
    pie_chart.render_to_file('D:/chart.svg')


def dot_graph(data):
    dot_chart = pg.Dot(x_label_rotation=30, dots_size=100)
    dot_chart.title = 'Amount of calcories in each Starbucks Beverage calcories'
    dot_chart.x_labels = [i for i in data]
    for i in data:
        dot_chart.add(i, data[i])
    dot_chart.render_to_file('D:/chart.svg')


def scatter_graph(data):
    xy_chart = pg.XY(stroke=False)
    xy_chart.title = 'Overview amount of x(Calories) and Y(Sugars)'
    for i in data:
        xy_chart.add(i, data[i])
    xy_chart.render_to_file('D:/chart.svg')

def bar_graph(data):
    bar_chart = pg.HorizontalBar()
    bar_chart.title = 'Amount of sugar in each Starbucks Beverage'
    #bar_chart.x_labels = [i.split()[1] if len(i.split()) > 1 else i.split()[0] for i in data]
    _ = [bar_chart.add(i, round(data[i], 2)) for i in data if data[i]!=0 ]
    bar_chart.render_to_file('D:/chart.svg')



main()
