import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    """Return list of points on a line from (x1,y1) to (x2,y2) using Bresenham's algorithm."""
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        points.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
    return points

def plot_line(points, x1, y1, x2, y2):
    """Plot line using computed points from Bresenham algorithm."""
    xs, ys = zip(*points)
    plt.figure(figsize=(6,6))
    plt.scatter(xs, ys, c='red', s=60, marker='s', label="Bresenham Pixels")
    plt.plot([x1, x2], [y1, y2], 'b--', linewidth=1, label="Ideal Line")
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("Bresenham Line Drawing Algorithm")
    plt.grid(True, which='both', linestyle=":")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Example line
    x1, y1 = 2, 2
    x2, y2 = 15, 8

    points = bresenham_line(x1, y1, x2, y2)
    print("Generated points:", points)
    plot_line(points, x1, y1, x2, y2)
