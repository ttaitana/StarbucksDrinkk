import pandas as pd
def main():
    raw_data = pd.read_csv('StarbucksDrinkk/Data/starbucks_drinkMenu_expanded.csv')

    beverage = dict() #making dict for {beverage:[vlues]}
    for i in range(179, 213): #chage Number to index (see index in Data/beverage-index)
        if raw_data['Beverage'][i] not in beverage:
            beverage[raw_data['Beverage'][i]] = [raw_data[' Sugars (g)'][i]]
        else:
            beverage[raw_data['Beverage'][i]].append(raw_data[' Sugars (g)'][i])

#find sugar avg
    sugar_avg = 0
    for i in beverage:
        sugar_avg += sum(beverage[i])
    sugar_avg /= 58


#graph making zone
    graph = pg.SolidGauge(show_legend=True,
            half_pie=True,
            inner_radius=0.70,
            style=custom_style,legend_at_bottom=True)

    graph.title             =   raw_data['Beverage_category'][179, 213] #change name to index number between 1st - last index of beverage
    percent_formatter       =   lambda x: '{:.4g}%'.format(x)
    graph.value_formatter   =   percent_formatter

    for i in beverage:
        graph.add(i, ( sum(beverage[i]) / len(beverage[i]) ) / sugar_avg*100)

    graph.render_to_file('D:\Frappuccino® Blended Coffee.svg') #eg: 'D:/Graph.svg'

main()
