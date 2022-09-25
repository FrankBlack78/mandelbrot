from PIL import Image, ImageDraw
from mandelbrot import mandelbrot, MAX_ITER

# Image size (pixels)
WIDTH = 1920
HEIGHT = 1080

# # Plot window
# RE_START = -2
# RE_END = 1
# IM_START = -1
# IM_END = 1

# Plot window (Test)
RE_START = -1.9963822159164977
RE_END = -1.9963822159164644
IM_START = 3.585235356419038e-06
IM_END = 3.5852353365033377e-06

im = Image.new('HSV', (WIDTH, HEIGHT), (0, 0, 0))
draw = ImageDraw.Draw(im)

for x in range(0, WIDTH):
    for y in range(0, HEIGHT):
        # Convert pixel coordinate to complex number
        c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                    IM_START + (y / HEIGHT) * (IM_END - IM_START))
        # Compute the number of iterations
        m = mandelbrot(c)
        # The color depends on the number of iterations
        hue = int(255 * m / MAX_ITER)
        saturation = 255
        value = 255 if m < MAX_ITER else 0
        # Plot the point
        draw.point([x, y], (hue, saturation, value))

im.convert('RGB').save('output/output.png', 'PNG')
