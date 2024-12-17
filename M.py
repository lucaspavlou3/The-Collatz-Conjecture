## Collatz Multiplicities ##

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
            n = n / 2
        else:
            n = (3 * n) + 1
        iterations += 1

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
    plt.scatter(path_length, multiplicity, color="#247BA0", label="Multiplicity (Frequency)", s=3)
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
    plt.title("Multiplicity Duration of Collatz Path Lengths (Scatter Plot)")

    # display figure legend and gridlines
    plt.legend(fontsize=10, loc="upper right")
    plt.grid()

    # plot the graph
    plt.show()
