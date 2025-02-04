def bisection_method(f, a, b, tolerance=1e-6, max_iterations=100):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")

    iteration = 0
    while (b - a) / 2 > tolerance and iteration < max_iterations:
        m = (a + b) / 2
        fm = f(m)

        print(f"Iteration {iteration + 1}: a = {a}, b = {b}, m = {m}, f(m) = {fm}")

        if fm == 0:
            return m
        elif f(a) * fm < 0:
            b = m
        else:
            a = m

        iteration += 1

    return (a + b) / 2

def func(x):
    return x**2 - 4

root = bisection_method(func, 0, 3)
print(f"Approximate root: {root}")
