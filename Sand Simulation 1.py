import pygame
import math
import copy
import random
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BLOCK_SIZE = 7
SAND_COUNT = 0
cols = math.floor(WINDOW_HEIGHT/BLOCK_SIZE)
rows = math.floor(WINDOW_WIDTH/BLOCK_SIZE)
SAND_ARRAY = [[None for i in range(cols)] for j in range(rows)]
SAND_ARRAY_Next_Frame = [[None for i in range(cols)] for j in range(rows)]
RANDOM_DIR = (0,1,-1)
def main():
    pygame.display.set_caption('Sand Simulation (NOT OPTIMIZED) - JBill')
    background_color = (0,0,0)
    global SCREEN
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    SCREEN.fill(background_color)
    running= True
    dragging = False
    
    fall = pygame.USEREVENT + 1
    pygame.time.set_timer(fall, 17 )
    while running:
        # DrawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                dragging = True
            if event.type == pygame.MOUSEBUTTONUP:
                dragging = False
            if event.type == pygame.MOUSEMOTION:
                if dragging:
                    Drag_Event()
            if event.type == fall:
                pygame.display.flip()
                DrawSand()

                    
            
            
            
def DrawGrid():
    for x in range(0, WINDOW_WIDTH, BLOCK_SIZE):
        for y in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (200,200,200), rect, 1)


def Drag_Event():
    global SAND_COUNT
    SAND_COUNT += 1
    pos = pygame.mouse.get_pos()
    
    if(pos[0] > 0 and pos[1] > 0 and pos[0] <WINDOW_WIDTH and pos[1] <WINDOW_HEIGHT):
        SAND_ARRAY[math.floor(pygame.mouse.get_pos()[0]/BLOCK_SIZE)][math.floor(pygame.mouse.get_pos()[1]/BLOCK_SIZE)] = pygame.Rect(RoundToNearestN(pos[0],BLOCK_SIZE),RoundToNearestN(pos[1],BLOCK_SIZE),BLOCK_SIZE,BLOCK_SIZE)
    
    # rect = pygame.Rect(RoundToNearestN(pos[0],BLOCK_SIZE),RoundToNearestN(pos[1],BLOCK_SIZE),BLOCK_SIZE,BLOCK_SIZE)
    #pygame.draw.rect(SCREEN,(255,255,255),SAND_ARRAY[math.floor(pygame.mouse.get_pos()[0]/BLOCK_SIZE)][math.floor(pygame.mouse.get_pos()[1]/BLOCK_SIZE)])
    pass          
def RoundToNearestN(n,base):
    return base * math.floor(n/base)
    pass        
def DrawSand():
    global SAND_ARRAY ,SAND_ARRAY_Next_Frame
    SCREEN.fill((0,0,0))
    for x in range(rows):
        for y in range(cols):
            if(SAND_ARRAY[x][y] != None):
                rec = SAND_ARRAY[x][y]
                if(y + 1 < cols and SAND_ARRAY[x][y+1] == None):
                    SAND_ARRAY_Next_Frame[x][y+1] = pygame.Rect(rec.x, rec.y+BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE)
                else:
                    # SAND_ARRAY_Next_Frame[x][y] = pygame.Rect(rec.x, rec.y,BLOCK_SIZE,BLOCK_SIZE)
                    dir = random.choice(RANDOM_DIR)
                    match dir:
                        case -1:
                            if(x-1 >=0 and  y+1 <cols  and SAND_ARRAY[x-1][y+1] == None):
                                SAND_ARRAY_Next_Frame[x-1][y+1] = pygame.Rect(rec.x - BLOCK_SIZE, rec.y + BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE)
                            else:
                                SAND_ARRAY_Next_Frame[x][y] = pygame.Rect(rec.x, rec.y,BLOCK_SIZE,BLOCK_SIZE)

                        case 1:
                            if(x+1 <rows and  y+1 <cols  and SAND_ARRAY[x+1][y+1] == None):
                                SAND_ARRAY_Next_Frame[x+1][y+1] = pygame.Rect(rec.x + BLOCK_SIZE, rec.y + BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE)
                            else:
                                SAND_ARRAY_Next_Frame[x][y] = pygame.Rect(rec.x, rec.y,BLOCK_SIZE,BLOCK_SIZE)
                        case _:
                            SAND_ARRAY_Next_Frame[x][y] = pygame.Rect(rec.x, rec.y,BLOCK_SIZE,BLOCK_SIZE)
                            
                
                pygame.draw.rect(SCREEN,(194, 178, 128),rec)
    SAND_ARRAY = copy.deepcopy(SAND_ARRAY_Next_Frame)
    SAND_ARRAY_Next_Frame = [[None for i in range(cols)] for j in range(rows)]
main()