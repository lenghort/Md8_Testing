def bisection_method(f, a, b, tolerance=1e-6, max_iterations=100):
    if f(a) * f(b) >= 0:
        return None

    iteration = 0
    while (b - a) / 2 > tolerance and iteration < max_iterations:
        m = (a + b) / 2
        fm = f(m)

        if fm == 0 or (b - a) / 2 < tolerance:
            return m

        if f(a) * fm < 0:
            b = m
        else:
            a = m

        iteration += 1

    return (a + b) / 2


def find_all_roots(f, start, end, step=0.5, tolerance=1e-6):
    roots = []
    a = start

    while a < end:
        b = a + step
        root = bisection_method(f, a, b, tolerance)
        if root is not None:
            if not any(abs(root - r) < tolerance for r in roots):
                roots.append(root)
        a = b

    return roots

def func(x):
    return x**4 + 3*x**3 + x**2 - 2*x - 0.5

roots = find_all_roots(func, -10, 10)

print(f"Approximate roots: {roots}")
