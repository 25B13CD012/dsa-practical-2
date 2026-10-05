def fractional_knapsack(items, capacity):
    ranked = sorted(
        items,
        key=lambda item: item[1] / item[2],
        reverse=True
    )

    total_value = 0.0
    remaining = capacity

    for name, value, weight in ranked:
        if remaining == 0:
            break

        take = min(weight, remaining)
        gained = value * take / weight

        total_value += gained
        remaining -= take

        print(f"Take {take} kg of {name:7} -> value {gained:.1f}")

    return total_value


items = [
    ("Gold", 60, 10),
    ("Silver", 100, 20),
    ("Bronze", 120, 30)
]

best = fractional_knapsack(items, 50)

print("Best value:", best)
