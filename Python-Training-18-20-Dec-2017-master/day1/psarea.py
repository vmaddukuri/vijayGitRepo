"""string formatting
    {:fmt-str}
"""
import math


def compute(radius):
    # function definition
    return math.pi * (radius ** 2)  # exponential operator


try:
    user_radius = float(input('enter the radius :'))
    area = compute(user_radius)  # function calling
    print("radius: {}\narea : {:.3f}".format(user_radius, area))
except ValueError as err:
    print(err)
