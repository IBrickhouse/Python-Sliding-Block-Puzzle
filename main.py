#importing modules
import pygame
import sys
import os 
import random

# loading background image for processing
background = pygame.image.load('images/momo.jpg') 
dimensions = background.get_rect().size

#print(dimensions[0])

#initializing window
WIDTH = dimensions[0]
HEIGHT = dimensions[1]
FPS = 12                                                 #controls how often the gameDisplay should refresh. In our case, it will refresh every 1/12th second
pygame.init()
pygame.display.set_caption('sliding tiles')
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))   #setting game window size
clock = pygame.time.Clock()

# Define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
brown = (100,40,0)

#setting game background image and size
background = pygame.transform.scale(background, (dimensions[0], dimensions[1]))

#set game text font
font = pygame.font.Font(os.path.join(os.getcwd(), 'Comic Book.ttf'), 70)


#*Class for whole game*
class Generate_Puzzle:                     
    def __init__(self, gridsize, tilesize, margin):  
        
        self.gridsize,self.tilesize,self.margin = gridsize, tilesize, margin

        self.tiles_no = gridsize[0]*gridsize[1]-1          # no of tiles
        self.tiles = [(x,y) for y in range(gridsize[1]) for x in range(gridsize[0])]  #coordinate of tiles
       

        self.tilepos = {(x,y):(x*(tilesize+margin)+margin,y*(tilesize+margin)+margin) for y in range(gridsize[1]) for x in range(gridsize[0])}  #tile position
        self.prev = None

        self.tile_images =[]
        font = pygame.font.Font(None, 80)           

        for i in range(self.tiles_no):
            image = pygame.Surface((tilesize,tilesize))    #display tiles 
            image.fill(brown)
            text = font.render(str(i+1),2,(255,255,255))  ##text on tiles
            width,height = text.get_size()  #text size
            image.blit(text,((tilesize-width)/2 , (tilesize-height)/2))   #####display text in the middle of tile
            self.tile_images += [image]
           

    def Blank_pos(self):  
        
        return self.tiles[-1]
    
    

    def set_Blank_pos(self,pos):

        self.tiles[-1] = pos
    opentile = property(Blank_pos, set_Blank_pos)   #get and set the pos of blank



    def switch_tile(self, tile):
        self.tiles[self.tiles.index(tile)]=self.opentile      #
        self.opentile = tile
        self.prev= self.opentile
        


    def check_in_grid(self, tile):
        return tile[0]>=0 and tile[0]<self.gridsize[0] and tile[1]>=0 and tile[1]<self.gridsize[1]


    def close_to(self):              #adjacent tile postion to blank (which tiles can move to blank position)
        x, y = self.opentile
        return (x-1,y),(x+1,y),(x,y-1),(x,y+1)

    def set_tile_randomly(self):
        adj = self.close_to()
        adj = [pos for pos in adj if self.check_in_grid(pos)and pos!= self.prev ]
        tile = random.choice(adj)
        self.switch_tile(tile)
        #print(self.prev)


    def update_tile_pos(self,dt):        #update tile position

        mouse = pygame.mouse.get_pressed()
        mpos = pygame.mouse.get_pos()

        if mouse[0]:
            x,y = mpos[0]%(self.tilesize+self.margin),mpos[1]%(self.tilesize+self.margin)
            if x>self.margin and y>self.margin:
                tile = mpos[0]//self.tilesize,mpos[1]//self.tilesize
                if self.check_in_grid(tile) and tile in self.close_to():
                    self.switch_tile(tile)


    def draw_tile(self,gameDisplay):                             #####draw tiles in particular positioned
        for i in range(self.tiles_no):
            x,y = self.tilepos[self.tiles[i]]
            gameDisplay.blit(self.tile_images[i],(x,y))
                    


    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:    #press space to random the tiles
                for i in range(100):
                    self.set_tile_randomly()




################creating levels


def level_screen():
    L1, L1_RECT = makeText('Level1', RED, True, 100, 40)
    L2, L2_RECT = makeText('Level2', RED, True, 500, 40)
    L3, L3_RECT = makeText('Level3', RED, True, 100, 180)
    L4, L4_RECT = makeText('Level4', RED, True, 500, 180)
    L5, L5_RECT = makeText('Level5', RED, True, 100, 320)
    L6, L6_RECT = makeText('Level6', RED, True, 500, 320)
    L7, L7_RECT = makeText('Level7', RED, True, 100, 460)
    L8, L8_RECT = makeText('Level8', RED, True, 500, 460)

    #### display levels on the screen

    gameDisplay.blit(L1, L1_RECT)
    gameDisplay.blit(L2, L2_RECT)
    gameDisplay.blit(L3, L3_RECT)
    gameDisplay.blit(L4, L4_RECT)
    gameDisplay.blit(L5, L5_RECT)
    gameDisplay.blit(L6, L6_RECT)
    gameDisplay.blit(L7, L7_RECT)
    gameDisplay.blit(L8, L8_RECT)

    ###########checking collision of mouse and levels
    mpos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if L1_RECT.collidepoint(mpos):
            level1()
        elif L2_RECT.collidepoint(mpos):
            level2()
                        
        elif L3_RECT.collidepoint(mpos):
            level3()

        elif L4_RECT.collidepoint(mpos):
            level4()

        elif L5_RECT.collidepoint(mpos):
            level5()

        elif L5_RECT.collidepoint(mpos):
            level6()

        elif L6_RECT.collidepoint(mpos):
            level6()

        elif L7_RECT.collidepoint(mpos):
            level7()

        elif L8_RECT.collidepoint(mpos):
            level8()

