import time

calls = 0


def fib_naive(n):
    global calls

    calls += 1

    if n <= 1:
        return n

    return fib_naive(n - 1) + fib_naive(n - 2)


memo = {}


def fib_memo(n):
    if n <= 1:
        return n

    if n not in memo:
        memo[n] = fib_memo(n - 1) + fib_memo(n - 2)

    return memo[n]


def fib_table(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


n = 25

print("naive :", fib_naive(n), "calls:", calls)
print("memo :", fib_memo(n))
print("table :", fib_table(n))

t = time.time()
fib_table(5000)
print("table(5000) finished in under a second:", time.time() - t < 1)
