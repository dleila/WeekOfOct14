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
acc = 2
for x in range(2, 101):
    acc = acc + x
print(acc)

# Compute the sum of the first 50 odd numbers.
acc = 2
for x in range(1, 51):
    acc = acc + x
print(acc)

# Compute the average of the first 100 odd numbers
acc = 2
for x in range(1, 101):
    acc = acc + x
print(acc/100)

# Write a function that returns the average of the first N numbers, where N is a parameter.
acc = 1
for x in range(1, 10):
    acc = acc + x
n=int(input("Input a number to compute the average of all numbers leading up to it : "))

# Write a function called factorial that computes the product of the first N numbers, where N is a parameter.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factorial : "))
print(factorial(n))


# A Monte Carlo Simulation

import random

print(random.random())

# Boolean expressions
# > greater than
# >= greater than or equal to
# < less than
# <= less than or equal to
# == the same as [equal to]
# != NOT equal to

dogWeight = 25
print(dogWeight != 25)
catWeight = 15

# compound Boolean operators
# and
# or
# not

print(not catWeight < 20)

# Decision Making -- Selection statements
a = 5
b = 10
c = 75

if a > b:
    c = 45

print(c)

if a > b:
    c = 45
    if b > c:
        a = 25
else:
    c = 1050
    if b == a:
        c = 25

print(a, b, c)


d = 55
e = 75
f = 44
ans = 0

if d > e:
    ans = 12
else:
    if d == e:
        ans = 50
    else:
        if f < d * e:
            ans = 100
        else:
            ans = 75
print(ans)

def montePi(numDarts):

    inCircle = 0

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)

        if distance <= 1:
            inCircle = inCircle +1

    pi = inCircle / numDarts * 4
    return pi

print(montePi(10000))

import turtle

def showMontePi(numDarts):
    scn = turtle.Screen()
    t = turtle.Turtle()

    scn.setworldcoordinates(-1, -1, 1, 1)

    t.penup()
    t.goto(-1, 0)
    t.pendown()
    t.goto(1, 0)

    t.penup()
    t.goto(0, 1)
    t.pendown()
    t.goto(0, -1)

    inCircle = 0
    t.penup()

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)

        t.goto(x, y)

        if distance <= 1:
            inCircle = inCircle + 1
            t.color("Blue")
        else:
            t.color("Red")

        t.dot()

    pi = inCircle / numDarts * 4
    scn.exitonclick()
    return pi

showMontePi(1000)

# Your Task:
# Modify the simulation to plot point in the entire circle.
# You will have to adjust the calculated value of pi accordingly.
