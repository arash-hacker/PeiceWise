import pyglet
from pyglet.gl import *
from pyglet.window import Window

Config = pyglet.gl.Config(sample_buffers=2, samples=2,
                          double_buffer=True, stencil_size=4)
window = Window(800, 640, caption='Stencil Test Draw with mask', 
config=Config)


n=GL_NEVER	
a=GL_ALWAYS	
l=GL_LESS	
g=GL_GREATER
ge=GL_EQUAL	
e=GL_EQUAL	
le=	GL_NOTEQUAL

k=GL_KEEP	
inv=v=GL_INVERT
z=GL_ZERO	
r=GL_REPLACE	
i=GL_INCR
iw=GL_INCR_WRAP
d=GL_DECR	
dw=GL_DECR_WRAP


i=70
def on_draw(dt):
    global i
    print(i)
    window.clear()

    """ alpha blending """
    glEnable(gl.GL_BLEND)
    glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)

    """ Trying to smooth stencil Circle Mask """
    # glEnable(GL_SMOOTH)

    """Clear """
    glClearStencil(0)
    glEnable(GL_STENCIL_TEST)
    glDisable(GL_DEPTH_TEST)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT | GL_STENCIL_BUFFER_BIT); 

    glStencilFunc(GL_ALWAYS, 0, 1)
    glStencilOp(GL_INCR, GL_INCR, GL_INCR)
    glColor4f(1, 0, 0, 1.0)
    pyglet.graphics.draw(4, GL_QUADS, ('v2f', [250+i, 250+i, 250+i, 350+i, 350+i, 350+i, 350+i, 250+i]))
    pyglet.graphics.draw(4, GL_QUADS, ('v2f', [200,200, 200,350, 350,350, 350,200]))

    glStencilFunc(GL_EQUAL, 2, 1)
    glStencilOp(k,k,k)
    glColor4f(0, 0, 0, 1.0)
    pyglet.graphics.draw(4, GL_QUADS, ('v2f', [0,0, 0,800, 800,800, 800,0]))

    """ Remove stencil test """
    glDisable(GL_STENCIL_TEST)

pyglet.clock.schedule_interval(on_draw, 1/60)
pyglet.app.run()
