# Stock Market

import sys


def stocks(stockPrices):
    # method to print highest and lowest stock prices
    prices = stockPrices.split(',')
    # convert each price to an integer
    prices = list(map(int, prices))

    # initialize the max and min prices
    max_price = -sys.maxsize - 1
    min_price = sys.maxsize
    ind_min, ind_max = 0, 0

    # iterate on the prices list and store the results
    for index, price in enumerate(prices):
        if price > max_price:
            max_price = price
            ind_max = index

        if price < min_price:
            min_price = price
            ind_min = index

    # display the output as asked in the question
    print("Highest price : {} occurred on day # {}".format(max_price, ind_max))
    print("Lowest price : {} occurred on day # {}".format(min_price, ind_min))


if __name__ == '__main__':
    # main method to take input string and call the method above to test
    stockPrices = input("Please enter stock prices : ")
    stocks(stockPrices)