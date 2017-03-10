import pygame
import random
import gamemode
import spaceship
import starfield
import enemy
import explosion
import fragment
import ammobar
import score
import powerup
import pirate
import soundmanager
from constants import *

class PlayMode(gamemode.GameMode):
    """ Play Mode """

    def __init__(self, screen, game, message="Play Mode", fps=60):
        super().__init__(screen, game, message, fps)
#1
        self.name = "PlayMode"
        self.game_over = False
        self.mode_exit_delay = 5 * fps # seconds * fps=60

        # Sprites and Spritelists
        self.player = None
        self.all_sprites_list = None
        self.enemy_sprite_list = None
        self.enemy_sprite_hit_list = None
        self.phaser_sprite_list = None
        self.ammo_bar = None
        self.starfield = None
        self.scorefield = None
        self.hiscorefield = None
        self.ammo_power_up = None
        self.pirate = None
        self.time_to_power_up = 30000  # milliseconds
        self.power_up_event = pygame.USEREVENT + 1
        self.power_up_sprite_list = None
        self.pirate_coming_event = pygame.USEREVENT + 2
        self.pirate_sprite_list = None
        self.pirate_sprite_hit_list = None
        self.sm = soundmanager.SoundManager()
        #self.starfield = starfield.Starfield(self.screen, 250, 2)
        # self.sm = soundmanager.SoundManager()
    def enter(self):
        """ enter mode """
        self.active = True # Playmode active

        pygame.time.set_timer(self.power_up_event, self.time_to_power_up)
        pygame.time.set_timer(self.pirate_coming_event, self.time_to_power_up // 3)
        # populate world with objects
        # Sprites and Spritelists
        self.player = spaceship.SpaceShip(self.screen, 320, 400)
        self.ammo_bar = ammobar.AmmoBar(self.screen, 680, 20)
        self.all_sprites_list = pygame.sprite.Group(self.player, self.ammo_bar)
        self.enemy_sprite_list = pygame.sprite.Group()
        self.enemy_sprite_hit_list = pygame.sprite.Group()
        self.phaser_sprite_list = pygame.sprite.Group()
        self.scorefield = score.Score(self.screen, self.screen.get_width() // 2, 20)
        self.hiscorefield = score.HiScore(self.screen, self.screen.get_width() // 3, 20)
        self.all_sprites_list.add(self.scorefield)
        self.all_sprites_list.add(self.hiscorefield)
        self.starfield = starfield.Starfield(self.screen, 250, 2)
        # self.shoot_sound = self.sm.load_sound("laser5.ogg")
        self.ammo_power_up = powerup.PowerUpAmmo(self.screen, random.randrange(0, self.screen.get_width()), -10)
        self.power_up_sprite_list = pygame.sprite.Group(self.ammo_power_up)
        self.pirate_sprite_hit_list = pygame.sprite.Group()
        self.pirate_sprite_list = pygame.sprite.Group()
        self.sm.play_ambient('RocknRollLoop.wav', 0.3)

        # create 1st enemy wave
        for i in range(50):
            x = random.randrange(self.scr_w)
            y = random.randrange(self.scr_h / 2)
            tmp_enemy = enemy.Enemy(self.screen, x, y)
            if random.randint(0, 1) == 0:
                tmp_dir = -1
            else:
                tmp_dir = 1
            tmp_enemy.direction = tmp_dir
            tmp_enemy.speed = random.randint(1, 2)
            self.all_sprites_list.add(tmp_enemy)
            self.enemy_sprite_list.add(tmp_enemy)

    def exit(self):
        self.active = False
        self.game_over = False
        self.sm.stop_ambient()
        self.mode_exit_delay = 5 * self.fps

        #time.sleep(5)
    def _generate_enemy_wave(self, level=1):
        for i in range(50):
            x = random.randrange(self.scr_w)
            #y = random.randrange(self.scr_h / 2)
            y = random.randrange(0, 300)
            tmp_enemy = enemy.Enemy(self.screen, x, y)
            tmp_enemy.change_speed(level)
            if random.randint(0, 1) == 0:
                tmp_dir = -1
            else:
                tmp_dir = 1
            tmp_enemy.direction = tmp_dir
            tmp_enemy.speed = random.randint(1, level)
            self.all_sprites_list.add(tmp_enemy)
            self.enemy_sprite_list.add(tmp_enemy)


    def update(self):

        self.ammo_bar.ammo_stock = self.player.ammo_stock

        for a_phaser in self.phaser_sprite_list:
            self.enemy_sprite_hit_list = pygame.sprite.spritecollide(a_phaser, self.enemy_sprite_list, True)
            self.pirate_sprite_hit_list = pygame.sprite.spritecollide(a_phaser, self. pirate_sprite_list, True)
            # add something to score

            # if hit_list had some elememt then also kill the corresponding bullet/phaser
            if self.enemy_sprite_hit_list or self.pirate_sprite_hit_list:
                a_phaser.kill()
                for a_enemy in self.enemy_sprite_hit_list:
                    for _ in range(random.randint(3, 15)):
                        self.all_sprites_list.add(fragment.Fragment(self.screen, a_enemy.rect.centerx, a_enemy.rect.centery))
                    self.scorefield.score += 50
                for pirate in self.pirate_sprite_hit_list:
                    my_explosion = explosion.Explosion(self.screen, self.pirate.rect.centerx, self.pirate.rect.centery)
                    my_explosion.explode()
                    self.all_sprites_list.add(my_explosion)
                    self.scorefield.score += 500



        self.power_up_hit_list = pygame.sprite.spritecollide(self.player, self.power_up_sprite_list, True)
        for powerup in self.power_up_hit_list:
            if self.player.ammo_stock < (AMMO_STOCK_MAX - 20):
                self.player.ammo_stock += 20
            else:
                self.player.ammo_stock = AMMO_STOCK_MAX


        if not self.game_over:
            player_hit = pygame.sprite.spritecollideany(self.player, self.enemy_sprite_list)
            if player_hit:
                self.player.hit = True

            for pirate in self.pirate_sprite_list:
                if pygame.sprite.collide_rect(self.player, pirate):
                    my_explosion = explosion.Explosion(self.screen, self.pirate.rect.centerx,
                                                       self.pirate.rect.centery)
                    my_explosion.explode()
                    self.all_sprites_list.add(my_explosion)
                    pirate.kill()
                    self.player.hit = True
#1
            if self.player.hit:
                #self.player.hit = True
                self.player.dead = True
                my_explosion = explosion.Explosion(self.screen, self.player.rect.centerx, self.player.rect.centery)
                my_explosion.explode()
                self.all_sprites_list.add(my_explosion)


                # game over
                self.game_over = True
                # save hi score if any
                if self.scorefield.score > self.hiscorefield.score:
                    self.hiscorefield.score = self.scorefield.score
                    self.hiscorefield.save_hiscore_file()
                # removes player sprite from all groups
                self.player.kill()
            elif len(self.enemy_sprite_list) == 0:
                #self.game_over = True
                self._generate_enemy_wave(6)



        else:
            if self.mode_exit_delay > 0:
                self.mode_exit_delay -= 1
            else:
                self.exit()


        self.all_sprites_list.update()
        self.starfield.update()

    def draw_frame(self):
        self.screen.fill([0, 0, 0])
        self.starfield.draw()
        self.all_sprites_list.draw(self.screen)
        pygame.display.update()

    def handle_events(self):
        """ processing event Loop """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.change_speed(-3, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.change_speed(3, 0)
                elif event.key == pygame.K_UP:
                    self.player.change_speed(0, -3)
                elif event.key == pygame.K_DOWN:
                    self.player.change_speed(0, 3)
                elif event.key == pygame.K_SPACE:
                    # shoot phaser
                    # self.shoot_sound.play()
                    tmp_phaser = self.player.shoot()
                    if tmp_phaser:
                        self.phaser_sprite_list.add(tmp_phaser)
                        self.all_sprites_list.add(tmp_phaser)
                #elif event.key == pygame.K_r:
                    #if self.game_over:
                      #  self.game_over == False
                     #   self.__init__(self.screen)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.change_speed(3, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.change_speed(-3, 0)
                elif event.key == pygame.K_UP:
                     self.player.change_speed(0, 3)
                elif event.key == pygame.K_DOWN:
                    self.player.change_speed(0, -3)
            if event.type == self.power_up_event:
                self.ammo_power_up = powerup.PowerUpAmmo(self.screen, random.randrange(0+64, self.screen.get_width()-64), -100)
                self.all_sprites_list.add(self.ammo_power_up)
                self.power_up_sprite_list.add(self.ammo_power_up)
            if event.type == self.pirate_coming_event:
                if random.randint(0,1):
                    self.pirate = pirate.Pirate(self.screen, -50, random.randrange(0, self.screen.get_height()))
                    self.pirate.speed = random.randint(1,10)
                else:
                    self.pirate = pirate.Pirate(self.screen, self.screen.get_width() + 100, random.randrange(0, self.screen.get_height()))
                    self.pirate.speed = random.randint(1, 10)
                self.all_sprites_list.add(self.pirate)
                self.pirate_sprite_list.add(self.pirate)
        return False
