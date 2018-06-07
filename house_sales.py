"""
2: Given a CSV listing homes sold, the sale date, and the ZIP code of the home, write a script to print out how many homes were sold each day.
3: Building on question 2, expand that script to break down the homes sold per day by ZIP code. Your output should look like:
Date,76325,789123,54375 07/13/2018,4,0,2 08/04/2017,6,9,0
"""

import pandas as pd 
import numpy as np 

xl = pd.read_excel('sales_data.xls')

col_list = list(xl)
col_list.remove('Date')
xl['Total sales'] = xl[col_list].sum(axis=1)

print(xl['Total sales'])



	


