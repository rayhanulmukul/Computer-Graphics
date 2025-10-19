import matplotlib.pyplot as plt

# Define clipping rectangle boundaries
x_left, x_right, y_bottom, y_top = 120, 500, 100, 350

# Region codes
INSIDE, LEFT, RIGHT, BOTTOM, TOP = 0, 1, 2, 4, 8

def region_code(x, y):
    code = INSIDE
    if x < x_left:  code |= LEFT
    elif x > x_right: code |= RIGHT
    if y < y_bottom: code |= BOTTOM
    elif y > y_top: code |= TOP
    return code

def cohen_sutherland(x1, y1, x2, y2, ax):
    code1 = region_code(x1, y1)
    code2 = region_code(x2, y2)

    while True:
        if not (code1 | code2):
            # Both points inside
            ax.plot([x1, x2], [y1, y2], color="black", linewidth=2)
            break
        elif code1 & code2:
            # Both points outside
            break
        else:
            x, y = 0, 0
            code_out = code1 if code1 else code2

            if code_out & TOP:
                x = x1 + (x2 - x1) * (y_top - y1) / (y2 - y1)
                y = y_top
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (y_bottom - y1) / (y2 - y1)
                y = y_bottom
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (x_right - x1) / (x2 - x1)
                x = x_right
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (x_left - x1) / (x2 - x1)
                x = x_left
            if code_out == code1:
                x1, y1 = x, y
                code1 = region_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = region_code(x2, y2)


def main():
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_facecolor('white')

    # Draw clipping rectangle (orange)
    rect_x = [x_left, x_right, x_right, x_left, x_left]
    rect_y = [y_bottom, y_bottom, y_top, y_top, y_bottom]
    ax.plot(rect_x, rect_y, color='orange', linewidth=2, label='Clipping Rectangle')

    # Draw original line
    x1, y1, x2, y2 = 50, 200, 500, 400
    ax.plot([x1, x2], [y1, y2], color='red', linestyle='--', alpha=0.5, label='Original Line')

    # Draw clipped line
    cohen_sutherland(x1, y1, x2, y2, ax)

    ax.set_xlim(0, 600)
    ax.set_ylim(0, 500)
    # ax.set_aspect('equal', adjustable='box')
    ax.set_title('Cohen-Sutherland Line Clipping Algorithm', fontsize=16)
    ax.set_xlabel('X-axis', fontsize=14)
    ax.set_ylabel('Y-axis', fontsize=14)
    # plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()