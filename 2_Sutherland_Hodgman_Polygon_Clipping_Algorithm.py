import matplotlib.pyplot as plt

x_min, y_min, x_max, y_max = 120, 100, 500, 350
EDGES = ("LEFT", "RIGHT", "BOTTOM", "TOP")

def inside(p, edge):
    x, y = p
    if edge == "LEFT":   return x >= x_min
    if edge == "RIGHT":  return x <= x_max
    if edge == "BOTTOM": return y >= y_min
    if edge == "TOP":    return y <= y_max
    return True

def intersect(p1, p2, edge):
    x1, y1 = p1
    x2, y2 = p2

    if x1 == x2:
        m = None
    else:
        m = (y2 - y1) / (x2 - x1)
    
    if edge == "LEFT":
        x, y = x_min, y1 + (x_min - x1) * m
    elif edge == "RIGHT":
        x, y = x_max, y1 + (x_max - x1) * m
    elif edge == "BOTTOM":
        if m is None:
            return None
        x, y = x1 + (y_min - y1) / m, y_min
    elif edge == "TOP":
        if m is None:
            return None
        x, y = x1 + (y_max - y1) / m, y_max
    return (x, y)

def clip_polygon(polygon, edge):
    clipped = []
    n = len(polygon)
    for i in range(n):
        curr = polygon[i]
        prev = polygon[i - 1]

        if inside(curr, edge):
            if not inside(prev, edge):
                inter = intersect(prev, curr, edge)
                if inter:
                    clipped.append(inter)
            clipped.append(curr)
        elif inside(prev, edge):
            inter = intersect(prev, curr, edge)
            if inter:
                clipped.append(inter)
    return clipped

def sutherland_hodgman(polygon):
    for edge in EDGES:
        polygon = clip_polygon(polygon, edge)
    return polygon

def main():
    # Examle polygon
    polygon = [(100, 150), (200, 50), (300, 150), (350, 250), (300, 350), (200, 350), (150, 250)]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    ax1.set_facecolor("white")
    ax2.set_facecolor("white")

    # Draw original polygon
    xs, ys = zip(*polygon)
    ax1.fill(xs, ys, facecolor="lightcoral", alpha=0.7, edgecolor="darkred", linewidth=2)
    rect_x = [x_min, x_max, x_max, x_min, x_min]
    rect_y = [y_min, y_min, y_max, y_max, y_min]
    ax1.plot(rect_x, rect_y, color="blue", linewidth=2, label="Clip window")
    ax1.set_title("Original Polygon")
    ax1.set_xlim(50, 600)
    ax1.set_ylim(50, 400)
    ax1.set_aspect("equal")
    ax1.grid(True, alpha=0.3)


    # Draw clipped polygon
    clipped = sutherland_hodgman(polygon)
    if clipped:
        xs, ys = zip(*clipped)
        ax2.fill(xs, ys, facecolor="lightgreen", alpha=0.7, edgecolor="darkgreen", linewidth=2)
    ax2.plot(rect_x, rect_y, color="blue", linewidth=2, label="Clip window")
    ax2.set_title("Clipped Polygon")
    ax2.set_xlim(50, 600)
    ax2.set_ylim(50, 400)
    ax2.set_aspect("equal")
    ax2.grid(True, alpha=0.3)

    plt.suptitle("Sutherland-Hodgman Polygon Clipping Algorithm", fontsize=16)
    plt.show()

if __name__ == "__main__":
    main()