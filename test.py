import matplotlib.pyplot as plt

# Read inputs
n = int(input())                    # number of vertices
pts = [tuple(map(int, input().split())) for _ in range(n)]
tx, ty = map(int, input().split())  # translation (tx, ty)

# Split into x,y for plotting
x, y = zip(*pts)
x2 = [xi + tx for xi in x]
y2 = [yi + ty for yi in y]

plt.figure(figsize=(7, 6))
ax = plt.gca()
ax.set_facecolor("white")
ax.invert_yaxis()                   # mimic graphics.h (optional)

# Draw original (black) and translated (red)
plt.plot(list(x)+[x[0]], list(y)+[y[0]], "k-", linewidth=2, label="Before")
plt.plot(x2+[x2[0]], y2+[y2[0]], "r-", linewidth=2, label="After")

plt.axis("equal")
plt.grid(True, alpha=0.3)
plt.legend()
plt.title("2D Polygon Translation")
plt.show()
