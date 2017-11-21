import pandas as pd
import pygal as pg

from pygal.style import Style
custom_style = Style(
  background='transparent',
  colors=('#18301e', '#0B421A', '#00723F', '#EAC784', '#e5a632', '#604C4C', '#BBBBBB', '#AAAAAA'),
  value_colors = '#212320')

def main():
    raw_data = pd.read_csv('../data/starbucks_drinkMenu_expanded.csv')

main()
