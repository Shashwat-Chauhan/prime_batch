# Given coins of currency 2000 , 500 , 200 , 100, 50, 20 , 10 , 5 , 2 , 1
# You have to find the minimum number of coins required to form a given number

from math import remainder


coins = [2000 , 500 , 200 , 100, 50, 20 , 10 , 5 , 2 , 1]
amount_to_form = 3960

def min_coins_req(coins: list[int] , amount_to_form: int) -> int:

    count = 0
    remaining = amount_to_form
    while(remaining != 0):
        for coin in coins:
            if coin <= remaining:
                remaining -= coin
                count += 1
                break
    return count

ans = min_coins_req(coins , amount_to_form)
print(ans)


def min_coins(coins: list[int] , amount_to_form: int) -> int:
    count = 0
    remaining = amount_to_form

    for coin in coins:
        if remaining == 0:
            break
        to_pick = remaining / coin
        remaining -= to_pick * coin
        count += to_pick
    
    return count

ans2 = min_coins(coins , amou 
nt_to_form)
print(ans2)