
import world, player, pygame, sys

def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((800, 600))
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    f = pygame.font.Font(pygame.font.get_default_font(), 20)
    clock = pygame.time.Clock()
    ticks = 0
    gameOn = True

    pPlayer = player.Player([400, 300], 5)
    level = world.Level(1, pPlayer)
    states = [False, False, False, False]
    appliers = [(0,-1), (0,1), (1,0), (-1,0)]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.constants.QUIT: sys.exit(0)
            elif event.type == pygame.constants.KEYDOWN:
                if event.key in [273, 274, 275, 276]:
                    states[event.key - 273] = True
                if not gameOn:
                    gameOn = True
                    pPlayer = player.Player([400, 300], 5)
                    level = world.Level(1, pPlayer)
                    states = [False, False, False, False]
                    ticks = 0
            elif event.type == pygame.constants.KEYUP:
                if event.key in [273, 274, 275, 276]:
                    states[event.key - 273] = False
                    
        for state, applier in zip(states, appliers):
            if state:
                pPlayer.x_force += applier[0]
                pPlayer.y_force += applier[1]

        level.runIter()
        screen.blit(background, (0, 0))
        if gameOn:
            level.draw(screen)
            screen.blit(f.render(str(ticks), True, (25, 25, 200)), (10, 10))
        else:
            screen.blit(f.render("You Lose. :( Score: %s"%(ticks), True, (25, 25, 200)), (325, 275))
            
        pygame.display.flip()
        
        if gameOn:
            ticks += 1
        if ticks % 100 == 0:
            level.addWell()
        if level.isOver():
            gameOn = False
        
        clock.tick(20)

if __name__ == "__main__":
    main()
