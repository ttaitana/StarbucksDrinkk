import pandas as pd
import pygal as pg

from pygal.style import Style
custom_style = Style(
  background='transparent',
  colors=('#18301e', '#0B421A', '#00723F', '#EAC784', '#e5a632', '#604C4C', '#BBBBBB', '#AAAAAA'),
  value_colors = '#212320')

def main():
    f = open("file.txt", "w")
    raw_data = pd.read_csv('../Data/starbucks_drinkMenu_expanded.csv')



    for i in range(len(raw_data)):
        if raw_data[' Sugars (g)'][i] < 37.5:
            f.write(str(raw_data['Beverage_category'][i]))
            f.write('\t')
            f.write(str(raw_data['Beverage'][i]))
            f.write('\t')
            f.write(str(raw_data['Beverage_prep'][i]))
            f.write('\t')   
            f.write(str(raw_data[' Sugars (g)'][i]))
            f.write('\n')

    # print(pd.DataFrame.keys(raw_data))
    f.close()
main()
