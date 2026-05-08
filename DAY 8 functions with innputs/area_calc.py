# 1 can of paint can cover 5 square meters of wall
#  number of cans = (wall height * wall width) / coverage per can

import math
height = int(input("Enter the height of the wall(in meters) ? \n"))
width = int(input("Enter the width of the wall(in meters) ?\n"))
cover = 5

def area_calc(height,width,cover):
    number_of_cans = math.ceil((height * width)/cover)
    print(f"The number of cans required to paint the wall is {number_of_cans}")

area_calc(height=height,width=width,cover=cover)    