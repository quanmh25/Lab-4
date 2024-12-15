from itertools import combinations
from math import *


# List of items (name, size, value)
stuffs = {
    'r': ('rifle', 3, 25),
    'p': ('pistol', 2, 15),
    'a': ('ammo', 2, 15),
    'm': ('medkit', 2, 20),
    'i': ('inhaler', 1, 5),  # Mandatory
    'k': ('knife', 1, 15),
    'x': ('axe', 3, 20),
    't': ('talisman', 1, 25),
    'f': ('flask', 1, 15),
    'd': ('antidot', 1, 10),
    's': ('supplies', 2, 20),
    'c': ('crossbow', 2, 20),
}

# Function to calculate and trace optimal items 
def mainPart():
    # Ensure 'i' (inhaler) is always included
    res = ['i']  
    space = max_space - stuffs['i'][1] 

    # Calculate remaining items (excluding 'i')
    items = [item for item in stuffs if item != 'i']
    sizes = [stuffs[item][1] for item in items]
    values = [stuffs[item][2] for item in items]

    # Create DP table for remaining items
    dp = [[0] * (space + 1) for _ in range(len(items) + 1)]
    for i in range(len(items)):
        for j in range(space + 1):
            dp[i + 1][j] = dp[i][j]
            if j >= sizes[i]:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - sizes[i]] + values[i])


    # Trace back from DP table to find the optimal set of remaining items
    remaining_space = space
    for i in range(len(items), 0, -1):
        if dp[i][remaining_space] != dp[i - 1][remaining_space]:        # If item is selected
            res.append(items[i - 1])
            remaining_space -= sizes[i - 1]


    # Arrange the backpack into a 3x3 matrix
    backpack = [["" for _ in range(3)] for _ in range(3)]
    index = 0
    for item in res:
        if index < 9:
            row = index // 3
            col = index % 3
            backpack[row][col] = f"[{item}]"
            index += 1

    # Display the backpack
    print("Backpack:")
    for row in backpack:
        print(" ".join(row))

    # Calculate total points
    total_points = current_points + sum(stuffs[item][2] for item in res)
    penalty_points = sum(stuffs[item][2] for item in stuffs if item not in res)

    print(f"Total survival points: {total_points - penalty_points}")


def extraPart():
    new_max = 7
    show = []
    for x in range(1, n + 1):
        for comb in combinations(stuffs.keys(), x):
            if 'i' in comb:
                total_space = 0
                total_survival = 10
                penalty_survival = 0

                for item in comb:
                    total_space += stuffs[item][1]
                    total_survival += stuffs[item][2]
                for item in stuffs:
                    if item not in comb:
                        penalty_survival += stuffs[item][2]

                final = total_survival - penalty_survival
                if  total_space <= new_max and final > 0:
                    show.append((comb, final))

                # print(f"Combination: {comb}")
                # print(f"Total space: {total_space}")
                # print(f"Total survival points: {total_survival}")
                # print(f"Penalty survival points: {penalty_survival}")
                # print(f"Final survival points: {final}")

    if show:
        for i, (comb, final) in enumerate(show, 1):
            print(f"Combination {i} : {comb} - Survival points: {final}")
    else:
        print("No valid combinations found.")


if __name__ == '__main__':
    n = len(stuffs)  # Number of items
    max_space = 9    # Backpack's size (3x3)
    current_points = 10

    # Size and Value of each item
    size = [stuffs[item][1] for item in stuffs]
    value = [stuffs[item][2] for item in stuffs]
    
    mainPart()
    extraPart()

