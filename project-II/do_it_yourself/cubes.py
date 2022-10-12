import matplotlib.pyplot as plt

values_1 = [1, 2, 3, 4, 5]
cubes_1 = [x**3 for x in values_1]

fig_1, ax = plt.subplots()
ax.scatter(values_1, cubes_1, s=10)

# Set chart title and label axis
ax.set_title('Cube Numbers', fontsize=20)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube of Value', fontsize=14)

# Size of the tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()

values_2 = range(1, 5001)
cubes_2 = [x**3 for x in values_2]

fig_2, ay = plt.subplots()
ay.scatter(values_2, cubes_2, c=cubes_2, cmap=plt.cm.Blues, s=10)

# Set chart title and label axis
ay.set_title('Cube Numbers(5000)', fontsize=20)
ay.set_xlabel('Value', fontsize=14)
ay.set_ylabel('Cube of Value', fontsize=14)

# Size of the tick labels
ay.tick_params(axis='both', labelsize=14)
ay.axis([0, 5000, 0, 125000000000])

plt.show()