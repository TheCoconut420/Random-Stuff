import pygame
pygame.font.init()
import random



class game: 
    def __init__(self):
        self.WIDTH = 1920
        self.rec_width = self.WIDTH / 30
        self.enemy_width = self.rec_width
        self.stalker_width = self.rec_width
        self.coin_width = self.WIDTH / 96

        self.HEIGHT = self.WIDTH // 16 * 9
        self.rec_height = self.rec_width
        self.enemy_height = self.rec_height
        self.stalker_height = self.rec_height
        self.info_bar_height = self.WIDTH / 25

        self.x = 0
        self.enemy_x = self.WIDTH - self.enemy_width
        self.stalker_x = self.HEIGHT / 2
        self.coin_x = self.WIDTH / 2

        self.y = 0 + self.info_bar_height
        self.enemy_y = self.HEIGHT - self.enemy_height
        self.stalker_y = self.HEIGHT / 2
        self.coin_y = self.HEIGHT / 2

        self.speed = self.WIDTH / 350
        self.enemy_speed_horizontal = self.speed / 3
        self.enemy_speed_vertical = self.speed / 3
        self.stalker_speed = self.speed / 3
 
        self.FPS = 120

        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.yellow = (255, 255, 0)

        self.score = 0
        self.my_font = pygame.font.SysFont("monospace", self.WIDTH // 50)
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Simple Game")

    def draw_window(self):
        self.WIN.fill(self.white)
        self.draw_player()
        self.draw_enemy()
        self.draw_coin()
        self.draw_info_bar()
        self.draw_stalker()

        self.wall_collision()
        self.enemy_collision()
        self.coin_collision()

        self.player_movement()
        self.enemy_movement()
        self.stalker_movement()
        
        pygame.display.update()

    def draw_info_bar(self):
        self.info_bar = pygame.draw.rect(self.WIN, self.black, (0, 0, self.WIDTH, self.info_bar_height))
        self.info_bar_text = self.my_font.render("Score: " + str(self.score), 1, self.white)
        self.WIN.blit(self.info_bar_text, (self.WIDTH / 2 - self.info_bar_text.get_width() / 2, self.info_bar_height / 2 - self.info_bar_text.get_height() / 2))

    def draw_player(self):
        self.player = pygame.draw.rect(self.WIN, self.green, (self.x, self.y, self.rec_width, self.rec_height))
        self.player_edge = pygame.draw.rect(self.WIN, self.black, (self.x, self.y, self.rec_width, self.rec_height), 4)
    
    def draw_enemy(self):
        self.enemy = pygame.draw.rect(self.WIN, self.red, (self.enemy_x, self.enemy_y, self.enemy_width, self.enemy_height))
        self.enemy_edge = pygame.draw.rect(self.WIN, self.black, (self.enemy_x, self.enemy_y, self.enemy_width, self.enemy_height), 4)

    def draw_stalker(self):
        self.stalker = pygame.draw.rect(self.WIN, self.red, (self.stalker_x, self.stalker_y, self.stalker_width, self.stalker_height))
        self.stalker_edge = pygame.draw.rect(self.WIN, self.black, (self.stalker_x, self.stalker_y, self.stalker_width, self.stalker_height), 4)

    def draw_coin(self):
        self.coin = pygame.draw.circle(self.WIN, self.yellow, (self.coin_x, self.coin_y), self.coin_width)
        self.coin_edge = pygame.draw.circle(self.WIN, self.black, (self.coin_x, self.coin_y), self.coin_width, 2)

    def coin_collision(self):
        collide = self.player.colliderect(self.coin)
        if collide:
            self.coin_x = random.randint(0, self.WIDTH)
            self.coin_y = random.randint(int(self.info_bar_height), self.HEIGHT)
            self.enemy_speed_horizontal *= 1.1
            self.enemy_speed_vertical *= 1.1
            self.score += 100

    def wall_collision(self):
        if self.WIDTH <= self.x:
            self.x = 0 - self.rec_width
        elif self.HEIGHT <= self.y:
            self.y = 0 - self.rec_height + self.info_bar_height
        elif 0 - self.rec_width >= self.x:
            self.x = self.WIDTH
        elif 0 - self.rec_height + self.info_bar_height >= self.y:
            self.y = self.HEIGHT

    def enemy_collision(self):
        collide = self.player.colliderect(self.enemy)
        if collide:
            self.reset()

    def reset(self):
        self.x = 0
        self.enemy_x = self.WIDTH - self.enemy_width
        self.coin_x = self.WIDTH / 2

        self.y = 0 + self.info_bar_height
        self.enemy_y = self.HEIGHT - self.enemy_height
        self.coin_y = self.HEIGHT / 2

        self.enemy_speed_horizontal = self.speed / 3
        self.enemy_speed_vertical = self.speed / 3

        self.score = 0

    def player_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

    def enemy_movement(self):
        self.enemy_x -= self.enemy_speed_horizontal
        self.enemy_y -= self.enemy_speed_vertical
        if self.enemy_x >= self.WIDTH - self.enemy_width:
            self.enemy_speed_horizontal = -self.enemy_speed_horizontal
        elif self.enemy_x <= 0:
            self.enemy_speed_horizontal = -self.enemy_speed_horizontal
        elif self.enemy_y >= self.HEIGHT - self.enemy_height:
            self.enemy_speed_vertical = -self.enemy_speed_vertical
        elif self.enemy_y <= 0 + self.info_bar_height:
            self.enemy_speed_vertical = -self.enemy_speed_vertical

    def stalker_movement(self):
        if self.x > self.stalker_x:
            self.stalker_x += self.stalker_speed
        elif self.x < self.stalker_x:
            self.stalker_x -= self.stalker_speed
        if self.y > self.stalker_y:
            self.stalker_y += self.stalker_speed
        elif self.y < self.stalker_y:
            self.stalker_y -= self.stalker_speed


    def main(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(self.FPS)
            print(clock.get_fps())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            game.draw_window(self)
        pygame.quit()

if __name__ == "__main__":
    g = game()
    g.main()