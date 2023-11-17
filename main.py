import pygame

# Define Colors
GREY = (128, 128, 128)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
wall_list = []

# Wall Class
class Wall():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw_wall(self, screen):
        pygame.draw.rect(screen, GREY, [self.x, self.y, self.width, self.height])

# Make wall list
def create_wall_list():
    # append walls into list
    wall_list.append(Wall(50, 50, 700, 20))
    wall_list.append(Wall(50, 50, 20, 700))
    wall_list.append(Wall(50, 750, 700, 20))
    wall_list.append(Wall(750, 50, 20, 720))
    wall_list.append(Wall(140, 200, 150, 20))
    wall_list.append(Wall(140, 600, 150, 20))
    wall_list.append(Wall(350, 250, 20, 300))
    wall_list.append(Wall(400, 70, 20, 200))
    wall_list.append(Wall(600, 300, 120, 20))
    wall_list.append(Wall(500, 600, 250, 20))

def check_collision(player):
    for i in range(len(wall_list)):
        if rectCollide(player, wall_list[i]):
            return i
    
    return -1

def rectCollide(rect1, rect2):
    return rect1.x < rect2.x + rect2.width and rect1.y < rect2.y + rect2.height and rect1.x + rect1.width > rect2.x and rect1.y + rect1.height > rect2.y


        
# Player Class
class Player():
    def __init__(self, x, y, width, height, change_x, change_y):
        # Class attributes
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # player's speed and direction / vector
        self.change_x = change_x
        self.change_y = change_y
        
    
    def go_left(self):
        self.change_x = -3
    
    def go_right(self):
        self.change_x = 3
    
    def go_up(self):
        self.change_y = -3
    
    def go_down(self):
        self.change_y = 3

    def update(self):
        # Horizontal collision check
        self.x += self.change_x
        wall_index = check_collision(self)
        if wall_index != -1:
            if self.change_x > 0:
                self.x = wall_list[wall_index].x - self.width
            else:
                self.x = wall_list[wall_index].x + wall_list[wall_index].width
        # Vertical collision check
        self.y += self.change_y
        wall_index = check_collision(self)
        if wall_index != -1:
            if self.change_y > 0:
                self.y = wall_list[wall_index].y - self.height
            elif self.change_y < 0:
                self.y = wall_list[wall_index].y + wall_list[wall_index].height
        
            
            

    def hzstop(self):
        self.change_x = 0

    def vtstop(self):
        self.change_y = 0

    def draw_player(self, screen):
        screen.fill(WHITE)
        pygame.draw.rect(screen, RED, [self.x, self.y, self.width, self.height])

def main():
    # Initialize pygame
    pygame.init()

    # Screen
    size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(size)

    create_wall_list()
    # Create player
    player = Player(200, 380, 20, 20, 0, 0)
    

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # loop until user clicks the close button
    done = False
    while not done:
        # EVENT STUFF
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                elif event.key == pygame.K_RIGHT:
                    player.go_right()
                elif event.key == pygame.K_UP:
                    player.go_up()
                elif event.key == pygame.K_DOWN:
                    player.go_down()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0 or event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.hzstop()
                elif event.key == pygame.K_UP and player.change_y < 0 or event.key == pygame.K_DOWN and player.change_y > 0:
                    player.vtstop()
                
        # LOGIC STUFF 
        player.update()       

        # Draw Stuff

        # Player
        player.draw_player(screen)
        # Walls
        for i in range(len(wall_list)):
            wall_list[i].draw_wall(screen)

        clock.tick(60)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

