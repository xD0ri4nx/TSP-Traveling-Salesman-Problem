# Travelling Salesman Problem Solver

This Python script provides a solution to the Travelling Salesman Problem (TSP) using three different algorithms:

1. Depth-First Search (DFS)
2. Uniform Cost Search (UCS)
3. A* Search

## Requirements

- Python 3.x

## Usage

1. Ensure you have Python installed on your system.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using the following command:

   ```bash
   python tsp_solver.py
   ```

4. The script will output the best cost and path found by each algorithm.

## Description

- The script defines a class `TSP` that takes a list of distances between cities as input.
- It provides methods to solve the TSP using DFS, UCS, and A* algorithms.
- Each algorithm is implemented as a method within the class.
- The `solve` method is used to run each algorithm and print the best cost and path.

## Example

Given the following distances between cities:

```
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
```

Running the script will output:

```
Solving with DFS...
DFS Best Cost: 80, Path: [0, 1, 2, 3, 0]
Solving with UCS...
UCS Best Cost: 80, Path: [0, 1, 2, 3, 0]
Solving with A*...
A* Best Cost: 80, Path: [0, 1, 2, 3, 0]
```
