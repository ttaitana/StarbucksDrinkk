import pandas as pd
import pygal as pg

def main():
    raw_data = pd.read_csv('../Data/starbucks_drinkMenu_expanded.csv')
    #print(pd.DataFrame.keys(raw_data))

    beverage_index = [[0, 4], [4, 62], [62, 102], [102, 154],\
                      [154, 172], [172, 181], [181, 217], [217, 229], [229, 238]]

    for i in beverage_index:
        for j in range(i[0], i[1]):
            print("%s : %s : %d" %(raw_data['Beverage_category'][j], raw_data['Beverage_prep'][j], raw_data[' Sugars (g)'][j]))
        print('----------------------------------------')


main()
