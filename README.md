# Maze A* Visualization 
Maze Solver is a Python program that allows you to interactively create mazes and find the shortest path from a start point to an end point using various algorithms. I used pygame for the visualization tool. I implmented a DFS algorithm to generate a random maze, and used A* to solve the maze. 

## Installation

1. Clone the repository: git clone https://github.com/your-username/Maze-A-Star-Visualization.git
2. Install the required dependencies: pip install pygame

## Usage

1. Run the program: python main.py

2. Interface Controls:
- Left-click to place nodes: The start node will be placed first, then the end node, then all barriers. 
- Right-click to remove nodes: Right-clicking on nodes will remove them from the maze. If you remove the start and/or end node(s), those will be the next ones to be placed. 
- Press 'x' to generate a random maze.
- Press 'r' to reset the maze.
- Press the spacebar to start the maze-solving algorithm.

3. Algorithm Visualization:
- The maze-solving algorithm uses the A* algorithm with a Manhattan distance heuristic.
- The algorithm starts searching from the start node and expands neighboring nodes until it reaches the end node.
- Once the algorithm finishes, the shortest path from the start to the end node will be highlighted in purple.

## Demonstration of Randomly Generated Maze solving
An important note -> After randomly generating a maze, the user can edit it by removing/add barriers! 
https://www.loom.com/share/bf8fc2ca2c7f46fea35f1bdcce136bc3?sid=cb368c67-c49e-4417-9e17-9535e1499c13

## Demonstration of Maze Solving User Drawn Barriers 
https://www.loom.com/share/a13492f8a19e499881269f6e55964603

