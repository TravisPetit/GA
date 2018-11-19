# Tarjan and Trojanowski's algorithm
This consists of an implementation of the famous Tarjan and Torjanowski's algorithm that finds the maximum set in a graph in O(2^(n/3)).
It also consists of a function that compares the runtime of this algorithm with the naive approach at finding maximum cliques.

## Requirements
Python 3

## Dependencies
* Itertools (I believe this is part of the standart library in python 3+)

## Usage
...

## FAQ
**Q:** Where can I find the pseudo code for this algorithm?

**A:** [Here.](http://i.stanford.edu/pub/cstr/reports/cs/tr/76/550/CS-TR-76-550.pdf)

**Q:** Why is the set of edges defined as a list?

**A:** Because sets are not hashable, therefore they cannot contain sets which is a problem because every edge is a set.

**Q:** ... Then why are they not defined as frozensets of sets?

**A:** To keep things simple.

**Q:** Would it not make more sense to define graphs as a dictionaries (vertices->edges)?

**A:** Yes and no, that has it's drawbacks too. It would make some tasks easier and some harder.
