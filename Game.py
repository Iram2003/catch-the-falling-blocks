from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# Window
WIDTH = 600
HEIGHT = 600

# Basket
basket_x = 250
basket_width = 100
basket_speed = 40   # faster movement

# Blocks
NUM_BLOCKS = 3
blocks = []

# Game state
score = 0
miss = 0
game_over = False
speed = 2   # constant speed

#  INIT BLOCKS 
def init_blocks():
    global blocks
    blocks = []
    for i in range(NUM_BLOCKS):
        blocks.append({
            "x": random.randint(0, WIDTH - 20),
            "y": HEIGHT + i * 150
        })

# TEXT FUNCTION
def draw_text(x, y, text):
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))

# BASKET 
def draw_basket():
    glColor3f(0, 1, 0)
    glBegin(GL_QUADS)
    glVertex2f(basket_x, 20)
    glVertex2f(basket_x + basket_width, 20)
    glVertex2f(basket_x + basket_width, 40)
    glVertex2f(basket_x, 40)
    glEnd()

# BLOCK 
def draw_block(x, y):
    glColor4f(1, 0, 0, 0.6)  # blending
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + 20, y - 20)
    glVertex2f(x + 20, y)
    glVertex2f(x, y - 20)
    glEnd()

#  DISPLAY FUNCTION
def display():
    glClear(GL_COLOR_BUFFER_BIT)

    draw_basket()

    for b in blocks:
        draw_block(b["x"], b["y"])

    glColor3f(1, 1, 1)
    draw_text(10, 570, f"Score: {score}")
    draw_text(450, 570, f"Miss: {miss}")

    if game_over:
        draw_text(220, 320, "GAME OVER")
        draw_text(200, 290, f"Final Score: {score}")
        draw_text(180, 260, "Press R to Restart")

    glutSwapBuffers()

# UPDATE 
def update(value):
    global score, miss, game_over

    if not game_over:
        for b in blocks:
            b["y"] -= speed   # constant speed

            if b["y"] <= 40:
                if basket_x < b["x"] < basket_x + basket_width:
                    score += 1
                else:
                    miss += 1

                b["y"] = HEIGHT
                b["x"] = random.randint(0, WIDTH - 20)

        if miss >= 3:
            game_over = True
            print("Game Over! Final Score:", score)

    glutPostRedisplay()
    glutTimerFunc(16, update, 0)

#  KEYBOARD INPUT FOR RESTART
def keyboard(key, x, y):
    global score, miss, game_over

    if key == b'r' or key == b'R':
        score = 0
        miss = 0
        game_over = False
        init_blocks()

# ARROW KEYS FOR BASKET MOVEMENT
def special_keys(key, x, y):
    global basket_x

    if game_over:
        return

    if key == GLUT_KEY_LEFT:
        basket_x -= basket_speed
    elif key == GLUT_KEY_RIGHT:
        basket_x += basket_speed

    if basket_x < 0:
        basket_x = 0
    if basket_x > WIDTH - basket_width:
        basket_x = WIDTH - basket_width

def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(0, WIDTH, 0, HEIGHT)

    # Blending for transparency
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

#  MAIN 
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(WIDTH, HEIGHT)
glutCreateWindow(b"Catch Game - Final Stable Version")

init()
init_blocks()

glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutSpecialFunc(special_keys)
glutTimerFunc(0, update, 0)
glutMainLoop()