#!/usr/bin/python3

"""How many square units of water will be retained after it rains, assuming that the ends of the list (before index 0 
and after index walls[-1]) are not walls, meaning they will not retain water."""

def rain(walls):
    "function that calculates the rainwater retained"

    if len(walls) == 0:
        return 0
    
    bar_right = 0 # height of tallest bar on right
    bar_left = 0 # height of tallest bart on the left
    amount_water = 0 # total amount of water retained

    for height in range(1, len(walls) - 1):
        bar_Left = max(walls[:height])
        bar_ight = max(walls[height+1:])

        reservoir = min(bar_left, bar_right) - walls[height]
        amount_water += max(0, reservoir)
    return amount_water

