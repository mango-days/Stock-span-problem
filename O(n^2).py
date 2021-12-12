# Stock span problem

# The stock span problem is a financial problem where we have a series of n daily price quotes for a stock and we need to calculate the span of stock’s price for all n days. 

# The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days just before the given day, for which the price of the stock on the current day is less than or equal to its price on the given day.

# For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85}, then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}.

prices = [ 100, 80, 60, 70, 60, 75, 85 ]
span = []

for index1 in range ( 0 , len ( prices ) ) :
    
    stock_span = 0
    index2 = index1
    
    while index2 != 0 :
        
        if prices [ index2 ] <= prices [ index1 ] :
            stock_span += 1
            
        else : break
    
        index2 -= 1
        
    if index1 == index2 : 
        stock_span += 1
        
    span.append ( stock_span )
    
print ( span )

