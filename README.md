# Tarjan and Trojanowski's algorithm
This is an implementation of the Tarjan and Torjanowski's algorithm that finds maximum independent sets in <a href="https://www.codecogs.com/eqnedit.php?latex=O(2^{\frac{|V|}{3}})" target="_blank"><img src="https://latex.codecogs.com/svg.latex?O(2^{\frac{|V|}{3}})" title="O(2^{\frac{|V|}{3}})" /></a>
 set up in way such that it finds the cardinality of the maximum clique for a given graph.
It also consists of a script that compares the runtime of this algorithm with the naive approach at finding maximum cliques.
## Requirements
* Python 3

## Usage
If it is your first time using this program, add the src folder to your PYTHONPATH enviroment variable. If you use Linux or MacOS you can do this by running `sh setup.sh` and then restarting your terminal.

To create a benchmark .txt file run `python3 benchmark.py`.

You may change the default behavior of the benchmark script. To do so run `python3 benchmark.py --help` to read about the possible commands.

## FAQ
**Q:** Where can I find the pseudo code for this algorithm?

**A:** [Here.](http://i.stanford.edu/pub/cstr/reports/cs/tr/76/550/CS-TR-76-550.pdf) Page seven.

**Q:** Why is the set of edges defined as a list?

**A:** Because sets are not hashable, therefore they cannot contain sets which is a problem because every edge is a set.

**Q:** ... Then why are they not defined as frozensets of sets?

**A:** To keep things simple.

**Q:** Would it not make more sense to define graphs as a dictionaries (vertices->edges)?

**A:** Yes and no, that has it's drawbacks too. It would make some tasks easier and some harder.

## Notes
Due to time constraints, I was no able to implement the the following statements:
* 3.3.1
* 3.4.3.3
* 3.4.3.4.*
* 4.1.*

For such cases I have tweaked the program such that it uses the naive approach at finding maximum independent sets.

The main algorithm is also not bug-free. From my expereince it works about 90 to 95% of times.
Due to time constraints I was not able to fully debug it. I suspect the error lies somewhere deep into statement 3.
