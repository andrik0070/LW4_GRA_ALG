from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import sys
from pprint import pprint


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)

    glutInitWindowSize(800, 600)
    glutCreateWindow("OpenGL lesson 6")

    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutKeyboardFunc(processNormalKeys)
    glutSpecialFunc(processSpecialKeys)
    glutMainLoop()


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()
    glOrtho(-10, 10, -10, 10, -10, 10)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClearColor(1, 1, 1, 0)


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glPushMatrix()
    glLoadIdentity()
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 1)
    glVertex3f(-20, 0, 0.0)
    glVertex3f(20, 0, 0.0)

    # glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0, -500, 0.0)
    glVertex3f(0, 500, 0.0)
    #
    # # glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -500)
    glVertex3f(0.0, 0.0, 500)
    glEnd()
    glPopMatrix()
    glutWireTeapot(5)
    glutSwapBuffers()


def processNormalKeys(key, x, y):
    if key == b'\x1b':
        return sys.exit(0)


def processSpecialKeys(key, x, y):
    if key == GLUT_KEY_UP:
        glMatrixMode(GL_MODELVIEW)
        glTranslated(0, 1, 0)
        display()
    elif key == GLUT_KEY_DOWN:
        glMatrixMode(GL_MODELVIEW)
        glTranslated(0, -1, 0)
        display()
    elif GLUT_KEY_LEFT == key:
        glMatrixMode(GL_MODELVIEW)
        glTranslated(-1, 0, 0)
        display()
    elif GLUT_KEY_RIGHT == key:
        glMatrixMode(GL_MODELVIEW)
        glTranslated(1, 0, 0)
        display()
    elif GLUT_KEY_HOME == key:
        glMatrixMode(GL_MODELVIEW)
        glRotatef(30.0, 1.0, 0.0, 0)
        display_all()


main()
