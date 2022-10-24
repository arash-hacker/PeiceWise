from pyglet import window, gl, shapes, app
import pyglet
config = gl.Config(double_buffer=True, stencil_size=8)
win = window.Window(width=800, height=600, config=config)
fps_display = pyglet.window.FPSDisplay(window=win)
i = 0
j = 0


def update(dt):
    global i, j
    win.clear()
    gl.glEnable(gl.GL_STENCIL_TEST)
    gl.glStencilMask(gl.GL_TRUE)
    gl.glClearStencil(0)

    gl.glClear(gl.GL_STENCIL_BUFFER_BIT)
    gl.glStencilFunc(gl.GL_NEVER, 1, 0xFF)
    gl.glStencilOp(gl.GL_REPLACE, gl.GL_KEEP, gl.GL_KEEP)
    square = shapes.Rectangle(x=200, y=200, width=200,
                              height=200, color=(0, 0, 255))
    square.draw()
    gl.glStencilMask(gl.GL_FALSE)
    gl.glStencilFunc(gl.GL_GREATER, 1, 0xFF)
    square2 = shapes.Rectangle(
        x=150, y=150, width=200, height=200, color=(255, 0, 0))
    square2.draw()
    gl.glDisable(gl.GL_STENCIL_TEST)


pyglet.clock.schedule_interval(update, 1/60)


@win.event
def on_draw():
    win.clear()
    # batch.draw()
    fps_display.draw()


pyglet.app.run()
