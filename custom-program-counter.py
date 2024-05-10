import time
import threading
from pynput.mouse import Listener, Button

count = 0
start_counting = False
stop_counting = False

def on_click(x, y, button, pressed):
    global start_counting, stop_counting
    
    if button == Button.right and pressed:
        start_counting = True
    elif button == Button.middle and pressed:
        stop_counting = True
        return False  # Stop the listener

def count_numbers():
    global count, start_counting, stop_counting
    
    while True:
        if start_counting:
            count += 1
            print(count)
        if stop_counting:
            print("Counting stopped.")
            break
        time.sleep(0.74)

def start_listener():
    with Listener(on_click=on_click) as listener:
        listener.join()

if __name__ == "__main__":
    counting_thread = threading.Thread(target=count_numbers)
    counting_thread.daemon = True
    counting_thread.start()
    
    start_listener()


# import random

# # Lookup table for actual constants and maximum number of trials
# lookup_table = {
#     0.05: (0.00380, 263),
#     0.10: (0.01475, 67),
#     0.15: (0.03221, 31),
#     0.17: (0.04214, 24),
#     0.20: (0.05570, 17),
#     0.25: (0.08475, 11),
#     0.30: (0.11895, 8),
#     0.3333: (0.13929, 7), 
#     0.35: (0.14628, 6),
#     0.40: (0.18128, 5),
#     0.45: (0.21867, 4),
#     0.50: (0.25701, 3),
#     0.55: (0.29509, 3),
#     0.60: (0.33324, 3),
#     0.65: (0.38109, 2),
#     0.70: (0.42448, 2),
# }

# def prd_critical_strike(chance, num_iterations, num_simulations):
#     total_results = {True: 0, False: 0}  # Aggregate results over all simulations
#     for _ in range(num_simulations):
#         results = {True: 0, False: 0}  # Results for a single simulation
#         count = 1  # Count of consecutive non-critical strikes
#         C, max_N = lookup_table[chance]  # Get the actual constant and maximum number of trials
#         for _ in range(num_iterations):
#             if random.random() < count * C or count >= max_N:
#                 results[True] += 1
#                 count = 1  # Reset the count
#             else:
#                 count += 1  # Increase the count
#                 results[False] += 1
#         # Aggregate results from the current simulation
#         total_results[True] += results[True]
#         total_results[False] += results[False]
#     # Calculate averages over all simulations
#     avg_results = {k: v / num_simulations for k, v in total_results.items()}
#     return avg_results

# # Simulate 1000 attacks with a base critical strike chance of 25% over 1000 simulations
# results = prd_critical_strike(0.3333, 1000, 1000)

# print(f"Critical strikes: {results[True]}")
# print(f"Normal hits: {results[False]}")
