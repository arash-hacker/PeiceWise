import pyglet
from pyglet.gl import gl
from pyglet.gl import*
from pyglet.window import Window

Config = pyglet.gl.Config(sample_buffers=1, samples=16,
                          double_buffer=True, stencil_size=8)
window = Window(800, 640, caption='Stencil Test Draw with mask', config=Config)


@window.event
def on_draw():
    window.clear()
    """ alpha blending """
    gl.glEnable(gl.GL_BLEND)
    gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)

    """ Trying to smooth stencil Circle Mask """
    # glEnable(GL_SMOOTH)

    """Clear """
    glClearStencil(0)
    glEnable(GL_STENCIL_TEST)
    glColorMask(GL_FALSE, GL_FALSE, GL_FALSE, GL_FALSE)
    glStencilFunc(GL_NEVER, 0, 1)
    glStencilOp(GL_INVERT, GL_INVERT, GL_INVERT)

    """ Draw Stencil Mask (I'm trying with a circle shape, but in this example I use rect) """
    glColor4f(1, 0, 0, 1.0)
    pyglet.graphics.draw(
        4, GL_QUADS, ('v2f', [250, 250, 250, 300, 300, 300, 300, 250]))

    """ Now, we want only the framebuffer to be updated if stencil value is 1 """
    """ Draw rectangle pixels only inside stencil mask """
    glColorMask(GL_TRUE, GL_TRUE, GL_TRUE, GL_TRUE)
    glStencilFunc(GL_EQUAL, 1, 1)
    glStencilOp(GL_ZERO, GL_ZERO, GL_ZERO)
    glColor4f(0.0, 1.0, 1.0, 1.0)
    pyglet.graphics.draw(
        4, GL_QUADS, ('v2f', [200, 200, 200, 350, 350, 350, 350, 200]))

    """ Remove stencil test """
    glDisable(GL_STENCIL_TEST)


pyglet.app.run()
