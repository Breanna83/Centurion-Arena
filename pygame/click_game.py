mago = Actor('mago')
mago.pos = 100,50

WIDTH = 500
HEIGHT = mago.height + 20

def draw():
    screen.clear
    screen.fill((225, 225 , 225))
    mago.draw()

def update():
    mago.left = mago.left + 2
    if mago.left > WIDTH:
        mago.right = 0

def on_mouse_down(pos):
    if  mago.collidepoint(pos):
        print ("swag")
    else:
        print("no swag :/")
    if mago.collidepoint(pos):
        sounds.splat.play()
        mago.image='mago_click'
    if mago.collidepoint(pos):
        set_mago_click()

def set_mago_click():
    mago.image = 'mago_click'
    sounds.splat.play()

def set_mago_normal():
    mago.image = 'mago'

def set_mago_click():
    mago.image = 'mago_click'
    sounds.splat.play()
    clock.schedule_unique(set_mago_normal, 3.0)
