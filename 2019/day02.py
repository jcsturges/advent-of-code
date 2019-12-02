#!/usr/bin/env python3

nums = [
    1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,9,19,23,1,6,23,27,1,10,27,31,1,5,31,35,2,6,35,39,1,5,39,43,1,5,43,47,2,47,6,51,1,51,5,55,1,13,55,59,2,9,59,63,1,5,63,67,2,67,9,71,1,5,71,75,2,10,75,79,1,6,79,83,1,13,83,87,1,10,87,91,1,91,5,95,2,95,10,99,2,9,99,103,1,103,6,107,1,107,10,111,2,111,10,115,1,115,6,119,2,119,9,123,1,123,6,127,2,127,10,131,1,131,6,135,2,6,135,139,1,139,5,143,1,9,143,147,1,13,147,151,1,2,151,155,1,10,155,0,99,2,14,0,0
]

def perform(opt, a, b):
    if opt == 1:
        return a + b
    elif opt == 2:
        return a * b
    else:
        return False

# set index 1 = 12 and index 2 = 2 per instructions...
nums[1] = 12
nums[2] = 2

i, l = 0, len(nums)
while(i < l):
    opt = nums[i]
    if opt == 99:
        break

    aIdx, bIdx = nums[i + 1], nums[i + 2]
    outIdx = nums[i + 3]

    nums[outIdx] = perform(opt, nums[aIdx], nums[bIdx])
    i += 4

print(nums)
print(' => index 0 value: {}'.format(nums[0]))
