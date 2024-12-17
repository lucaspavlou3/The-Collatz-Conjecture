## Probabilistic Collatz - (3n + 1) or (3n - 1) ##

from matplotlib import pyplot as plt
from statistics import mean, stdev
from random import random

def pos_collatz(n):
    iterations = 0
    
    while n != 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = (3 * n) + 1
        iterations += 1
    return iterations

def neg_collatz(n):
    iterations = 0
    n_collatz_list = []  # all numbers that have been visited in 3n-1 for each n
    
    while True:
        if n % 2 == 0:
            n = n//2
        else:
            n = (3 * n) - 1
        
        if n in n_collatz_list:
            break
        
        n_collatz_list.append(n)
        iterations += 1
    return iterations

# define the collatz conjecture: 3n + 1
integers = []
path_lengths = []

for n in range(1, 1000001):
    p = random()
    integers.append(n)
    
    if n == 1:
        path_lengths.append(0)
        
    else:
        if p > 0.5:
            pos = pos_collatz(n)
            path_lengths.append(pos)
        else:
            neg = neg_collatz(n)
            path_lengths.append(neg)


collatz_dict = {i: 0 for i in path_lengths}

for key, value in collatz_dict.items():
    collatz_dict[key] = path_lengths.count(key)

path_length = list(collatz_dict.keys())
multiplicity = list(collatz_dict.values())


if __name__ == "__main__":
    # find the mean and sd of the collatz list
    multis_mean = round(mean(path_lengths), 2)
    multis_sd = stdev(path_lengths)

    # define upper and lower standard devs
    upper_sd = round(multis_mean + multis_sd, 2)
    lower_sd = round(multis_mean - multis_sd, 2)

    # plot collatz list, with mean and standard devs
    plt.scatter(path_length, multiplicity, color="#247BA0", s=3)
    mean_line = plt.axvline(
        x=multis_mean, color="#FF3F00", label=f"Mean: {multis_mean}"
    )
    upper_sd_line = plt.axvline(
        x=upper_sd, color="#FF7F11", linestyle="dotted", label=f"+1 Std Dev: {upper_sd}"
    )
    lower_sd_line = plt.axvline(
        x=lower_sd, color="#FF7F11", linestyle="dotted", label=f"-1 Std Dev: {lower_sd}"
    )

    # axis and title labels
    plt.xlabel("Collatz Path Length")
    plt.ylabel("Multiplicity (Frequency)")
    plt.title("Distribution of Path Lengths in Probabilistic Collatz Conjecture")

    # display figure legend and gridlines
    plt.legend(fontsize=10, loc="upper right")
    plt.grid()

    # plot the graph
    plt.show()
