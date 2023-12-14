# Exercise 3: Line graph ☑️
# Draw a line in a diagram from position (1, 2) to position (6, 8)
# Draw a dotted line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10)


import matplotlib.pyplot as plt

# Draw a line from position (1, 2) to (6, 8)
x = [1, 6]
y = [2, 8]

# Draw a dotted line from position (1, 3) to (2, 8) to (6, 1) to (8, 10)
x_dot = [1, 2, 6, 8]
y_dot = [3, 8, 1, 10]

# Plotting the line
plt.plot(x, y, label='Solid Line')

# Plotting the line but with dot style
plt.plot(x_dot, y_dot, '--', label='Dotted Line')

# headings. 2 labels and a title
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Line and Dotted Line')
# displaying the labels with legend
plt.legend()

# Display the plot
plt.show()