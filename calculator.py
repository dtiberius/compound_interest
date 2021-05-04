'''
App: How rich will I be?
Function: Calculates compound interest (applied monthly), based on custom user input.
Author: Dan Welsh
'''

def monthly_compound_interest(initial, monthly, years, annual_rate):
    sum = initial
    months = years * 12
    annual_rate = annual_rate/100
    for month in range(int(months)):
        sum = sum * (1 + annual_rate/12)
        sum = sum + monthly
    return sum