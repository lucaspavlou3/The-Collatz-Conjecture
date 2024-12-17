## Alternative Collatz: 3n - 1 ##

from matplotlib import pyplot as plt

# define the collatz conjecture: 3n - 1
integers = []
blue_group = {}
red_group = {}


# collatz except (-1) - does the value return to the original?
for n in range(1, 1000001):
    integers.append(n)
    iterations = 0
    n_collatz_list = []
    original_value = n

    while True:
        if n == 1:
            blue_group[original_value] = iterations
            break
        elif n % 2 == 0:
            n = n/2
        else:
            n = (3 * n) - 1
        
        if n in n_collatz_list:
            red_group[original_value] = iterations
            break
        n_collatz_list.append(n)

        iterations += 1


# split blue and red group dictionaries into key and value lists
blue_integers = list(blue_group.keys())
blue_path_lengths = list(blue_group.values())

red_integers = list(red_group.keys())
red_path_lengths = list(red_group.values())


if __name__ == "__main__":
    # plot collatz list for blue_group and red_group
    plt.scatter(blue_integers, blue_path_lengths, color="#247BA0", label="Path goes to 1", s=0.5)
    plt.scatter(red_integers, red_path_lengths, color="#FF3F00", label="Path loops", s=0.5)
    
    # axis and title labels
    plt.xlabel("n (Starting Number)")
    plt.ylabel("Path Length")
    plt.title("Modified Collatz Path Length Distribution (3n - 1)")
    
    # display figure legend and gridlines
    plt.legend(fontsize=10, loc="upper left")
    plt.grid()

    # plot the graph
    plt.show()
