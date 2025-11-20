def compute_hash(s, p=31, m=10**9 + 9):
    n = len(s)
    hash_vals = [0] * (n + 1)
    p_powers = [1] * (n + 1)

    for i in range(1, n + 1):
        p_powers[i] = (p_powers[i - 1] * p) % m

    for i in range(n):
        val = ord(s[i]) - ord('a') + 1
        hash_vals[i + 1] = (hash_vals[i] + val * p_powers[i]) % m

    return hash_vals, p_powers

# Modular inverse using Fermat's Little Theorem
def mod_inverse(x, m):
    return pow(x, m - 2, m)

# Get hash of s[l:r] (0-based, inclusive)
def substring_hash(l, r, hash_vals, p_powers, m=10**9 + 9):
    raw_hash = (hash_vals[r + 1] - hash_vals[l] + m) % m
    norm = mod_inverse(p_powers[l], m)
    return (raw_hash * norm) % m


