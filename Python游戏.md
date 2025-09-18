---
title: https://www.pygame.org
since: 202508
---


## QuickStart

```
都是单个依赖
https://www.libhunt.com/compare-pygame-ce-vs-pygame
pip install pygame
pip install pygame-ce
python3 -m pip install -U pygame --user
sudo apt-get install python3-pygame

while True:
    events()
    loop()
    render()

------
import pygame

pygame.init() # 初始化pygame
screen = pygame.display.set_mode((400, 400)) # 创建一个400x400的窗口
pygame.display.set_caption("Pygame窗口") # 设置窗口标题

while True:
    for event in pygame.event.get(): # 获取用户事件
        if event.type == pygame.QUIT: # 如果事件为关闭窗口
            pygame.quit() # 退出pygame
```


## Example

https://pyga.me/docs/index.html
```
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
fpsClock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    # screen.fill("purple")
    screen.fill((60,25,60))

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()
    fpsClock.tick(60)  # limits FPS to 60

pygame.quit()
```


## 绘制按钮, 字体

https://thepythoncode.com/article/make-a-button-using-pygame-in-python
```
# font = pygame.font.SysFont(None, 20)
font = pygame.font.SysFont('arial', 20)
available_fonts = pygame.font.get_fonts()
print(available_fonts)

# 矩形区域
rect = pygame.Rect(300, 150+80*i,200,50)
pygame.draw.rect(screen, GRAY, rect)

# 文字居中
text_surface = font.render('Click', True, (255,0,0))
text_dest = text_surface.get_rect(center = rect.center)
screen.blit(text_surface, text_dest)
```


## 绘制网格
```
网格黑色
def render_board(w, h, size):
    for x in range(0, w, size):
        pygame.draw.line(screen, (0,0,0), (x,0), (x,h))
    for y in range(0, h, size):
        pygame.draw.line(screen, (0,0,0), (0,y), (w,y))


背景白色
screen.fill((255,255,255))
render_board(400, 400, 50)
```


## 绘制 Sprite 位图

https://www.cnblogs.com/liming19680104/p/13255064.html
```
class Block(pygame.sprite.Sprite):
   def __init__(self, color):
      super().__init__()
      self.image = pygame.Surface([50, 50]) #创建一个 50*50 的图像
      self.image.fill(color)
      self.rect = self.image.get_rect()

all_sprites_list = pygame.sprite.Group()

红色方块
player = Block((255,   0,   0)) 
all_sprites_list.add(player)

修改位置,跟随鼠标
player.rect.x = random.randrange(400)
player.rect.y = random.randrange(400)
pos = pygame.mouse.get_pos()  #获取鼠标位置
player.rect.x = pos[0]
player.rect.y = pos[1]

点击事件
if event.type == pygame.MOUSEBUTTONDOWN:
    pos = pygame.mouse.get_pos()
    if player.rect.collidepoint(pos):  # Rect对象，判断一个点是否在Rect内部
        print("Click ")

全部绘制
all_sprites_list.draw(screen)
```


## 设计模式 State Pattern
```
status = 0, 1, x 不同图像

有限状态机，状态转移
* 行为不同
* 页面不同

import enum
class StateEnum(enum.Enum):
  H = 1
  L = 0
  DISMISS = 10
  
  
if staus == StateEnum.H:

https://hot.dawoai.com/posts/2025/python-status-pattern-principle-and-practice-tutorial
class StateH(State):
	def next(self, context):
		context.state = StateL()
		
class StateL(State):
	def next(self, context):
		context.state = StateH()
		
class Context:
	def __init__(self):
		self.state = StateL()
	
	def click_next():
		self.state.next(self)
		
Context()
ctx.click_next()
ctx.click_next()
```


## 参考

https://developer.baidu.com/article/details/2803401

https://gamedevacademy.org/pygame-draw-text-tutorial-complete-guide/

https://www.geeksforgeeks.org/python/python-display-text-to-pygame-window/ 


