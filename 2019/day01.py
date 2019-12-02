#!/usr/bin/env python3
import math

# https://adventofcode.com/2019/day/1
"""
--- Day 1: The Tyranny of the Rocket Equation ---

Santa has become stranded at the edge of the Solar System while delivering presents to other planets! To accurately calculate his position in space, safely align his warp drive, and return to Earth in time to save Christmas, he needs you to bring him measurements from fifty stars.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

The Elves quickly load you into a spacecraft and prepare to launch.

At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. They haven't determined the amount of fuel required yet.

Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

For example:

    For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
    For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
    For a mass of 1969, the fuel required is 654.
    For a mass of 100756, the fuel required is 33583.

The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.

What is the sum of the fuel requirements for all of the modules on your spacecraft?
"""

masses = [
    85824,112173,142065,55390,111295,148584,123987,66433,95844,122580,146901,107700,63930,100389,139126,122243,65950,87443,137945,147755,86370,66749,133758,68317,147417,97202,75113,105996,103130,113328,128427,108580,131832,147958,137067,117676,61678,127254,51090,69924,58966,127437,144987,80181,85474,100216,119810,129946,84880,61614,107350,77076,93028,140464,86826,67901,118846,118658,63646,63328,106271,87376,90156,143507,139729,140393,70324,77304,81383,127336,144535,93496,145119,73128,103189,69519,95701,112919,104766,124188,69855,99495,147075,115498,115468,68706,51445,69871,134449,130838,105809,110721,50893,126521,81542,81384,148523,105748,93331,129279
]

total = 0
for mass in masses:
    fuel = math.floor(mass / 3) - 2
    total += fuel

print(' => total fuel: {}'.format(total))
