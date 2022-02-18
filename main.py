import pygame
import sys
import os
import random

# Initializing window
width = 800
height = 600
FPS  = 12

pygame.init()
pygame.display.set_caption('sliding tiles')
gameDisplay = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Define colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
brown = (100,40,0)

background = pygame.image.load('white.jpg')
background = pygame.transform.scale(background, (800,600))

font = pygame.font.Font(os.path.join(os.getcwd(), 'Comic Book.ttf'), 70)

class Generate_Puzzle:
    def __init__(self, gridsize, tilesize, margin):

        self.gridsize,self.tilesize,self.margin = gridsize, tilesize, margin

        self.tiles_no = gridsize[0]*gridsize[1]-1 # number of tiles
        self.tiles = [[x, y] for y in range(gridsize[1]) for x in range(gridsize[0])] #tile coordinates

        self.tilepos = {{x,y} : (x*(tilesize+margin)+margin,y*(tilesize+margin)+margin) for y in range(gridsize[1]) for x in range(gridsize[0])} # tile position
        self.prev = None

        self.tile_images = []
        font = pygame.font.Font(None, 80)

        for i in range(self.tiles_no):
            image = pygame.Surface((tilesize,tilesize)) # display tiles
            image.fill(brown)
            text = font.render(str(i+1), 2, (255,255,255)) #text on tiles
            width,height = text.get_size() #text size
            image.blit(text, ((tilesize-width)/2, (tilesize-height)/2)) # display text in middle of tile
            self.tile_images += [image]

    def blank_pos(self):
        return self.tiles[-1]

    def setBlankPos(self, pos):
        self.tiles[-1] = pos
    opentile = property(blank_pos, setBlankPos) # get and set the pos of blank

    def switchTile(self, tile):
        self.tiles[self.tiles.index(tile)]=self.opentile
        self.opentile = tile
        self.prev = self.opentile

    def checkInGrid(self, tile):
        return tile[0]>=0 and tile[0]<self.gridsize[0] and tile[1]>=0 and tile[1]<self.gridsize[1]

    def closeTo(self): #adjacent tile postion to blank (which tiles can move to blank position)
        x, y = self.opentile
        return (x-1,y), (x+1,y),(x,y-1), (x,y+1)

    def setTileRandomly(self):
        adj = self.closeTo()
        adj = [pos for pos in adj if self.checkInGrid(pos) and pos!=self.prev]
        tile = random.choice(adj)
        self.switchTile(tile)
        #print(self.prev)

    def updateTilePos(self, dt): # update tile position
        mouse = pygame.mouse.get_pressed()
        mpos = pygame.mouse.get_pos()

        if mouse[0]:
            x,y = mpos[0]%(self.tilesize+self.margin),mpos[1]%(self.tilesize+self.margin)
            if x>self.margin and y>self.margin:
                tile = mpos[0]//self.tilesize,mpos[1]//self.tilesize
                if self.checkInGrid(tile) and tile in self.closeTo():
                    self.switchTile(tile)

    def drawTile(self,gameDisplay):
        for i in range(self.tiles_no):
            x,y = self.tilepos[self.tiles[i]]
            gameDisplay.blit(self.tileImages[i], (x,y))

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for i in range:
                    self.setTileRandomly()

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


    def game_front_screen():
        gameDisplay.blit(background, (0,0))
        draw_text(gameDisplay, "SLIDING TILE GAME!", 90, width / 2, height / 4)
        draw_text(gameDisplay, "Press a key to begin!", 80, width / 2, height * 3 / 4)
        pygame.display.flip()
        waiting = True
        while waiting:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.get():
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    waiting = False
    

    def level_screen():
        L1, L1_RECT = makeText('Level1', RED,True,100,40)

        gameDisplay.blit(L1, L1_RECT)

        mpos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if L1_RECT.colliddepoint(mpos):
                level1()

    def level1():
        program=Generate_Puzzle((3,3),80,5)
        while True:
            dt = clock.tick()/1000
            gameDisplay.blit(background, (0,0))
            draw_text(gameDisplay)
            pygame.draw_tile(gameDisplay)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit();sys.exit()
                program.events(event)
            program.updateTilePos(dt)


    # Main loop of the game
    game_over = True
    game_running = True
    while game_running :
        if game_over :
            game_front_screen()
        game_over = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
        gameDisplay.blit(background, (0,0))
        level_screen()

        pygame.display.update()
        clock.tick(FPS)
    pygme.quit()

