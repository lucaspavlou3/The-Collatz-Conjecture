## Collatz Conjecture ##

from matplotlib import pyplot as plt
from statistics import mean, stdev


# define the collatz conjecture: 3n + 1
integers = []
path_lengths = []
    
for n in range(1, 1000001):
    integers.append(n)
    iterations = 0
    
    while n >= 1:
        if n == 1:
            path_lengths.append(iterations)
            break
        elif n % 2 == 0:
            n = n/2
        else:
            n = (3 * n) + 1
        iterations += 1

if __name__ == '__main__':
    # find the mean and sd of the collatz list
    collatz_mean = round(mean(path_lengths), 2)
    collatz_sd = stdev(path_lengths)

    # define upper and lower standard devs
    upper_sd = round(collatz_mean + collatz_sd, 2)
    lower_sd = round(collatz_mean - collatz_sd, 2)

    # plot collatz list, with mean and standard devs
    plt.scatter(integers, path_lengths, color = '#247BA0', s = 0.5)
    mean_line = plt.axhline(y = collatz_mean, color = '#FF3F00', label = f'Mean: {collatz_mean}')
    upper_sd_line = plt.axhline(y = upper_sd, color = '#FF7F11', linestyle = 'dotted', label = f'+1 Std Dev: {upper_sd}')
    lower_sd_line = plt.axhline(y = lower_sd, color = '#FF7F11', linestyle = 'dotted', label = f'-1 Std Dev: {lower_sd}')

    # axis and title labels
    plt.xlabel("integer n")
    plt.ylabel("Path Length")
    plt.title("Collatz Path Lengths for Integers from Considered Range")

    # display figure legend and gridlines
    plt.legend(fontsize=10, loc="upper left")
    plt.grid()

    # plot the graph
    plt.show()
