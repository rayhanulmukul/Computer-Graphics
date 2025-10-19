import matplotlib.pyplot as plt

def compute_point(u, controls):
    from math import comb  # For binomial coefficients (nCk)
    n = len(controls) - 1
    x, y = 0.0, 0.0
    for k in range(n + 1):
        blend = comb(n, k) * (u ** k) * ((1 - u) ** (n - k))
        x += controls[k][0] * blend
        y += controls[k][1] * blend
    return (x, y)

def bezier(controls, steps=100):
    curve = []
    for i in range(steps + 1):
        u = i / steps
        curve.append(compute_point(u, controls))
    return curve

controls = [(10, 10), (20, 100), (80, 100), (90, 10)]  # Change as needed
curve = bezier(controls, steps=200)

curve_x, curve_y = zip(*curve)
ctrl_x, ctrl_y = zip(*controls)

plt.figure(figsize=(6, 6))
plt.plot(ctrl_x, ctrl_y, 'bo--', label="Control Polygon")  # Control polygon
plt.plot(curve_x, curve_y, 'r-', linewidth=2, label="Bezier Curve")  # Curve
plt.legend()
plt.title("Bezier Curve (Cohen’s Algorithm in Python)")
plt.grid(True)
plt.show()