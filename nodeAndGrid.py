import colors
import pygame 
from maze import generate_maze
class Node:
    def __init__(self,row,col,width, total_rows):
        self.row = row 
        self.col = col 
        self.x = row * width 
        self.y = col * width 
        self.color = colors.WHITE
        self.neighbors = [] 
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def isClosed(self):
        return self.color == colors.RED
    
    def isOpen(self):
        return self.color == colors.GREEN 

    def isBarrier(self):
        return self.color == colors.BLACK
    
    def isStart(self):
        return self.color == colors.ORANGE
    
    def isEnd(self):
        return self.color == colors.BLUE
    
    def reset(self):
        self.color = colors.WHITE
    
    def makeClosed(self):
        self.color = colors.RED
         
    def makeOpen(self):
        self.color = colors.GREEN

    def makeBarrier(self):
        self.color = colors.BLACK

    def makeStart(self):
        self.color = colors.ORANGE

    def makeEnd(self):
        self.color = colors.BLUE
    
    def makePath(self):
        self.color = colors.AQUAMARINE

    def draw(self, win):

        pygame.draw.rect(win,self.color, (self.x,self.y,self.width, self.width))

    def updateNeighbors(self,grid):
        self.neighbors = [] 
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].isBarrier(): #DOWN
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].isBarrier(): #UP
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].isBarrier(): #LEFT
            self.neighbors.append(grid[self.row ][self.col + 1])
            
        if self.col > 0 and not grid[self.row][self.col - 1].isBarrier(): #RIGHT
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
         return False 

def make_grid(rows, width):
    grid = [] 
    gap = width // rows
    # for i in range(0, rows):
    #     grid.append([] )
    #     for j in range(0, rows):
    #         node = Node(i,j, gap, rows)
    #         grid[i].append(node)
    grid = [[Node(i, j, gap, rows) for j in range(rows)] for i in range(rows)]
    return grid

def make_random_maze(rows, width):
    random_maze = generate_maze(rows,rows)
    grid = [] 
    gap = width // rows

    for i in range(rows):
        grid.append([])  # Initialize a new row in the grid
        for j in range(rows):
            node = Node(i,j,gap,rows)
            if random_maze[i][j] == 1:
                node.makeBarrier()  # Corrected method name
            grid[i].append(node)  # Append the node to the row

    return grid


def draw_grid(win,rows,width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, colors.GREY, (0,i * gap), (width, i * gap))
        for j in range(rows):
                pygame.draw.line(win, colors.GREY, (j * gap, 0), (j * gap, width))
            
def draw(win, grid, rows, width):
    win.fill(colors.WHITE)
    for row in grid:
        for node in row: 
            node.draw(win)

    draw_grid(win,rows,width)
    pygame.display.update() 

def get_clicked_position(pos,rows,width):
    gap = width // rows 
    y,x = pos 
    row = y // gap 
    col = x // gap 
    
    return row,col 

