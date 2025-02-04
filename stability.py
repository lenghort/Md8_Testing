import math

def f(x):
    return math.tan(x)

x = 1.57076
eps = 1e-10

print(int(f(x + eps)))
print(int(f(x - eps)))