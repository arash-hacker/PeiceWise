import pyglet
from pyglet.gl import gl
from pyglet.gl import*
from pyglet.window import Window
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
Config = pyglet.gl.Config(sample_buffers=1, samples=16,
                          double_buffer=True, stencil_size=8)


class MidPoint(object):
    def iterate(self):
        glViewport(-250, -150, 250, 150)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(-250.0, 250.0, -150.0, 150.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def showScreen(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        self.iterate()
        glColor3f(0.5, 1.0, 1.0)
        # self.draw_points(45,45)
        self.drawCircle(100)
        glutSwapBuffers()

    def drawCircle(self, r):
        x = r
        y = 0
        d = 1 - r
        self.draw8Way(x, y)
        while (y <= x):
            if (d < 0):
                d = d+(2 * y+3)
                y = y+1
            else:
                d = d+(2 * y-2 * x+5)
                x = x-1
                y = y+1
            print("x: ", x, " y: ", y)
            self.draw8Way(x, y)

    def draw8Way(self, x, y):
        glPointSize(5)
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glVertex2f(y, x)
        glVertex2f(-x, y)
        glVertex2f(-y, x)
        glVertex2f(-x, -y)
        glVertex2f(-y, -x)

        glVertex2f(x, -y)
        glVertex2f(y, -x)
        glEnd()

    def main_function(self):
        glutInit()
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(700, 700)  # window size
        #glutInitWindowPosition(0, 0)
        glutInitWindowPosition(100, 100)
        wind = glutCreateWindow(b"OpenGL Coding Practice")  # window name
        glutDisplayFunc(self.showScreen)
        glutMainLoop()


MidPoint().main_function()
