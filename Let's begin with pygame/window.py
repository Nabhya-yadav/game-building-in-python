import pygame
pygame.init()
pygame.display.set_mode((500,600))

pygame.display.set_caption("My Game")

done=True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.flip()        

