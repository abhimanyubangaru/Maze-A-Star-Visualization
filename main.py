from ast import Lambda
import colors
import pygame
from heuristicfunction import algorithm
from nodeAndGrid import (
    Node,
    make_grid,
    draw_grid,
    draw,
    get_clicked_position,
    make_random_maze
)

WIDTH = 800 
window_width = 800
window_height = 800

WIN = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("click to place, right click to remove, x for random maze, r for reset")

def main(win, width):

    ROWS = 50 
    grid = make_grid(ROWS, width)

    start = None 
    end = None 

    run = True 
    started = False
    while run: 
        draw(win,grid,ROWS,width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if started:
                continue

            # if pressed left mouse button 
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos() 
                row,col = get_clicked_position(pos, ROWS, width)
                node = grid[row][col]
                if not start and node != end:
                    start = node 
                    start.makeStart() 
                elif not end and node != start: 
                    end = node 
                    end.makeEnd()
                elif node != start and node != end:
                    node.makeBarrier()


            elif pygame.mouse.get_pressed()[2]: # RIGHT 
                pos = pygame.mouse.get_pos() 
                row,col = get_clicked_position(pos, ROWS, width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            if node.color != colors.BLACK and node != start and node != end:
                                node.reset()
                    for row in grid:
                        for node in row:
                            node.updateNeighbors(grid) 
                    
                    algorithm(lambda: draw(win,grid,ROWS,width),grid,start,end)
                    #lambda is an anonymous function, you dont need to give it a name you can just pass it along 

                if event.key == pygame.K_r:
                    start = None
                    end = None 
                    grid = make_grid(ROWS, width)

                if event.key == pygame.K_x:
                    start = None
                    end = None 
                    grid = make_random_maze(ROWS,width)

    pygame.quit()


main(WIN, WIDTH) 