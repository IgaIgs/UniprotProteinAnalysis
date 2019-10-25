import matplotlib.pyplot as plt


def plot_bar_show(d):
    """Prepare a bar graph template.

    :param d: Records in analysed file.
    :return: Show the bar graph.
    """
    # A list of numbers as long as the elements in d
    r = range(0, len(d))
    # Prepare a figure
    plt.figure()

    # Add bars, one at each x position, with the values of d
    plt.bar(r, d.values())
    # Add labels to the x-axis, with the keys of d and print the labels vertically
    plt.xticks(r, d.keys(), rotation=90)
    # Squash everything up so there is no white space
    plt.tight_layout()
    # Show the graph
    plt.show()


def plot_pie_show(d):
    """Prepare a pie chart template.

    :param d: Records in analysed file.
    :return: A pie chart.
    """
    # A list of numbers as long as the elements in d
    r = range(0, len(d))
    # Prepare a figure

    sizes = d.values()
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=d.keys(), autopct='%1.1f%%', startangle=90, rotatelabels=270)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()
