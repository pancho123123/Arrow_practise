import pygame, random
from random import randint

WIDTH = 1200
HEIGHT = 700
BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (0, 255, 0)
RED = (255,0,0)
BLUE = (0,0,255)
BROWN = (50,20,30)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arrow Practise")
clock = pygame.time.Clock()

def draw_text1(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, WHITE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_text2(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, BLACK)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_hp_bar(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, GREEN, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

def draw_hp_bar2(surface, x, y, percentage):
	BAR_LENGHT = 70
	BAR_HEIGHT = 7
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BROWN, fill)
	pygame.draw.rect(surface, BROWN, border, 2)

def draw_mana_bar(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BLUE, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

def distance(a,b):
	#pitagoras distancia entre a y b
	dx = b.rect.centerx - a.rect.centerx
	dy = b.rect.centery - a.rect.centery
	return (dx**2 + dy**2)**(1/2)

def direction(a,b):
	#vector unitario desde a a b
	dx = b.rect.centerx - a.rect.centerx
	dy = b.rect.centery - a.rect.centery
	radio = (dx**2 + dy**2)**(1/2)
	return dx/radio, dy/radio

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/mirana.png").convert(),(50,65))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.speed_x = 0
		self.speed_y = 0
		self.hp = 100
		self.counter = True

	def update(self):
		self.speed_x = 0
		self.speed_y = 0
		self.rect.x += self.speed_x
		self.rect.y += self.speed_y
		if self.rect.right > 100:
			self.rect.right = 100
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 50:
			self.rect.top = 50
		if self.rect.bottom > 550:
			self.rect.bottom = 550


class Player1(Player):
	def __init__(self):
		super().__init__()
		self.rect.x = 100
		self.rect.y = 200
		
	def update(self):
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_a]:
			self.speed_x = -3
		if keystate[pygame.K_d]:
			self.speed_x = 3
		self.rect.x += self.speed_x
		if keystate[pygame.K_w]:
			self.speed_y = -3
		if keystate[pygame.K_s]:
			self.speed_y = 3
		self.rect.y += self.speed_y
		if self.rect.right > 200:
			self.rect.right = 200
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 50:
			self.rect.top = 50
		if self.rect.bottom > 550:
			self.rect.bottom = 550

	def shoot(self):
		arrow1 = Arrow1(self.rect.right, self.rect.centery)
		all_sprites.add(arrow1)
		arrows.add(arrow1)
		arrows1.add(arrow1)

class Player2(Player):
	def __init__(self):
		super().__init__()
		self.rect.x = 100
		self.rect.y = 300
				
	def update(self):
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speed_x = -3
		if keystate[pygame.K_RIGHT]:
			self.speed_x = 3
		self.rect.x += self.speed_x
		if keystate[pygame.K_UP]:
			self.speed_y = -3
		if keystate[pygame.K_DOWN]:
			self.speed_y = 3
		self.rect.y += self.speed_y
		if self.rect.right > 200:
			self.rect.right = 200
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 50:
			self.rect.top = 50
		if self.rect.bottom > 550:
			self.rect.bottom = 550

	def shoot(self):
		arrow2 = Arrow2(self.rect.right, self.rect.centery)
		all_sprites.add(arrow2)
		arrows.add(arrow2)
		arrows2.add(arrow2)

class Player3(Player):
	def __init__(self):
		super().__init__()
		self.rect.x = 100
		self.rect.y = 400
				
	def update(self):
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_f]:
			self.speed_x = -3
		if keystate[pygame.K_h]:
			self.speed_x = 3
		self.rect.x += self.speed_x
		if keystate[pygame.K_t]:
			self.speed_y = -3
		if keystate[pygame.K_g]:
			self.speed_y = 3
		self.rect.y += self.speed_y
		if self.rect.right > 200:
			self.rect.right = 200
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 50:
			self.rect.top = 50
		if self.rect.bottom > 550:
			self.rect.bottom = 550

	def shoot(self):
		arrow3 = Arrow3(self.rect.right, self.rect.centery)
		all_sprites.add(arrow3)
		arrows.add(arrow3)
		arrows3.add(arrow3)

