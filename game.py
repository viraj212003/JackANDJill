import pygame
from pygame.locals import *

pygame.init()

screen_width=700
screen_height=700

screen=pygame.display.set_mode((screen_width,screen_height))


pygame.display.set_caption("chutiya")

tile_size=100

bg_img=pygame.image.load('illustration12.jpg')
def draw_grid():
    for line in range (0,8):
         pygame.draw.line(screen,(125,125,125),(0,line*tile_size),(screen_width,line*tile_size))
         pygame.draw.line(screen,(125,125,125),(line*tile_size,0),(line*tile_size,screen_height))                                  
class World():
    def __init__(self,data):
        self.tile_list=[]
        

        platform_img=pygame.image.load('platfrom.png')
        base_img=pygame.image.load('base.png')
        row_count=0
        for row in data:
            col_count = 0
            for tile in row:
                if tile==1:
                    img=pygame.transform.scale(platform_img,(tile_size,tile_size))
                    img_rect=img.get_rect()
                    img_rect.x=col_count*tile_size
                    img_rect.y=row_count*tile_size
                    tile=(img,img_rect)
                    self.tile_list.append(tile)
                if tile==2:
                    img=pygame.transform.scale(base_img,(tile_size,tile_size))
                    img_rect=img.get_rect()
                    img_rect.x=col_count*tile_size
                    img_rect.y=row_count*tile_size
                    tile=(img,img_rect)
                    self.tile_list.append(tile)
                col_count+=1
            row_count+=1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0],tile[1])
            

world_data=[
[0,0,0,0,0,0,1],
[0,0,1,0,0,1,0],
[0,1,0,0,1,0,0],
[0,0,1,0,1,1,0],
[0,0,0,1,0,0,0],
[0,0,1,0,1,0,0],
[2,2,2,2,2,2,2],
]


world= World(world_data)
run=True
while run==True:
    screen.blit(bg_img,(0,0))

    world.draw()

    draw_grid()

    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    pygame.display.update()

pygame.quit()
