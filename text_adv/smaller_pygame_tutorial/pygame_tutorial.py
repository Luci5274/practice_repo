import pygame

pygame.init()

white = (255, 255, 255)
green =(0, 255,0 )
blue = (0, 0, 128)

x = 400
y = 400

display_surface = pygame.display.set_mode((x,y))

pygame.display.set_caption('Show text')

font = pygame.font.Font('freesansbold.ttf' , 32)

text = font.render(' >:)', True, green, blue )

textRect = text.get_rect()

textRect.center = (x //2 , y // 2)

while True:
    display_surface.fill(white)

    display_surface.blit(text, textRect)

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()