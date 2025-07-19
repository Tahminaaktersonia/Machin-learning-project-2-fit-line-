import matplotlib.pyplot as plt
import numpy as np

def my_linfit(x, y):
    N = len(x)  # Number of data points
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x_squared = np.sum(x ** 2)

    a = (N * sum_xy - sum_x * sum_y) / (N * sum_x_squared - sum_x ** 2)
    b = (sum_y * sum_x_squared - sum_x * sum_xy) / (N * sum_x_squared - sum_x ** 2)

    return a, b

# Function to collect points
def on_click(event, x_list, y_list):
    if event.button == 1:  # Left click to add point
        x_list.append(event.xdata)
        y_list.append(event.ydata)
        plt.plot(event.xdata, event.ydata, 'kx')
        plt.draw()
    elif event.button == 3:  # Right click to stop collecting
        plt.close()


# Main
x = []
y = []

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Left click to add points, right click to finish')
fig.canvas.mpl_connect('button_press_event', lambda event: on_click(event, x, y))
plt.show()

# Convert to numpy arrays
x = np.array(x)
y = np.array(y)

# Fit the line using collected points
if len(x) > 1:
    a, b = my_linfit(x, y)

    # Plot the original points
    plt.plot(x, y, 'kx')

    # Plot the fitted line
    xp = np.arange(min(x) - 1, max(x) + 1, 0.1)
    plt.plot(xp, a * xp + b, 'r-')

    print(f"My fit: a={a} and b={b}")
    plt.show()
else:
    print("Not enough points to fit a line.")
