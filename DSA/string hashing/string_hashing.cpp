#include <iostream>
#include <vector>
#include <string>
using namespace std;

typedef long long ll;
const ll P = 31;             // Prime base
const ll M = 1e9 + 9;        // Modulus for hashing

vector<ll> hash_vals, p_powers;

// Function to compute prefix hashes and powers of P
void compute_hash(const string &s, ll p = P, ll m = M) {
    int n = s.size();
    hash_vals.resize(n + 1, 0);
    p_powers.resize(n + 1, 1);

    for (int i = 1; i <= n; ++i) {
        p_powers[i] = (p_powers[i - 1] * p) % m;
    }

    for (int i = 0; i < n; ++i) {
        ll val = s[i] - 'a' + 1;  // Map 'a' -> 1, 'b' -> 2, etc.
        hash_vals[i + 1] = (hash_vals[i] + val * p_powers[i]) % m;
    }
}

// Function to compute hash of substring s[l...r] (0-based)
ll substring_hash(int l, int r, ll m = M) {
    ll raw_hash = (hash_vals[r + 1] - hash_vals[l] + m) % m;
    // Use modular inverse of p_powers[l] for correct normalization
    return (raw_hash * p_powers[p_powers.size() - 2 - l]) % m;
}

int main() {
    string s = "abcabc";
    compute_hash(s);

    // Example: hash of substring s[0...2] = "abc"
    int l = 0, r = 2;
    cout << "Hash of substring \"" << s.substr(l, r - l + 1) << "\" = " << substring_hash(l, r) << endl;

    return 0;
}
