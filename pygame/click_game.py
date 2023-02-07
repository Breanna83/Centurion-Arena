mago = Actor('character')
mago.pos = 100,50

WIDTH = 500
HEIGHT = mago.height + 20

def draw():
    screen.clear
    screen.fill((255 , 255 , 255))
    mago.draw()

def update():
    mago.left = mago.left + 2
    if mago.left > WIDTH:
        mago.right = 0
