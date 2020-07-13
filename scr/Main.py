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
class Objects():
    # Player
    class Player():
        # Gravity
        Gravity = 2
        # Jumping
        Jumping = False
        # Old position Y
        OldPosY = 0
        # Image
        Image = pyglet.image.load('32x32-dark_green.png')
        # Sprite
        Sprite = pyglet.sprite.Sprite(Image, x=100,y=300, batch=ObjectBatch)
        # Direction
        Direction = ''
    # Block1
    class Block1():
        # Images
        Image = pyglet.image.load('32x32-white.png')

        # Sprites
        Sprite1 = pyglet.sprite.Sprite(Image, x=100,y=100, batch=ObjectBatch)
        Sprite2 = pyglet.sprite.Sprite(Image, x=132,y=100, batch=ObjectBatch)
        Sprite3 = pyglet.sprite.Sprite(Image, x=164,y=100, batch=ObjectBatch)
        Sprite4 = pyglet.sprite.Sprite(Image, x=196,y=100, batch=ObjectBatch)
        Sprite5 = pyglet.sprite.Sprite(Image, x=228,y=100, batch=ObjectBatch)
        Sprite6 = pyglet.sprite.Sprite(Image, x=260,y=100, batch=ObjectBatch)
        Sprite7 = pyglet.sprite.Sprite(Image, x=292,y=100, batch=ObjectBatch)
        Sprite8 = pyglet.sprite.Sprite(Image, x=324,y=100, batch=ObjectBatch)
        Sprite9 = pyglet.sprite.Sprite(Image, x=324,y=132, batch=ObjectBatch)
        Sprite10 = pyglet.sprite.Sprite(Image, x=260,y=198, batch=ObjectBatch)

    # Block1Solid
    def Block1Solid(obj1x,obj1y,obj2x,obj2y,obj1w,obj1h,obj2w,obj2h):
        if collision.rectangle(obj1x,obj1y-0.1 ,obj2x,obj2y ,obj1w,obj1h ,obj2w,obj2h):
            if KeyHandler[key.W]:
                Objects.Player.OldPosY = Objects.Player.Sprite.y
                Objects.Player.Jumping = True
            Objects.Player.Sprite.y += Objects.Player.Gravity

        if collision.rectangle(obj1x,obj1y ,obj2x-0.1,obj2y ,obj1w,obj1h ,obj2w+0.2,obj2h):
            if Objects.Player.Direction == 'left': Objects.Player.Sprite.x += 4
            if Objects.Player.Direction == 'right': Objects.Player.Sprite.x -= 4
        if collision.rectangle(obj1x,obj1y ,obj2x+2,obj2y ,obj1w,obj1h+0.1 ,obj2w-5,obj2h-31):
            Objects.Player.Sprite.y -= Objects.Player.Gravity
            Objects.Player.Jumping = False


# draw objects
@Window.event
def on_draw():
    # Clears the window
    Window.clear()
    # Draws the Objects in the batch
    ObjectBatch.draw()

# Update
def Update(dt):

    # Turn Block1 solid
    Objects.Block1Solid(Objects.Player.Sprite.x,Objects.Player.Sprite.y ,Objects.Block1.Sprite1.x,Objects.Block1.Sprite1.y, 32,32,32,32)
    Objects.Block1Solid(Objects.Player.Sprite.x,Objects.Player.Sprite.y ,Objects.Block1.Sprite2.x,Objects.Block1.Sprite2.y, 32,32,32,32)
    Objects.Block1Solid(Objects.Player.Sprite.x,Objects.Player.Sprite.y ,Objects.Block1.Sprite3.x,Objects.Block1.Sprite3.y, 32,32,32,32)
    Objects.Block1Solid(Objects.Player.Sprite.x,Objects.Player.Sprite.y ,Objects.Block1.Sprite4.x,Objects.Block1.Sprite4.y, 32,32,32,32)
    Objects.Block1Solid(Objects.Player.Sprite.x,Objects.Player.Sprite.y ,Objects.Block1.Sprite5.x,Objects.Block1.Sprite5.y, 32,32,32,32)
    Objects.Block1Solid(Objects.Player.Sprite.x,Objects.Player.Sprite.y ,Objects.Block1.Sprite6.x,Objects.Block1.Sprite6.y, 32,32,32,32)
    Objects.Block1Solid(Objects.Player.Sprite.x,Objects.Player.Sprite.y ,Objects.Block1.Sprite7.x,Objects.Block1.Sprite7.y, 32,32,32,32)
    Objects.Block1Solid(Objects.Player.Sprite.x,Objects.Player.Sprite.y ,Objects.Block1.Sprite8.x,Objects.Block1.Sprite8.y, 32,32,32,32)
    Objects.Block1Solid(Objects.Player.Sprite.x,Objects.Player.Sprite.y ,Objects.Block1.Sprite9.x,Objects.Block1.Sprite9.y, 32,32,32,32)
    Objects.Block1Solid(Objects.Player.Sprite.x,Objects.Player.Sprite.y ,Objects.Block1.Sprite10.x,Objects.Block1.Sprite10.y, 32,32,32,32)

    # Gravity for player
    Objects.Player.Sprite.y -= Objects.Player.Gravity
    # Movment
    if KeyHandler[key.A]:
        Objects.Player.Direction = 'left'
        Objects.Player.Sprite.x -= 4
    if KeyHandler[key.D]:
        Objects.Player.Direction = 'right'
        Objects.Player.Sprite.x += 4
    if Objects.Player.Jumping == True:
        Objects.Player.Sprite.y += Objects.Player.Gravity + 4
        if Objects.Player.Sprite.y == Objects.Player.OldPosY + 70:
            Objects.Player.Jumping = False


pyglet.clock.schedule_interval(Update, 1/120)
pyglet.app.run()