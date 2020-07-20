import pyglet
from pyglet.window import key
from RectangleCollision import collision

# Window
Window = pyglet.window.Window(caption='Platformer', width=600,height=600)
Window.set_location(Window.screen.width//2-Window.width//2, Window.screen.height//2-Window.height//2)
Window.set_icon(pyglet.image.load('logo.ico'))

# Key handler
KeyHandler = key.KeyStateHandler()
Window.push_handlers(KeyHandler)

# Object batch
ObjectBatch = pyglet.graphics.Batch()

# Objects
Player = pyglet.sprite.Sprite(pyglet.image.load('32x32-dark_green.png') ,x=100,y=200, batch=ObjectBatch)
PlayerOldPosX = 0
Block1 = pyglet.sprite.Sprite(pyglet.image.load('32x32-white.png') ,x=100,y=100, batch=ObjectBatch)
Block2 = pyglet.sprite.Sprite(pyglet.image.load('32x32-white.png') ,x=132,y=100, batch=ObjectBatch)
Block3 = pyglet.sprite.Sprite(pyglet.image.load('32x32-white.png') ,x=164,y=100, batch=ObjectBatch)
Block4 = pyglet.sprite.Sprite(pyglet.image.load('32x32-white.png') ,x=196,y=100, batch=ObjectBatch)
Block5 = pyglet.sprite.Sprite(pyglet.image.load('32x32-white.png') ,x=132,y=132, batch=ObjectBatch)
Block6 = pyglet.sprite.Sprite(pyglet.image.load('32x32-white.png') ,x=196,y=196, batch=ObjectBatch)
Jump = False

def BlockSolid(BlockX, BlockY):
    global Jump, PlayerOldPosX
    if collision.rectangle(Player.x,Player.y ,BlockX+5,BlockY+30 ,32,32 ,22,2):
        Player.y += 1
        if KeyHandler[key.W]:
            PlayerOldPosX = Player.y
            Jump = True
    if collision.rectangle(Player.x,Player.y+0.1 ,BlockX,BlockY ,32,32 ,32,2):
        Jump = False
    if collision.rectangle(Player.x,Player.y ,BlockX,BlockY+1 ,32,32 ,2,30):
        Player.x -= 1
    if collision.rectangle(Player.x,Player.y ,BlockX+30,BlockY+1 ,32,32 ,2,30):
        Player.x += 1


@Window.event()
def on_draw():
    # Clears the window
    Window.clear()
    # Draws all of the objects in the Object Batch
    ObjectBatch.draw()

def Update(dt):
    global Jump
    # Gravity
    Player.y -= 1
    if KeyHandler[key.A]: Player.x -= 1
    if KeyHandler[key.D]: Player.x += 1
    BlockSolid(Block1.x,Block1.y)
    BlockSolid(Block2.x,Block2.y)
    BlockSolid(Block3.x,Block3.y)
    BlockSolid(Block4.x,Block4.y)
    BlockSolid(Block5.x,Block5.y)
    BlockSolid(Block6.x,Block6.y)
    if Jump == True:
        Player.y += 3
        if Player.y >= PlayerOldPosX + 70: Jump = False

pyglet.clock.schedule_interval(Update, 1/120)
pyglet.app.run()