def level1():
    program=Generate_Puzzle((3,3),80,5)
    while True:
        dt = clock.tick()/1000
        gameDisplay.blit(background, (0,0))
        draw_text(gameDisplay,'PRESS SPACE TO START GAME', 60,370 , 500)
        program.draw_tile(gameDisplay)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit();sys.exit()
            program.events(event)
        program.update_tile_pos(dt)
    
    

def level2():
    program=Generate_Puzzle((3,4),80,5)
    while True:
        dt = clock.tick()/1000
        gameDisplay.blit(background, (0,0))
        draw_text(gameDisplay,'PRESS SPACE TO START GAME', 60,370 , 500)
        program.draw_tile(gameDisplay)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit();sys.exit()
            program.events(event)
        program.update_tile_pos(dt)

def level3():
    program=Generate_Puzzle((4,3),80,5)
    while True:
        dt = clock.tick()/1000
        gameDisplay.blit(background, (0,0))
        draw_text(gameDisplay,'PRESS SPACE TO START GAME', 60,370 , 500)
        program.draw_tile(gameDisplay)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit();sys.exit()
            program.events(event)
        program.update_tile_pos(dt)

def level4():
    program=Generate_Puzzle((4,4),80,5)
    while True:
        dt = clock.tick()/1000
        gameDisplay.blit(background, (0,0))
        draw_text(gameDisplay,'PRESS SPACE TO START GAME', 60,370 , 500)
        program.draw_tile(gameDisplay)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit();sys.exit()
            program.events(event)
        program.update_tile_pos(dt)
def level5():
    program=Generate_Puzzle((4,5),80,5)
    while True:
        dt = clock.tick()/1000
        gameDisplay.blit(background, (0,0))
        draw_text(gameDisplay,'PRESS SPACE TO START GAME', 60,370 , 500)
        program.draw_tile(gameDisplay)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit();sys.exit()
            
            program.events(event)
        program.update_tile_pos(dt)
def level6():
    program=Generate_Puzzle((5,5),80,5)
    while True:
        dt = clock.tick()/1000
        gameDisplay.blit(background, (0,0))
        draw_text(gameDisplay,'PRESS SPACE TO START GAME', 60,370 , 500)
        program.draw_tile(gameDisplay)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();sys.exit()
            program.events(event)
        program.update_tile_pos(dt)

def level7():
    program=Generate_Puzzle((5,4),80,5)
    while True:
        dt = clock.tick()/1000
        gameDisplay.blit(background, (0,0))
        draw_text(gameDisplay,'PRESS SPACE TO START GAME', 60,370 , 500)
        program.draw_tile(gameDisplay)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit();sys.exit()
            program.events(event)
        program.update_tile_pos(dt)

def level8():
    program=Generate_Puzzle((6,5),80,5)
    while True:
        dt = clock.tick()/1000
        gameDisplay.blit(background, (0,0))
        draw_text(gameDisplay,'PRESS SPACE TO START GAME', 60,370 , 500)
        program.draw_tile(gameDisplay)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit();sys.exit()
            program.events(event)
        program.update_tile_pos(dt)


# create the Surface and Rect objects for some text.
def makeText(text, color, bgcolor, top, left):
    textSurf = font.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return (textSurf, textRect)    


# Generic method to draw fonts on the screen   
font_name = pygame.font.match_font('Comic Book.ttf')
def draw_text(display, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, brown)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    gameDisplay.blit(text_surface, text_rect)

 ##front screen of the game

def game_front_screen():
    gameDisplay.blit(background, (0,0))
    draw_text(gameDisplay, "SLIDING TILE GAME!", 90, WIDTH / 2, HEIGHT / 4)
    draw_text(gameDisplay, "Press a key to begin!", 80, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
                

#####mainloop

game_over = True        
game_running = True 
while game_running :
    if game_over :
        game_front_screen()           #front screen of the game
    game_over = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:          
            game_running = False
    gameDisplay.blit(background, (0,0))  
    level_screen()                ##goes to second screen of the game which is levels 
   
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()


# background image size getter (may more to seperate file in future)
# does not use external package. currently not used.
def get_image_size(fname):
    '''Determine the image type of fhandle and return its size.
    from draco'''
    with open(fname, 'rb') as fhandle:
        head = fhandle.read(24)
        if len(head) != 24:
            return
        if imghdr.what(fname) == 'png':
            check = struct.unpack('>i', head[4:8])[0]
            if check != 0x0d0a1a0a:
                return
            width, height = struct.unpack('>ii', head[16:24])
        elif imghdr.what(fname) == 'gif':
            width, height = struct.unpack('<HH', head[6:10])
        elif imghdr.what(fname) == 'jpeg':
            try:
                fhandle.seek(0) # Read 0xff next
                size = 2
                ftype = 0
                while not 0xc0 <= ftype <= 0xcf:
                    fhandle.seek(size, 1)
                    byte = fhandle.read(1)
                    while ord(byte) == 0xff:
                        byte = fhandle.read(1)
                    ftype = ord(byte)
                    size = struct.unpack('>H', fhandle.read(2))[0] - 2
                # We are at a SOFn block
                fhandle.seek(1, 1)  # Skip `precision' byte.
                height, width = struct.unpack('>HH', fhandle.read(4))
            except Exception: #IGNORE:W0703
                return
        else:
            return
        return width, height
    
