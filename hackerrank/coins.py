import sys


def minCoins(coins, m, V):
    table = [0 for i in range(V + 1)]

    table[0] = 0

    for i in range(1, V + 1):
        table[i] = sys.maxsize

    for i in range(1, V + 1):

        for j in range(m):
            if coins[j] <= i:
                sub = table[i - coins[j]]
                if (sub != sys.maxsize and
                        sub + 1 < table[i]):
                    table[i] = sub + 1
    return table[V]


if __name__ == "__main__":
    total = input("enter total $")
    V = int(total)
    coins = [1, 3, 5]
    m = len(coins)

    print("Minimum coins required is",
          minCoins(coins, m, V))
