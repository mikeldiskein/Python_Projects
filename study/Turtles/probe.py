import turtle as t
from math import pi
t.color('black')

for i in range(1000):
    t.forward(i)
    t.right(20 + 0.1*i)

