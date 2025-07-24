# Interview question with solutions

Welcome to the Algorithms and Programming Problems Repository! This repository is organized to facilitate learning and practice of algorithms and programming problems in various languages including TypeScript, JavaScript, Go, and Python. Below is an in-depth guide to the structure of this repository:
Most of the questions are from coding interviwes and codewars while some are from leetcode

## Author 
[@shadmeoli](https://www.github.com/shadmeoli)


---

#### Python Testing Update

> 📣 **New Test Runner Available!**  
> We've added a unified and elegant way to test Python solutions with colored CLI output, spinners, and summaries using a custom decorator.

Activate your Poetry environment:

```sh
poetry env activate $(poetry env info --path)
````

[Jump to testing usage guide](#python-test-runner-usage)

---


##Appendix


Most of the questions are based on 1D-arrays & 2D-arrays and some need use of hash maps | dictionaries | sets | heap

## Folder Structure:

```

cpp
└── main.cpp
go
├── algos
│   └── bubbleSort.go
├── go.mod
├── main.go
└── problems
    └── perms.go
java
├── KnightMoves.java
└── main.java
poetry.lock
pyproject.toml
pyru.sh
python
├── algos
│   ├── dijkstra.py
│   └── DS_and_algotithims.py
├── Concepts
│   └── OOP_Concepts.py
├── problems
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-313.pyc
│   │   ├── find_peaks.cpython-313.pyc
│   │   ├── reverse_words.cpython-313.pyc
│   │   └── traversing_arrays.cpython-313.pyc
│   ├── chessMovesCalc.py
│   ├── duplicates.py
│   ├── dynamic_programming_problems.py
│   ├── find_peaks.py
│   ├── gameoflife.py
│   ├── panag.py
│   ├── permuation.py
│   ├── reverse_words.py
│   ├── stars.py
│   └── traversing_arrays.py
└── tester
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-313.pyc
    │   └── testLogger.cpython-313.pyc
    └── testLogger.py
README.md
ts
├── algos
│   ├── binary_search.ts
│   ├── bubbleSort.ts
│   ├── dijkstra.ts
│   ├── dsa_with_ts.ts
│   ├── finding_nines.ts
│   ├── numsum.ts
│   └── panagram.ts
├── bun.lockb
├── index.ts
├── package.json
├── pnpm-lock.yaml
├── problems
│   ├── duplicates.ts
│   ├── majority_element.ts
│   ├── mocking-spinner.ts
│   ├── noisefunction.ts
│   ├── permutations.ts
│   ├── speedDetector.ts
│   └── stars.ts
└── tsconfig.json


```

## Folder Descriptions:

- **go-lang**: This directory contains Go language code. It includes implementations of algorithms and programming problems written in Go.

- **python**: This directory contains Python code. It includes implementations of algorithms and programming problems written in Python.

- **ts-js**: This directory contains TypeScript and JavaScript code. It includes implementations of algorithms and programming problems written in TypeScript and JavaScript.

## File Descriptions:

- **algos.go**: This file contains Go language implementations of various algorithms.

- **DS_and_algotithims.py**: This file contains Python implementations of various algorithms and data structures.

- **index.ts**: This file serves as the main entry point for TypeScript code.

- **package.json**: This file contains metadata about the Node.js project and its dependencies.

- **problems**: This directory contains files with programming problems and their solutions written in various languages.

## Additional Information:

- This repository is designed for educational purposes, to help users learn and practice algorithms and programming problems in different languages.

- Feel free to contribute by adding new algorithms, improving existing ones, or suggesting better solutions to the programming problems.

### Topics to cover in the comming week.

- Permuations and recussion
- Tris.
- Double linked list and its operations

> I am also adding some conepts mostly OOP concepts first with python but late with more OOP centered languages
> like **Java** and **c++**


**From now on most complex OOP concepts I will be implementing them either with c++ of Java**

#### Why Java or C++.
To my preference I believe these are some of the languages tha use deep OOP concepts which are building blocks of how some things work mostly algorithms and data sctructures


#### Concepts to cover:
- [X] Class Methods and instance methods.
- [x] Reference counting



## Codewards Problems
> I am not by any way suggesting my ways are better. These were just my approach to the problem.

#### Shortest Knight Path
Pyhton File: [chessMovesCalc.py](python/problems/chessMovesCalc.py)\
Java File: [KnightMoves.java](__java__/KnightMoves.java)\
Approach: BFS

#### Solution Break down.
1.  **Board Representation**: The first step is to represent the chessboard. We can represent the board as an 8x8 grid, where each cell represents a square on the board. We'll use algebraic notation to label each cell.
    
2.  **Valid Moves**: We need to determine the valid moves a knight can make from a given position. According to the rules of chess, a knight can move in an "L" shape: two squares in one direction (either horizontally or vertically) and then one square perpendicular to that direction. We'll compute all possible valid moves for a given position.
    
3.  **Breadth-First Search (BFS)**: We'll use BFS to search for the shortest path from the starting position to the target position. BFS is well-suited for finding the shortest path in unweighted graphs, which is applicable here since each move has the same weight (1).
    
4.  **Queue for BFS**: We'll use a queue data structure to implement BFS. Starting with the initial position, we'll explore all possible moves from each position until we reach the target position.
    
5.  **Visited Set**: To avoid revisiting the same position and getting stuck in an infinite loop, we'll keep track of visited positions using a set data structure.
    
6.  **Algorithm Execution**: We'll start BFS from the initial position. At each step, we'll dequeue a position from the queue, check if it's the target position, and if not, enqueue all its valid neighboring positions that haven't been visited yet. We'll repeat this process until we find the target position or exhaust all possible moves.
    
7.  **Distance Calculation**: As we explore positions in BFS, we'll keep track of the distance traveled from the initial position to each visited position. Once we find the target position, we'll return the distance traveled as the least number of moves required.
    

### Code Execution:

The implementation consists of defining the `knight` function, which encapsulates the entire solution. Within this function:

*   The chessboard is represented as a grid.
*   BFS is performed using a queue to find the shortest path.
*   Valid moves are computed dynamically for each position.
*   Visited positions are tracked to avoid revisiting.

The function returns the least number of moves required for the knight to reach the target position.

---

### Python Test Runner Usage

Create your testable function normally:

```python
# my_code.py
def find_first_big_number(arr):
    for idx, val in enumerate(arr):
        if val >= 10:
            return idx
    return -1
````

Then, in your test file:

```python
# test_find_big.py
from tester.testLogger import test_runner
from my_code import find_first_big_number

@test_runner
def test_case_1():
    assert find_first_big_number([2, 5, 11, 3]) == 2

@test_runner
def test_case_2():
    assert find_first_big_number([1, 4, 6, 9]) == -1

@test_runner
def test_case_3():
    assert find_first_big_number([10, 20, 30]) == 0
```

> You don't have to separete them you can also have then in the same file here's an example with an in-file setup
```py

from python.tester.testLogger import test_runner


# level 1
def find_first_big_number(arr):
    pass

@test_runner(
    ...<!decorator kwargs>
)
def test_find_first_big_number(arr):
    return find_first_big_number(arr)


# level 2
def count_increasing_pairs(arr):
    pass


@test_runner(
    ...<!decorator kwargs>
)
def test_count_increasing_pairs(arr):
    return count_increasing_pairs(arr)


if __name__ == "__main__":
     test_find_first_big_number()
    test_count_increasing_pairs()

```


Run the file:

```bash
python test_find_big.py
```

> 💡 **Note:**  
For python questions and also the custom test runner decorator I am using [Poetry](https://python-poetry.org/) to manage dependencies and environments.  
If you're contributing or testing locally, make sure to install Poetry and use the configured environment:

```bash
# Install project dependencies
poetry install

# Activate the virtual environment
poetry env activate $(poetry env info --path)

# Run a file
poetry run python python/problems/your_file.py
````

Alternatively, you can use the helper script to quickly run problem files:

#### Example usage
```bash
./run.sh traversing_arrays
```

This will run `python/problems/traversing_arrays.py` using the Poetry environment.


