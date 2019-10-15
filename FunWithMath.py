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

for sides in range(2, 100, 2):
    print(sides, archimedes(sides))

# Experiment with the loop above alongside the actual value of Pi.
# How many sides does it take to make these two close?
    # It takes 2 sides to make the answer be the same on the second replay of the loop.
