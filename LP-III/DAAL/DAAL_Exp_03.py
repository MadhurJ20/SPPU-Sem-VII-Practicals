'''
Madhur Jaripatke
Roll No. 52
BE A Computer
RMDSSOE, Warje, Pune
'''
'''
Write a program to solve a fractional Knapsack problem using a greedy method.
'''
class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

def fractional_knapsack(items, capacity):
    # Calculate the value-to-weight ratio for each item
    value_weight_ratio = [(item.value / item.weight, item) for item in items]

    # Sort items in decreasing order of value-to-weight ratio
    value_weight_ratio.sort(reverse=True)

    total_value = 0.0
    knapsack = []

    for ratio, item in value_weight_ratio:
        if capacity == 0:
            break

        weight = min(item.weight, capacity)
        total_value += weight * ratio
        capacity -= weight

        knapsack.append((item, weight))

    return total_value, knapsack

# Example usage
if __name__ == "__main__":
    items = [Item(10, 60), Item(20, 100), Item(30, 120)]
    max_capacity = 50

    max_value, selected_items = fractional_knapsack(items, max_capacity)

    print("Selected Items:")
    for item, weight in selected_items:
        print(f"Item with weight {item.weight} and value {item.value} (fraction taken: {weight / item.weight})")

    print(f"Maximum value achievable: {max_value}")
