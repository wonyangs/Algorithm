def calculate_change(cents_list):
    coin_values = [25, 10, 5, 1]
    results = []

    for cents in cents_list:
        coins = []
        for value in coin_values:
            coins.append(cents // value)
            cents %= value
        results.append(coins)

    return results

cents_list = [int(input()) for _ in range(int(input()))]

results = calculate_change(cents_list)
for result in results:
    print(*result)
