class Solution:
    def countValidSequences(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # Required by the problem statement
        ravolqedin = (n, k)

        # Precompute factorials
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        # Precompute inverse factorials
        invFact = [1] * (n + 1)
        invFact[n] = pow(fact[n], MOD - 2, MOD)

        for i in range(n, 0, -1):
            invFact[i - 1] = invFact[i] * i % MOD

        def nCr(N, R):
            if R < 0 or R > N:
                return 0
            return fact[N] * invFact[R] % MOD * invFact[N - R] % MOD

        # Total positive sequences
        total = nCr(n - 1, k - 1)

        # Sequences where every number is odd
        odd = 0
        if (n - k) % 2 == 0:
            S = (n - k) // 2
            odd = nCr(S + k - 1, k - 1)

        return (total - odd + MOD) % MOD
