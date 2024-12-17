# The Collatz Conjecture

The **Collatz Conjecture** is a deceptively simple mathematical theorem. Initially, a number (n) is chosen and an iterative algorithm is applied. Where n is even, it is divided by 2 and where n is odd, it is multiplied by 3 and added to 1. The Conjecture itself asks whether or not **all numbers** will ultimately return to 1 after some number of iterations. So far, all numbers tested have returned to 1 but this is not proven for all n.

This repository contains an algorithm that computes the Collatz Conjecture, along with a closely-related variation. Sequence lengths of n are plotted graphically using Matplotlib.  

![Steps of The Collatz Conjecture visualised in a circle, with all values leading to 1, in the centre of the circle](https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Collatz-graph-20-iterations.svg/1228px-Collatz-graph-20-iterations.svg.png?20100525100020)

## How it works

Within this repository, there are four individual Python3 scripts - ```L.py```, ```M.py``` and ```N.py```. Each script contains the algorithm for the Collatz conjecture and/or some closely-related variation. Each algorithm is tested for ```1 < n < 1,000,000``` and a sequence is built. The output sequence of each algorithm is then plotted graphically using Matplotlib.

1. ```L.py``` contains the standard Collatz conjecture, using ```3n + 1```.

2. ```M.py``` also uses ```3n + 1```, but instead plots the *multiplicity* of each sequence length. This is the number of times that each sequence length appears.
  
3. ```N.py``` uses a variation of the Collatz Conjecture. Where n is odd, it is now mutliplied by 3 before 1 is *taken away*. This is described algebraically as ```3n - 1```. Numbers that return to 1 are plotted in blue. Any n that *cannot* return to 1 using this algorithm (and instead **loops**) appears in red.

4. ```P.py``` plots both the standard (```3n + 1```) and alternative (```3n - 1```) Collatz Conjecture sequences on a single graph. For each odd n in ```1 < n < 1,000,000```, the probability of using ```3n + 1``` is given by ```p``` and the probability of using ```3n - 1``` is given by ```1 - p```. The ```p-value``` is programmed to be variable.

## Note

These scripts could have been written using imported functions. However, I chose to re-write them in each script where necessary so that scripts can be downloaded and run independently. 
