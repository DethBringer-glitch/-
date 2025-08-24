from tkinter import *
from tkinter.colorchooser import *
root = Tk()
root.geometry("660x400")
root.title("«Рисовалка»")
root['bg'] = ('gray100')
canvas = Canvas(root, width=1000, height=800, bg="white")
canvas.grid(row=0, column=0, rowspan=7)
state = "circle"
brush = 10
color = "red"
size = Label(root, text = brush, fg=color,
             font = (None, 36))
size.grid(row = 6, column = 1)
def choose(input):
    global state, brush
    if input == 'plus' and brush < 98:
        brush += 2
        size.configure(text=brush)
        return
    elif input == ('minus') and brush > 0:
        brush -= 2
        size.configure(text=brush)
    state = input
def paint(event):
    if event.widget.__class__ is not Canvas:
        return
    if state == "circle":
        canvas.create_oval(event.x - brush,  # Координата x1
            event.y - brush,  # Координата y1
            event.x + brush,  # Координата x2
            event.y + brush,  # Координата y2
            fill=color,  # Цвет заливки
            outline=color)  # Цвет обводки
    elif state == "square":
        canvas.create_rectangle(event.x - brush,
            event.y - brush,
            event.x + brush, event.y + brush,
            fill = color, outline = color)
    elif state == "line1":
        canvas.create_line(event.x - brush,
            event.y - brush,
            event.x + brush, event.y + brush, fill = color)

    elif state == "line2":
        canvas.create_line(event.x + brush,
            event.y - brush,
            event.x - brush, event.y + brush, fill = color)
    print(event.__dict__)
def ask_color(event):
    global color
    color_code = askcolor(title="Выбери цвет")
    color = color_code[1]
    size.configure(fg=color)
canvas.bind_all("<c>", ask_color)


def erase(event):
    canvas.create_oval(event.x - brush * 2, event.y - brush * 2,
        event.x + brush * 2, event.y + brush * 2,
        fill="white", outline="white")
root.bind_all("<3>", erase)
root.bind_all("<B3-Motion>", erase)

def clear(event):
    canvas.delete("all")
root.bind_all("<BackSpace>",clear)

root.bind_all('<1>', paint)
root.bind_all("<B1-Motion>", paint)
square_btn = Button(root, text = '🟥',font = (None, 20), command = lambda: choose('square'))
square_btn.grid(row=0, column=1)
circle_btn = Button(root, text="🔴", font=(None, 20), command=lambda: choose("circle"))
circle_btn.grid(row=1, column=1)
line1_btn = Button(root, text=" ↘ ", font=(None, 20), command=lambda: choose("line1"))
line1_btn.grid(row=2, column=1)
line2_btn = Button(root, text=" ↙ ", font=(None, 20), command=lambda: choose("line2"))
line2_btn.grid(row=3, column=1)
plus_btn = Button(root, text="➕", font=(None, 20), command=lambda: choose("plus"))
plus_btn.grid(row=4, column=1)
minus_btn = Button(root, text="➖", font=(None, 20), command=lambda: choose("minus"))
minus_btn.grid(row=5, column=1)















































































































































































































































root.mainloop()












































