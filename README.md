<div align="center">
  <a href="http://aima.cs.berkeley.edu/"><img src="https://raw.githubusercontent.com/aimacode/aima-python/master/images/aima_logo.png"></a><br><br>
</div>


Based on the book *[Artificial Intelligence: A Modern Approach](http://aima.cs.berkeley.edu),* and python repository provided.

## Structure of the Project

  -  [main.py](./main.py) - main file to be run from command prompt

  -  [QueensEnv](./Environment.py)(ironment):
      -  [Table](./Table.py) - wrapper class to hold agent, it's board and performance measure
      -  [Statistics Module](./Stats.py) - gathers all statistical information about current run
      -  [Agents](./Agents.py) - contains definitions of generator objects. Those are function-like creatures which remember their internal state and return a new value
      every time .send() is called. Initialisation is done with .send(None), in this case used to print agent's name.
      This structure is meant to represent functional nature of agent, as proposed in the book/original repo. May be changed as desired.
      -  [Utility Measures](./utility_measures.py) - implementation of utility function used by all agents so far, i.e. the number of
      pairs which check each other.

## Encoding system and plotting

A board with 8 queens on it is encoded by their y coordinates, assuming there is exactly one queen in each column. Simple plot utility plot_board(<int array>)
is provided in [StatsModule.py](./StatsModule.py). For example, board encoded as
\[0,1,2,3,4,5,7,7\] will render to:

![sample_board.png][./sample_board.png]

## Python 3.4 and up

This code requires Python 3.4 or later, and does not run in Python 2. You can [install Python](https://www.python.org/downloads) or use a browser-based Python interpreter such as [repl.it](https://repl.it/languages/python3).
You can run the code in an IDE, or from the command line with `python -i filename.py` where the `-i` option puts you in an interactive loop where you can run Python functions. See [jupyter.org](http://jupyter.org/) for instructions on setting up your own Jupyter notebook environment, or run the notebooks online with [try.jupiter.org](https://try.jupyter.org/). 

