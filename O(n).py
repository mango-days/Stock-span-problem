# Stock span problem

# The stock span problem is a financial problem where we have a series of n daily price quotes for a stock and we need to calculate the span of stock’s price for all n days. 

# The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days just before the given day, for which the price of the stock on the current day is less than or equal to its price on the given day.

prices = [ 100, 80, 60, 70, 60, 75, 85 ]
span = [ 1 ]

for index in range ( 1 , len ( prices ) ) :
    stock_span = 1
    
    if prices [ index ] >= prices [ index - 1 ] : 
        stock_span += span [ index - 1 ] 
        
    span.append ( stock_span )
    
print ( span )
