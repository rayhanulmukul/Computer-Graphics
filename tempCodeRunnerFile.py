# For comparison: ideal circle
    theta = [t for t in range(361)]
    x_ideal = [xc + r * plt.np.cos(t*3.14/180) for t in theta]
    y_ideal = [yc + r * plt.np.sin(t*3.14/180) for t in theta]
    plt.plot(x_ideal, y_ideal, 'b--', linewidth=1, label="Ideal Circle")