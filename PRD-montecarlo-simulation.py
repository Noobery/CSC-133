import random
import matplotlib.pyplot as plt

# Lookup table for actual constants and maximum number of trials
lookup_table = {
    0.05: (0.00380, 263),
    0.10: (0.01475, 67),
    0.15: (0.03221, 31),
    0.17: (0.04214, 24),
    0.20: (0.05570, 17),
    0.25: (0.08475, 11),
    0.30: (0.11895, 8),
    0.3333: (0.13929, 7), 
    0.35: (0.14628, 6),
    0.40: (0.18128, 5),
    0.45: (0.21867, 4),
    0.50: (0.25701, 3),
    0.55: (0.29509, 3),
    0.60: (0.33324, 3),
    0.65: (0.38109, 2),
    0.70: (0.42448, 2),
}

def prd_montecarlo(chance, num_iterations, num_simulations):
    total_results = {True: 0, False: 0}  # Aggregate results over all simulations
    for _ in range(num_simulations):
        results = {True: 0, False: 0}  # Results for a single simulation
        count = 1  # Count of consecutive non-critical strikes
        C, max_N = lookup_table[chance]  # Get the actual constant and maximum number of trials
        for _ in range(num_iterations):
            if random.random() < count * C or count >= max_N:
                results[True] += 1
                count = 1  # Reset the count
            else:
                count += 1  # Increase the count
                results[False] += 1
        # Aggregate results from the current simulation
        total_results[True] += results[True]
        total_results[False] += results[False]
    # Calculate averages over all simulations
    avg_results = {k: v / num_simulations for k, v in total_results.items()}
    return avg_results

# Simulate 1000 attacks with a base critical strike chance over 1000 simulations
chances = sorted(lookup_table.keys())
true_probabilities = []
for chance in chances:
    results = prd_montecarlo(chance, 1000, 1000)
    true_probabilities.append(results[True])

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(chances, true_probabilities, marker='o', linestyle='-')
plt.xlabel('Passive Skill Probability') 
plt.ylabel('True Probability of PRD Percentages')
plt.title('True Probability vs. Chance for PRD')
plt.grid(True)
plt.show()
