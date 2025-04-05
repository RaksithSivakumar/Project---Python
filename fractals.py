import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def generate_fractal(xmin, xmax, ymin, ymax, width, height, max_iter):
    real_vals = np.linspace(xmin, xmax, width)
    imag_vals = np.linspace(ymin, ymax, height)
    fractal = np.zeros((height, width))
    
    for i, re in enumerate(real_vals):
        for j, im in enumerate(imag_vals):
            c = complex(re, im)
            fractal[j, i] = mandelbrot(c, max_iter)
    
    return fractal

xmin, xmax = -2.5, 1.5
ymin, ymax = -2.0, 2.0
width, height = 800, 800
max_iter = 256

fractal_data = generate_fractal(xmin, xmax, ymin, ymax, width, height, max_iter)

plt.figure(figsize=(10, 10))
plt.imshow(fractal_data, cmap='hot', extent=[xmin, xmax, ymin, ymax])
plt.colorbar()
plt.title('Mandelbrot Fractal Art')
plt.show()
