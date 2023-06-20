from queue import PriorityQueue
import pygame

def h(p1,p2):
    # manhattan distance
    x1,y1 = p1
    x2,y2 = p2 
    # above is shortcut in python 
    return abs(x1 - x2) + abs(y1-y2)

def reconstruct_path(came_from, current,draw):
    while current in came_from:
        current = came_from[current]
        current.makePath()
        draw()

def algorithm(draw,grid,start,end):
    count = 0 
    open_set = PriorityQueue()
    #count is purely to break ties
    open_set.put((0, count, start))
    #dictionary is supposed to function as a parents array 
    came_from = {} 
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0 
    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = h(start.get_pos(),end.get_pos())

    #priority queue doesn't have size so we are keeping another hash with the same contents to keep track of size  
    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            #make path
            reconstruct_path(came_from, end, draw)
            end.makeEnd() 
            start.makeStart()
            return True 
        
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.makeOpen() 
        draw()

        if current != start:
            current.makeClosed() 
    return False 
     