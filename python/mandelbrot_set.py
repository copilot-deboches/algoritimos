import numpy as np


def create_mandelbrot(size, maxiter):
    """
    Create a mandelbrot set covering the given rectangle.

    The rectangle is defined by the characters x1, y1, x2, y2, where
    (x1, y1) are the coordinates of the top-left corner, and (x2, y2)
    are the coordinates of the bottom-right corner.

    The mandelbrot set is defined by the equation z_n = z_{n-1}**2 + c,
    where c is a constant.
    """
    x1, y1, x2, y2 = size
    dx = float(x2 - x1) / maxiter
    dy = float(y2 - y1) / maxiter
    x, y = np.mgrid[x1:x2 + dx:dx, y1:y2 + dy:dy]
    c = x + y * 1j
    z = np.zeros_like(c, dtype=np.complex128)
    for i in range(maxiter):
        z = z ** 2 + c
    return z
