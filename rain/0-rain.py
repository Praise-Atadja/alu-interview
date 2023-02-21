#!/usr/bin/python3

"""How many square units of water will be retained after it rains."""

def rain(walls):
    "function that calculates the rainwater retained"


    if len(walls) == 0:
        return 0
    bar_left, bar_right = 0, len(walls) - 1
    bar_leftMax, bar_rightMax = walls[bar_left], walls[bar_right]
    amount_water = 0

    while bar_left < bar_right:
        if bar_leftMax < bar_rightMax:
            bar_left += 1
            bar_leftMax = max(bar_leftMax, walls[bar_left])
            amount_water += bar_leftMax - walls[bar_left]
        else:
            bar_right -= 1
            bar_rightMax = max(bar_rightMax, walls[bar_right])
            amount_water += bar_rightMax - walls[bar_right]
    return amount_water
    