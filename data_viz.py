import sys
import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')


def boxplot(L, plot_title, out_file_name):
    '''This function makes a boxplot of the data, L, and saves the image to
    the name passed in out_file_name
    This method takes three arguments:
    - L is an array of input data that can be any number of columns (int)
    - plot_title is the title that will centered over the plot (str)
    - out_file_name is the name of the plot you would like to save (str)'''

    width = 3
    height = 3
    fig = plt.figure(figsize=(width, height), dpi=300)
    ax = fig.add_subplot(1, 1, 1)
    ax.boxplot(L)
    plt.title(plot_title, loc='center')
    plt.xlabel("Sample Name")
    plt.ylabel("Gene read counts")
    plt.savefig(out_file_name, bbox_inches='tight')


# def main():
    # fake_data = np.random.randint(1000, size=(20, 4))
    # boxplot(fake_data, "MAPT", "test_file_name.png")

if __name__ == '__main__':
    main()
