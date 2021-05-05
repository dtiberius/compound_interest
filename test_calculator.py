# cannot locate
def nothing():
    assert True

# highlight function naming convention
def test_nothing():
    assert True

from calculator import monthly_compound_interest

# try to make an actual test
def test_zeroes():
    # define what are we talking about
    initial = 0
    monthly = 0
    years = 0
    annual_rate = 0
    # calculate stuff
    final_sum = monthly_compound_interest(initial, monthly, years, annual_rate)
    # check it's right
    assert final_sum == 0

def test_cash():
    # define what are we talking about
    initial = 3000
    monthly = 100
    years = 10
    annual_rate = 0
    # calculate stuff
    final_sum = monthly_compound_interest(initial, monthly, years, annual_rate)
    # check it's right
    assert final_sum == 15000

def test_one_month():
    # define what are we talking about
    initial = 1000
    monthly = 100
    years = 1/12
    annual_rate = 12
    # calculate stuff
    final_sum = monthly_compound_interest(initial, monthly, years, annual_rate)
    # check it's right
    assert final_sum == 1110
