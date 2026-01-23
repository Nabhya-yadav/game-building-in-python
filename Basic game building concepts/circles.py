import pygame
pygame.init()
screen=pygame.display.set_mode((400,400))
screen.fill((255,255,255))
green=(0,255,0)
#solid circle
pygame.draw.circle(screen,green,(300,300),50)
#hollow circle
pygame.draw.circle(screen,green,(100,100),50,3)
done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

   
    pygame.display.flip()
pygame.quit()