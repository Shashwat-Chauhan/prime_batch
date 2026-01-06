# In a candy store, there are different types of candies available and prices[i] represent the price of  ith types of candies. You are now provided with an attractive offer.
# For every candy you buy from the store, you can get up to k other different candies for free. Find the minimum and maximum amount of money needed to buy all the candies.
# Note: In both cases, you must take the maximum number of free candies possible during each purchase.

# Examples :

# Input: prices[] = [3, 2, 1, 4], k = 2
# Output: [3, 7]
# Explanation: As according to the offer if you buy one candy you can take at most k more for free. So in the first case, you buy the candy worth 1 and takes candies worth 3 and 4 for free, also you need to buy candy worth 2. So min cost: 1+2 = 3. In the second case, you can buy the candy worth 4 and takes candies worth 1 and 2 for free, also you need to buy candy worth 3. So max cost: 3+4 = 7.


prices = [3, 2, 1, 4] 
k = 2

def find_min_cost(prices: list[int] , k:int)-> int:
    i = 0
    j = len(prices) - 1
    cost = 0
    prices = sorted(prices)
    while(i <= j):
        cost += prices[i]
        j -= k
        i+=1
    
    return cost

minimum_cost = find_min_cost(prices , k)
print(minimum_cost)

