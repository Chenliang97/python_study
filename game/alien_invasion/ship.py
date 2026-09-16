import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	"""管理飞船的类"""

	def __init__(self,ai_game):
		"""初始化飞船并设置位置"""
		super().__init__()
		self.screen=ai_game.screen
		self.settings=ai_game.settings
		self.screen_rect=ai_game.screen.get_rect()

		#加载飞船图像
		self.image=pygame.image.load('images/ship2.bmp')
		self.rect=self.image.get_rect()

		#每艘新飞船都放在屏幕底部的中央
		self.rect.midbottom=self.screen_rect.midbottom

		self.x=float(self.rect.x)

		#移动标志
		self.moving_right=False
		self.moving_left=False

	def update(self):
		"""根据移动标志移动飞船"""
		#更新飞船属性x的值,不石外接矩形的x属性
		if (self.moving_right and self.rect.right <
			self.screen_rect.right):
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -=self.settings.ship_speed

		#根据self.x更新rect对象
		self.rect.x=self.x

	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image,self.rect)
	
	def center_ship(self):
		"""将飞船放在屏幕底部中央"""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)