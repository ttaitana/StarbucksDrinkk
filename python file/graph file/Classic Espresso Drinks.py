import pandas as pd
import pygal as pg
from pygal.style import Style
custom_style = Style(
  background='transparent',
  colors=('#00723F', '#0B421A', '#00723F', '#EAC784', '#e5a632', '#604C4C', '#BBBBBB', '#AAAAAA'))

def teenager():
    raw_data = pd.read_csv('../../Data/starbucks_drinkMenu_expanded.csv')
    beverage = dict()
    #get Beverage for Classic Espresso Drinks
    for i in range(4, 62):
        if raw_data['Beverage'][i] not in beverage:
            beverage[raw_data['Beverage'][i]] = [raw_data[' Sugars (g)'][i]]
        else:
            beverage[raw_data['Beverage'][i]].append(raw_data[' Sugars (g)'][i])

    #find sugar avg
    sugar_avg = 0
    for i in beverage:
        sugar_avg += sum(beverage[i])
    sugar_avg /= 58


    graph = pg.SolidGauge(show_legend=True,
            half_pie=True,
            inner_radius=0.70,
            style=custom_style,legend_at_bottom=True)

    graph.title             =   raw_data['Beverage_category'][4]
    percent_formatter       =   lambda x: '{:.4g}%'.format(x)
    graph.value_formatter   =   percent_formatter

    for i in beverage:
        graph.add(i, (sum(beverage[i])/len(beverage[i]))/sugar_avg*100)

    graph.render_to_file('C:/Users/wAnnO/Desktop/StarbucksDrinkk/docs/graph/sugar.svg')

teenager()
