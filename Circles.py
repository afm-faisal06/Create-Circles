from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

WINDOW_WIDTH=600
WINDOW_HEIGHT=600

circles=[]
paused=False

# Mid Point Circle Algorithm
def Mid_Point_Circle(radius,x0,y0):
    d=1-radius
    x=0
    y=radius
    draw_circle_points(x,y,x0,y0)

    while x<y:
        if d<0:
            d=d+2*x+3
            x=x+1
        else:
            d=d+2*x-2*y+5
            x=x+1
            y=y-1

        draw_circle_points(x,y,x0,y0)


def draw_circle_points(x,y,x0,y0):
    glColor3f(1.0, 0.0,0.0)  # Red color
    glBegin(GL_POINTS)
    glVertex2f(x + x0, y + y0)
    glVertex2f(-x + x0, y + y0)
    glVertex2f(x + x0, -y + y0)
    glVertex2f(-x + x0, -y + y0)
    glVertex2f(y + x0, x + y0)
    glVertex2f(-y + x0, x + y0)
    glVertex2f(y + x0, -x + y0)
    glVertex2f(-y + x0, -x + y0)
    glEnd()


def draw_circles():
    for circle in circles:
        Mid_Point_Circle(circle['radius'],circle['x'],circle['y'])


def show_screen():
    global clickedX, clickedY, r
    # clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    draw_circles()
    glutSwapBuffers()


def circle_inside_display(circle):
    x, y, radius = circle['x'],circle['y'],circle['radius']
    return 0 <(x-radius) and (x+radius)< WINDOW_WIDTH and 0 <(y - radius) and (y+radius)< WINDOW_HEIGHT


def update_circles():
    for circle in circles:
        circle['radius']+=1

    # Check if any circle is out of display then remove it
    for circle in circles[:]:
        if not circle_inside_display(circle):
            circles.remove(circle)


def animation(value):
    global paused
    if paused==False:
        update_circles()
        glutPostRedisplay()
    glutTimerFunc(16,animation,0)
    

def mouse_click(button,state,x,y):
    global paused
    if button==GLUT_RIGHT_BUTTON and state==GLUT_DOWN and paused==False:
        circles.append({'x': x, 'y': WINDOW_HEIGHT - y, 'radius': 10})


def keyboard_click(key, x, y):
    global paused
    if key==b' ':
        if paused==False:
            paused=True
            print("Stop")
        else:
            paused=False
            print("Resume")


def initialize():
    glViewport(0,0,WINDOW_WIDTH,WINDOW_HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0,WINDOW_WIDTH,0,WINDOW_HEIGHT)
    glMatrixMode(GL_MODELVIEW)



glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(WINDOW_WIDTH,WINDOW_HEIGHT)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"Circles")

glClearColor(0.0,0.0,0.0,1.0)  # Black background
glutDisplayFunc(show_screen)
glutIdleFunc(glutPostRedisplay)
glutTimerFunc(0,animation,0)
glutMouseFunc(mouse_click)
glutKeyboardFunc(keyboard_click)
initialize()

glutMainLoop()
