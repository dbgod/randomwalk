import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make random walks until user quits.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_valies, s=15)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
