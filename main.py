from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

rocketY = -200
rocketX = 0  

#  Bresenham Line 
def drawPixel(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def bresenhamLine(x1, y1, x2, y2):

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    err = dx - dy

    while True:

        drawPixel(x1, y1)

        if x1 == x2 and y1 == y2:
            break

        e2 = 2 * err

        if e2 > -dy:
            err -= dy
            x1 += sx

        if e2 < dx:
            err += dx
            y1 += sy

# Stars 
def drawStars():

    glPointSize(2)

    glBegin(GL_POINTS)

    stars = [
        (-200,200), (-150,150), (100,220),
        (200,180), (250,250), (-250,100),
        (50,150), (-100,250)
    ]

    for s in stars:
        glColor3f(1,1,1)
        glVertex2f(s[0], s[1])

    glEnd()

# - Smoke Blending----
def drawSmoke():

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glColor4f(0.8, 0.8, 0.8, 0.3)

    glPushMatrix()
    glTranslatef(rocketX, rocketY - 40, 0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(rocketX - 20, rocketY - 60, 0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(rocketX + 20, rocketY - 60, 0)
    glPopMatrix()

    glDisable(GL_BLEND)

# - Rocket 
def drawRocket():

    glPushMatrix()

    # Rocket position
    glTranslatef(rocketX, rocketY, 0)

    # Body shading
    glBegin(GL_POLYGON)

    glColor3f(0.9, 0.9, 0.9)
    glVertex2f(-20, -40)

    glColor3f(0.5, 0.5, 0.5)
    glVertex2f(20, -40)

    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(20, 40)

    glColor3f(0.7, 0.7, 0.7)
    glVertex2f(-20, 40)

    glEnd()

    # Nose
    glBegin(GL_TRIANGLES)

    glColor3f(1, 0, 0)
    glVertex2f(-20, 40)

    glColor3f(0.8, 0, 0)
    glVertex2f(20, 40)

    glColor3f(1, 0.3, 0.3)
    glVertex2f(0, 70)

    glEnd()

    # Left wing
    glColor3f(0, 0, 1)

    glBegin(GL_TRIANGLES)
    glVertex2f(-20, -20)
    glVertex2f(-40, -50)
    glVertex2f(-20, -50)
    glEnd()

    # Right wing
    glBegin(GL_TRIANGLES)
    glVertex2f(20, -20)
    glVertex2f(40, -50)
    glVertex2f(20, -50)
    glEnd()

    # Window
    glColor3f(0, 1, 1)

    glPushMatrix()
    glTranslatef(0, 10, 0)
    glPopMatrix()

    glPopMatrix()

# -- Display ----
def display():

    glClear(GL_COLOR_BUFFER_BIT)

    glLoadIdentity()

    drawStars()
    drawSmoke()
    drawRocket()

    glutSwapBuffers()

#- Animation -
def update(value):

    global rocketY

    rocketY += 2

    if rocketY > 300:
        rocketY = -200

    glutPostRedisplay()
    glutTimerFunc(20, update, 0)

#  Keyboard Arrow Keys -
def specialKeys(key, x, y):

    global rocketX

    # Left Arrow
    if key == GLUT_KEY_LEFT:
        rocketX -= 10

    # Right Arrow
    elif key == GLUT_KEY_RIGHT:
        rocketX += 10

    glutPostRedisplay()

# - Initialization -
def init():

    glClearColor(0, 0, 0, 1)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glShadeModel(GL_SMOOTH)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluOrtho2D(-300, 300, -300, 300)

    glMatrixMode(GL_MODELVIEW)

# -- Main -
glutInit()

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

glutInitWindowSize(700, 700)

glutCreateWindow(b"Rocket Launch Simulation")

init()

glutDisplayFunc(display)

# Arrow key event
glutSpecialFunc(specialKeys)

glutTimerFunc(0, update, 0)

glutMainLoop()