class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0

        # dp[i] = number of ways to decode s[:i]
        dp = [0] * (n + 1)
        dp[0] = 1  # empty string: one way (do nothing)
        dp[1] = 1  # first char already checked non-zero

        for i in range(2, n + 1):
            one_digit = int(s[i - 1])
            two_digit = int(s[i - 2:i])

            if one_digit >= 1:  # single digit 1-9
                dp[i] += dp[i - 1]

            if 10 <= two_digit <= 26:  # two digits 10-26
                dp[i] += dp[i - 2]

        return dp[n]