class Player4(Player):
	def __init__(self):
		super().__init__()
		self.rect.x = 100
		self.rect.y = 500
				
	def update(self):
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_j]:
			self.speed_x = -3
		if keystate[pygame.K_l]:
			self.speed_x = 3
		self.rect.x += self.speed_x
		if keystate[pygame.K_i]:
			self.speed_y = -3
		if keystate[pygame.K_k]:
			self.speed_y = 3
		self.rect.y += self.speed_y
		if self.rect.right > 200:
			self.rect.right = 200
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 50:
			self.rect.top = 50
		if self.rect.bottom > 550:
			self.rect.bottom = 550

	def shoot(self):
		arrow4 = Arrow4(self.rect.right, self.rect.centery)
		all_sprites.add(arrow4)
		arrows.add(arrow4)
		arrows4.add(arrow4)

class Arrow(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/arrow.png").convert(),(75,25))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centery = y
		self.rect.centerx = x
		self.speedx = 10

	def update(self):
		self.rect.x += self.speedx
		if self.rect.left > 1300:
			self.kill()

class Arrow1(Arrow):
	def __init__(self, x , y):
		super().__init__(x, y)
		
class Arrow2(Arrow):
	def __init__(self, x, y):
		super().__init__(x, y)
		
class Arrow3(Arrow):
	def __init__(self, x, y):
		super().__init__(x, y)
		
class Arrow4(Arrow):
	def __init__(self, x, y):
		super().__init__(x, y)
		
class Penguin(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/penguin.png").convert(),(65,65))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(300,1000)
		self.rect.y = random.randrange(200,650)
		self.speedx = randint(-1,1)
		self.speedy = randint(-1,1)
		self.hp = 100
		self.a = randint(1000,3000)
		self.b = randint(1000,3000)
		self.counter1 = True
		self.counter2 = False
		self.counter3 = False
		self.start_time = pygame.time.get_ticks()
		
	def update(self):
		current_time = pygame.time.get_ticks()
		elapsed_time = current_time - self.start_time
		alist = [-1,1]
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 300:
			self.rect.left = 300
		if self.rect.top < 200:
			self.rect.top = 200
		if self.rect.bottom > 600:
			self.rect.bottom = 600
		if self.counter1:
			self.counter1 = False
			self.counter2 = True
			self.a = randint(1000,3000)
			self.b = randint(1000,3000)
			self.start_time = pygame.time.get_ticks()

		elif self.counter2:
			if elapsed_time >= self.a:
				self.counter2 = False
				self.speedx = random.choice(alist)
				self.speedy = random.choice(alist)
				self.counter3 = True
				self.start_time = pygame.time.get_ticks()
		elif self.counter3:
			if elapsed_time >= self.b:
				self.counter3 = False
				self.speedx = 0
				self.speedy = 0
				self.counter1 = True
				self.start_time = pygame.time.get_ticks()

class Bell1(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/bell1.png").convert(),(80,80))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 1120
		self.rect.y = 260

class Bell2(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/bell2.png").convert(),(80,80))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 1120
		self.rect.y = 360

class Bell3(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/bell3.png").convert(),(80,80))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 1120
		self.rect.y = 460


def show_go_screen():
	
	screen.fill(BLACK)
	draw_text1(screen, "Arrow Practise", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Shoot the bells", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)
	
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False


def show_game_over_screenp1():
	screen.fill(BLACK)
	draw_text1(screen, "Player 1 WINS", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)

	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

def show_game_over_screenp2():
	screen.fill(BLACK)
	draw_text1(screen, "Player 2 WINS", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)

	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

def show_game_over_screenp3():
	screen.fill(BLACK)
	draw_text1(screen, "Player 3 WINS", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)

	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

def show_game_over_screenp4():
	screen.fill(BLACK)
	draw_text1(screen, "Player 4 WINS", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)

	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

background = pygame.transform.scale(pygame.image.load("img/fond.png").convert(), (1300,700))

game_over1 = False
game_over2 = False
game_over3 = False
game_over4 = False
running = True
start = True
while running:
	if game_over1:
		show_game_over_screenp1()
				
		screen.blit(background,(0,0))
		game_over1 = False
		
		all_sprites = pygame.sprite.Group()
		arrows1 = pygame.sprite.Group()
		arrows2 = pygame.sprite.Group()
		arrows3 = pygame.sprite.Group()
		arrows4 = pygame.sprite.Group()
		arrows = pygame.sprite.Group()
		bell1 = Bell1()
		bell2 = Bell2()
		bell3 = Bell3()
		all_sprites.add(bell1, bell2, bell3)
		penguins = [Penguin() for _ in range(20)]

		all_sprites.add(*penguins)
		player1 = Player1()
		player2 = Player2()
		player3 = Player3()
		player4 = Player4()
		all_sprites.add(player1, player2, player3, player4)
		
		start_time = pygame.time.get_ticks()
		
	if game_over2:
		show_game_over_screenp2()
				
		screen.blit(background,(0,0))
		game_over2 = False
		all_sprites = pygame.sprite.Group()
		arrows1 = pygame.sprite.Group()
		arrows2 = pygame.sprite.Group()
		arrows3 = pygame.sprite.Group()
		arrows4 = pygame.sprite.Group()
		arrows = pygame.sprite.Group()
		bell1 = Bell1()
		bell2 = Bell2()
		bell3 = Bell3()
		all_sprites.add(bell1, bell2, bell3)
		penguins = [Penguin() for _ in range(20)]

		all_sprites.add(*penguins)
		player1 = Player1()
		player2 = Player2()
		player3 = Player3()
		player4 = Player4()
		all_sprites.add(player1, player2, player3, player4)
		
		start_time = pygame.time.get_ticks()
		
	if game_over3:
		show_game_over_screenp3()
				
		screen.blit(background,(0,0))
		game_over3 = False
		all_sprites = pygame.sprite.Group()
		arrows1 = pygame.sprite.Group()
		arrows2 = pygame.sprite.Group()
		arrows3 = pygame.sprite.Group()
		arrows4 = pygame.sprite.Group()
		arrows = pygame.sprite.Group()
		bell1 = Bell1()
		bell2 = Bell2()
		bell3 = Bell3()
		all_sprites.add(bell1, bell2, bell3)
		penguins = [Penguin() for _ in range(20)]

		all_sprites.add(*penguins)
		player1 = Player1()
		player2 = Player2()
		player3 = Player3()
		player4 = Player4()
		all_sprites.add(player1, player2, player3, player4)
		
		start_time = pygame.time.get_ticks()
		
	if game_over4:
		show_game_over_screenp4()
				
		screen.blit(background,(0,0))
		game_over4 = False
		all_sprites = pygame.sprite.Group()
		arrows1 = pygame.sprite.Group()
		arrows2 = pygame.sprite.Group()
		arrows3 = pygame.sprite.Group()
		arrows4 = pygame.sprite.Group()
		arrows = pygame.sprite.Group()
		bell1 = Bell1()
		bell2 = Bell2()
		bell3 = Bell3()
		all_sprites.add(bell1, bell2, bell3)
		penguins = [Penguin() for _ in range(20)]

		all_sprites.add(*penguins)
		player1 = Player1()
		player2 = Player2()
		player3 = Player3()
		player4 = Player4()
		all_sprites.add(player1, player2, player3, player4)
		
		start_time = pygame.time.get_ticks()
		
	if start:
		show_go_screen()
		
		start = False
				
		screen.blit(background,(0,0))
		all_sprites = pygame.sprite.Group()
		arrows1 = pygame.sprite.Group()
		arrows2 = pygame.sprite.Group()
		arrows3 = pygame.sprite.Group()
		arrows4 = pygame.sprite.Group()
		arrows = pygame.sprite.Group()
		bell1 = Bell1()
		bell2 = Bell2()
		bell3 = Bell3()
		all_sprites.add(bell1, bell2, bell3)
		penguins = [Penguin() for _ in range(20)]

		all_sprites.add(*penguins)
		player1 = Player1()
		player2 = Player2()
		player3 = Player3()
		player4 = Player4()
		all_sprites.add(player1, player2, player3, player4)
				
		start_time = pygame.time.get_ticks()
	
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_e:
				if len(arrows1) == 0:
					player1.shoot()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_p:
				if len(arrows2) == 0:
					player2.shoot()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_y:
				if len(arrows3) == 0:
					player3.shoot()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_o:
				if len(arrows4) == 0:
					player4.shoot()

		
	now = (pygame.time.get_ticks() - start_time)//1000
		
	all_sprites.update()

	# Checar colisiones - penguin1 - arrow
	for penguin in penguins:
		for arrow in arrows:
			if pygame.sprite.collide_rect(penguin, arrow):
				if penguin.hp > 0:
					penguin.hp -= 20
					arrow.kill()
		
	# Checar colisiones - bell1 - arrow1
	hits = pygame.sprite.spritecollide(bell1, arrows1, True)
	for hit in hits:
		game_over1 = True
		
	# Checar colisiones - bell1 - arrow2
	hits = pygame.sprite.spritecollide(bell1, arrows2, True)
	for hit in hits:
		game_over2 = True
		
	# Checar colisiones - bell1 - arrow3
	hits = pygame.sprite.spritecollide(bell1, arrows3, True)
	for hit in hits:
		game_over3 = True
		
	# Checar colisiones - bell1 - arrow4
	hits = pygame.sprite.spritecollide(bell1, arrows4, True)
	for hit in hits:
		game_over4 = True

	# Checar colisiones - bell2 - arrow1
	hits = pygame.sprite.spritecollide(bell2, arrows1, True)
	for hit in hits:
		game_over1 = True
		
	# Checar colisiones - bell2 - arrow2
	hits = pygame.sprite.spritecollide(bell2, arrows2, True)
	for hit in hits:
		game_over2 = True
		
	# Checar colisiones - bell2 - arrow3
	hits = pygame.sprite.spritecollide(bell2, arrows3, True)
	for hit in hits:
		game_over3 = True
		
	# Checar colisiones - bell2 - arrow4
	hits = pygame.sprite.spritecollide(bell2, arrows4, True)
	for hit in hits:
		game_over4 = True

	# Checar colisiones - bell3 - arrow1
	hits = pygame.sprite.spritecollide(bell3, arrows1, True)
	for hit in hits:
		game_over1 = True
		
	# Checar colisiones - bell3 - arrow2
	hits = pygame.sprite.spritecollide(bell3, arrows2, True)
	for hit in hits:
		game_over2 = True
		
	# Checar colisiones - bell3 - arrow3
	hits = pygame.sprite.spritecollide(bell3, arrows3, True)
	for hit in hits:
		game_over3 = True
		
	# Checar colisiones - bell3 - arrow4
	hits = pygame.sprite.spritecollide(bell3, arrows4, True)
	for hit in hits:
		game_over4 = True

	screen.blit(background, [0, 0])

	all_sprites.draw(screen)
	
	# Escudo.
	draw_text1(screen, "P1", 20, 110, 6)
	draw_text1(screen, "P2", 20, 400, 6)
	draw_text1(screen, "P3", 20, 700, 6)
	draw_text1(screen, "P4", 20, 1000, 6)

	draw_hp_bar(screen, 120, 5, player1.hp)
	draw_text2(screen, str(int(player1.hp)) + "/100", 10, 170, 6)

	draw_hp_bar(screen, 415, 5, player2.hp)
	draw_text2(screen, str(int(player2.hp))+ "/100", 10, 470, 6)

	draw_hp_bar(screen, 715, 5, player3.hp)
	draw_text2(screen, str(int(player3.hp))+ "/100", 10, 770, 6)

	draw_hp_bar(screen, 1015, 5, player4.hp)
	draw_text2(screen, str(int(player4.hp))+ "/100", 10, 1070, 6)

	for penguin in penguins:
		if penguin.hp > 0:
			draw_hp_bar2(screen, penguin.rect.x, penguin.rect.y, penguin.hp)

	#reloj
	draw_text1(screen, str((((pygame.time.get_ticks() - start_time)//60000)+(60))%(60))+":" + str((((pygame.time.get_ticks() - start_time)//1000)+(60))%(60)), 30, 570, 50)
		
	pygame.display.flip()
pygame.quit()