"""filter sugar"""
#import zone
import numpy as np
import pandas as pd


def controller():
    data = pd.read_csv('../data/starbucks_drinkMenu_expanded.csv')

    sugar = list()

    for i in range(len(data[' Sugars (g)'])):

        if data[' Sugars (g)'][i] < 16:

            print("%s : %s : %s" %(data['Beverage_category'][i], data['Beverage'][i], \
                data['Beverage_prep'][i]), file=open("teenager.txt", "a"))

controller()

