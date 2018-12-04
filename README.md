# Tarjan and Trojanowski's algorithm
This consists of an implementation of the famous Tarjan and Torjanowski's algorithm that finds the maximum set in a graph in <a href="https://www.codecogs.com/eqnedit.php?latex=O(2^{\frac{|V|}{3}})" target="_blank"><img src="https://latex.codecogs.com/svg.latex?O(2^{\frac{|V|}{3}})" title="O(2^{\frac{|V|}{3}})" /></a>
.
It also consists of a function that compares the runtime of this algorithm with the naive approach at finding maximum cliques.
## Requirements
* Python 3

## Usage
If it is your first time using this program, add the src folder to your PYTHONPATH enviroment variable. If you use Linux or MacOS this can be done by frist running `sh setup.sh` and then restarting your terminal.

To create a benchmark .txt file run `python3 benchmark.py`.

You may change the default behavior of the benchmark program. To do so run `python3 benchmark.py --help` to read about the possible commands.

This is still work in progress so you may get an error when running the benchmark script, if that were to occur simply re-run the script until you get no errors.

## FAQ
**Q:** Where can I find the pseudo code for this algorithm?

**A:** [Here.](http://i.stanford.edu/pub/cstr/reports/cs/tr/76/550/CS-TR-76-550.pdf) Page seven.

**Q:** Why is the set of edges defined as a list?

**A:** Because sets are not hashable, therefore they cannot contain sets which is a problem because every edge is a set.

**Q:** ... Then why are they not defined as frozensets of sets?

**A:** To keep things simple.

**Q:** Would it not make more sense to define graphs as a dictionaries (vertices->edges)?

**A:** Yes and no, that has it's drawbacks too. It would make some tasks easier and some harder.
