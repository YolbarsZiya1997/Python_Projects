import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk(5_000)
rw.fill_walk()

# Plot the points in the walk.
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15, 9))
ax.plot(rw.x_values, rw.y_values, linewidth=2)

ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

plt.savefig('molecular_motion.png', bbox_inches='tight', dpi=1080)
plt.show()