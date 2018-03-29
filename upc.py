"""Ilias Boujlil"""
"""3/28/2018"""
"""Section 002"""


import turtle
import barcode_utilities as bar

def start():
    t = turtle.Turtle()
    t.hideturtle()
    wn = turtle.Screen()
    WIDTH, HEIGHT = 500, 500
    wn.setup(WIDTH, HEIGHT)
    wn.tracer(0)
    module_width, module_height, short_module_height = 3, 200, 170
    total_width = (12 * 7 + 11) * (module_width + 1)
    font_size = (module_width + 1) * 9
    font = ("courier", font_size)
    print(total_width)
    start_x = -WIDTH // 2 + ((WIDTH - total_width) // 2)
    start_y = HEIGHT // 2 - module_height // 2

    valid = False
    prompt = 'Please enter a barcode number:'
    while(not valid):
        barcode_number = wn.textinput('barcode', prompt)
        valid = bar.valid_barcode(barcode_number)
        if not valid:
            prompt = 'THAT IS NOT A VALID BARCODE NUMBER!!!! :('
            prompt += '\n\nPlease enter another barcode number.'
    widths = bar.generate_bar_widths(barcode_number)

    #075678164125
    t.up()
    t.goto(start_x, start_y)
    black = True
    for i, n in enumerate(widths):
        print(n)
        color = '#000000' if black else '#ffffff'
        w, h = int(n) * module_width, module_height
        if i not in (0, 1, 2, 27, 28, 29, 30, 31, 56, 57, 58):
            h = short_module_height
        draw_rectangle(t, w, h, color=color)
        t.forward(w + 1)
        black = not black
    t.up()
    text_x = start_x + 3 * (module_width + 1) + font_size // 2
    text_y = start_y - module_height - font_size // 6
    t.goto(text_x, text_y)
    t.down()
    half_index = len(barcode_number) // 2
    t.write(barcode_number[:half_index], font=font)

    t.up()
    text_x = start_x + (6 * 7 + 8) * (module_width + 1)
    text_y = start_y - module_height - font_size // 6
    t.goto(text_x, text_y)
    t.down()
    t.write(barcode_number[half_index:], font=font)
    #t.write(barcode_number[:half_index], font="monospace 35")
    wn.update()

    wn.exitonclick()

def draw_rectangle(t, width, height, color='#000000'):
    t.setheading(0)
    t.down()
    t.color(color)
    t.begin_fill()
    for i in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

