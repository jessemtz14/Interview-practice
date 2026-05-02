# Buy and Sell Stock
# You are given an array prices where prices[i] is the price 
# of a given stock on the ith day.
# return the max profit you can achieve from buying once and selling 
# once after buying

def max_profit_brute(prices):
    min_price = float('inf')

    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        profit  = price - min_price
        max_profit = max(max_profit, price - min_price)
        
    return max_profit


# test case
if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    result = max_profit_brute(prices)
    print(result)  # Output: 5
    if result == 5:
        print("Test case passed!")    
    else:
        print("Test case failed!")                                                                                                                                                                                                                                              