import matplotlib.pyplot as plt

def bresenham_circle(xc, yc, r):
    """Return list of points on a circle centered at (xc, yc) with radius r."""
    x = 0
    y = r
    d = 3 - 2 * r
    points = []

    while y >= x:
        # 8-way symmetry
        points.extend([
            (xc + x, yc + y), (xc - x, yc + y),
            (xc + x, yc - y), (xc - x, yc - y),
            (xc + y, yc + x), (xc - y, yc + x),
            (xc + y, yc - x), (xc - y, yc - x)
        ])
        if d < 0:
            d = d + 4*x + 6
        else:
            d = d + 4*(x - y) + 10
            y -= 1
        x += 1
    return points

def plot_circle(points, xc, yc, r):
    xs, ys = zip(*points)
    plt.figure(figsize=(6,6))
    plt.scatter(xs, ys, c='red', s=50, marker='s', label="Bresenham Pixels")

    # For comparison: ideal circle
    theta = [t for t in range(361)]
    x_ideal = [xc + r * plt.np.cos(t*3.14/180) for t in theta]
    y_ideal = [yc + r * plt.np.sin(t*3.14/180) for t in theta]
    plt.plot(x_ideal, y_ideal, 'b--', linewidth=1, label="Ideal Circle")

    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("Bresenham Circle Drawing Algorithm")
    plt.grid(True, linestyle=":")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    xc, yc = 10, 10   # center
    r = 8             # radius
    points = bresenham_circle(xc, yc, r)
    print("Generated points:", points)
    plot_circle(points, xc, yc, r)
