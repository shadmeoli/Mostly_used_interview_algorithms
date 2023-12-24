# Interview question with solutions

Welcome to the Algorithms and Programming Problems Repository! This repository is organized to facilitate learning and practice of algorithms and programming problems in various languages including TypeScript, JavaScript, Go, and Python. Below is an in-depth guide to the structure of this repository:
Most of the questions are from coding interviwes and codewars while some are from leetcode

## Author 
[@shadmeoli](https://www.github.com/shadmeoli)

## Appendix

Any additional information goes here

Most of the questions are based on 1D-arrays & 2D-arrays and some need use of hash maps | dictionaries | sets | heap

## Folder Structure:

```
.
├── go-lang
│   ├── algos               # Contains Go language implementations of algorithms
│   │   └── algos.go        # File with Go implementations of algorithms
│   ├── go.mod              # Go module file for managing dependencies
│   ├── main.go             # Main Go program file for executing code
│   └── problems            # Directory for Go language programming problems
├── python
│   ├── algos               # Contains Python implementations of algorithms
│   │   └── DS_and_algotithims.py  # File with Python implementations of algorithms
│   └── problems            # Directory for Python programming problems
│       ├── gameoflife.py   # Python code for Conway's Game of Life problem
│       └── panag.py        # Python code for checking if a string is a panagram
├── ts-js
│   ├── algos               # Contains TypeScript/Javascript implementations of algorithms
│   │   ├── binary_search.ts        # TypeScript/Javascript code for binary search algorithm
│   │   ├── bubbleSort.ts           # TypeScript/Javascript code for bubble sort algorithm
│   │   ├── dsa_with_ts.ts          # TypeScript/Javascript code for data structures and algorithms
│   │   ├── finding_nines.ts        # TypeScript/Javascript code for finding nines problem
│   │   └── panagram.ts             # TypeScript/Javascript code for checking if a string is a panagram
│   ├── index.ts            # Main TypeScript file for executing code
│   ├── node_modules        # Node.js modules folder for managing dependencies
│   ├── package.json        # Node.js package file for managing project metadata and dependencies
│   ├── pnpm-lock.yaml      # pnpm package lock file for dependency management
│   ├── problems            # Directory for TypeScript/Javascript programming problems
│   │   ├── mocking-spinner.ts      # TypeScript/Javascript code for mocking spinner problem
│   │   └── noisefunction.ts        # TypeScript/Javascript code for noise function problem
│   └── tsconfig.json       # TypeScript configuration file for configuring TypeScript compiler options
├── README.md               # Repository Readme file containing documentation and information about the repository
└── .gitignore              # Git ignore file for specifying intentionally untracked files to ignore
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
