import pygame


# 1 repo this
# 2 find out how to create two separate displays, main menu versus outside menu
# 3 find out how to create text for menu
# 4 find out how to create buttons for menu

screen = pygame.display.set_mode((500, 500))

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("black")

    pygame.display.flip()

    clock.tick(60)

pygame.quit()



# Start Screen
    # Select screen size (mode) 300x 500x 800x
    # Select mode (speed) slow normal fast
    # select color background
    # Select start button
    # Show high score

# method to remember high score
# display current score
# change color of current score when it's greater than older score
# Start snake in center facing right
# method for adding snake parts
# method for moving snake as a whole
# method for spawning an apple
# method for eating the apple
# method for making the snake hit itself or hitting wall

