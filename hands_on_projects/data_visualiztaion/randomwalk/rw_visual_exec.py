import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # create a RandomWalk instanc and draw all the points
    rw = RandomWalk(5000)
    rw.fill_walk()

    # # set window size, the tuple's unit is inch
    # plt.figure(figsize=(10, 8))

    # point_numbers = list(range(rw.num_points))
    # plt.scatter(rw.x_values, rw.y_values,
    #             c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)

    # # show the starting and ending points
    # plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    # plt.scatter(rw.x_values[-1], rw.y_values[-1],
    #             c='red', edgecolors='none', s=100)

    # # hide axis
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)

    plt.plot(rw.x_values, rw.y_values, linewidth=3, )

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
