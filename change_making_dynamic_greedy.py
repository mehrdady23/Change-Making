import sys
import time

# Dynamic Programming Solution
def dynamic_programming_change(n, k, d):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for j in range(k):
            if i >= d[j]:
                dp[i] = min(dp[i], dp[i - d[j]] + 1)

    coins_used = []
    i = n
    while i > 0:
        for j in range(k):
            if i >= d[j] and dp[i] == dp[i - d[j]] + 1:
                coins_used.append(d[j])
                i -= d[j]
                break

    return coins_used, dp[n]


# Greedy Algorithm solution
def greedy_change_making(n, k, d):
    coins_used = []
    i = k - 1

    while n > 0 and i >= 0:
        while n >= d[i]:
            coins_used.append(d[i])
            n -= d[i]
        i -= 1

    return coins_used, len(coins_used)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python change_making_dynamic_greedy.py <n> <k> <d>")
        sys.exit(1)

    n = int(sys.argv[1])
    k = int(sys.argv[2])
    d = list(map(int, sys.argv[3].split()))

    start_time = time.time()
    dp_coins, dp_count = dynamic_programming_change(n, k, d)
    dp_time = time.time() - start_time

    start_time = time.time()
    greedy_coins, greedy_count = greedy_change_making(n, k, d)
    greedy_time = time.time() - start_time

    print("Dynamic Programming Solution:")
    print("Coins used:", dp_coins)
    print("Number of coins:", dp_count)
    print("Time taken:", dp_time, "nanoseconds")

    print("\nGreedy Solution:")
    print("Coins used:", greedy_coins)
    print("Number of coins:", greedy_count)
    print("Time taken:", greedy_time, "nanoseconds")
