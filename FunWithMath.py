# Starting off
print(22 / 7)
print(355 / 113)
import math

print(9801 / (2206 * math.sqrt(2)))


def archimedes(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfSideS = math.sin(math.radians(halfAngleA))
    sides = oneHalfSideS * 2
    polygonCircumference = numSides * sides
    pi = polygonCircumference / 2
    return pi


print(archimedes(8))
print(archimedes(16))

for sides in range(8, 100, 8):
    print(sides, archimedes(sides))

# Experiment with the loop above alongside the actual value of Pi.
# How many sides does it take to make these two close?
    # It takes 2 sides to make the answer be the same on the second replay of the loop.

# Accumulators

acc = 0
for x in range(1, 6):
    acc = acc + x
# We basically added 1+2+3+4+5 to get 15.

print(acc)

# Compute the sum of the first 100 even numbers.
# Compute the sum of the first 50 odd numbers.
# Compute the average of the first 100 odd numbers
# Write a function that returns the average of the first N numbers, where N is a parameter.
# Write a function called factorial that computes the product of the first N numbers, where N is a parameter.
# Each number the tht Fibonacci sequence is the sum of the previous two numbers.
    # First two numbers in sequence are 1 and 1. Compute the 10th Fibonacci number
# Write a function to compute the Nth Fibonacci number where N is a parameter.
    # You may assume that N will be grater than or equal to 3.
