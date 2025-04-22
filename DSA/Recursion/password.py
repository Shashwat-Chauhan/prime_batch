import sys
from itertools import product

def count_valid_codes(n, m, attempts):
    valid_count = 0
    
    for candidate in product("01", repeat=n):
        candidate = ''.join(candidate)
        valid = True
        
        for attempt, correct_count in attempts:
            count_matches = sum(1 for i in range(n) if candidate[i] == attempt[i])
            if count_matches != correct_count:
                valid = False
                break
        
        if valid:
            valid_count += 1
    
    return valid_count

n, m = map(int, sys.stdin.readline().split())
attempts = [tuple(sys.stdin.readline().split()) for _ in range(m)]
attempts = [(attempt, int(correct_count)) for attempt, correct_count in attempts]

print(count_valid_codes(n, m, attempts))
