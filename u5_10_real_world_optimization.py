def knapsack_01(items, capacity):
    n = len(items)

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, value, w = items[i - 1]

        for c in range(capacity + 1):
            dp[i][c] = dp[i - 1][c]

            if w <= c:
                dp[i][c] = max(
                    dp[i][c],
                    dp[i - 1][c - w] + value
                )

    chosen = []
    c = capacity

    for i in range(n, 0, -1):
        if dp[i][c] != dp[i - 1][c]:
            chosen.append(items[i - 1][0])
            c -= items[i - 1][2]

    return dp[n][capacity], list(reversed(chosen))


def min_coins(coins, amount):
    INF = float("inf")
    dp = [0] + [INF] * amount

    for a in range(1, amount + 1):
        for c in coins:
            if c <= a and dp[a - c] + 1 < dp[a]:
                dp[a] = dp[a - c] + 1

    return dp[amount]


def greedy_coins(coins, amount):
    count = 0

    for c in sorted(coins, reverse=True):
        count += amount // c
        amount %= c

    return count


topics = [
    ("Trees", 10, 3),
    ("Graphs", 12, 4),
    ("Hashing", 5, 2),
    ("DP", 14, 5),
    ("Greedy", 8, 3)
]

print(
    "Best marks and topics for 8 study hours:",
    knapsack_01(topics, 8)
)

print(
    "Coins {4,3,1,5}, v=7 -> DP:",
    min_coins([4, 3, 1, 5], 7),
    "| greedy:",
    greedy_coins([4, 3, 1, 5], 7)
)

print(
    "Coins {1,3,4}, v=6 -> DP:",
    min_coins([1, 3, 4], 6),
    "| greedy:",
    greedy_coins([1, 3, 4], 6)
)
