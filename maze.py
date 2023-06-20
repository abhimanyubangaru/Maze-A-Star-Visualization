import random 
import pygame

def generate_maze(width, height):
    # Ensure the width and height are odd
    
    maze = [[1] * width for _ in range(height)]
    
    # to start on edge 
    start = (0, random.randint(1, width - 2))
    # to end on edge 
    end = (height - 1, random.randint(1, width - 2))
    
    stack = [(start[0] + 1, start[1])]  # Start one row down

    while stack:
        row, col = stack[-1]
        neighbors = [] 
        
        if row > 2 and maze[row-2][col] == 1:
            neighbors.append((row-2,col))
        if col > 2 and maze[row][col-2] == 1:
            neighbors.append((row,col-2))
        if row < height - 3 and maze[row+2][col] == 1:
            neighbors.append((row+2,col))
        if col < width - 3 and maze[row][col+2] == 1:
            neighbors.append((row,col+2))
        
        if neighbors:
            nextrow, nextcol = random.choice(neighbors)
            maze[(row + nextrow) // 2][(col + nextcol) // 2] = 0
            stack.append((nextrow, nextcol))
            maze[nextrow][nextcol] = 0
        else:
            stack.pop()

    return maze

def initialize_window(maze_width, maze_height, cell_size):
    return pygame.display.set_mode((maze_width * cell_size, maze_height * cell_size))

def draw_maze(window, maze, cell_size):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            color = (0, 0, 0) if cell == 1 else (255, 255, 255)  # Black for walls, white for paths
            pygame.draw.rect(window, color, pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size))
