import time
from tkinter import *


class RGB:
    def __init__(self):
        self.name = None
        self.RGB = "#ffffff"
        self.brightness = 100
        self.last_rgb = (0,0,0)
        self.id = canvas.create_oval(40, 40, 190, 190, width=2, fill=self.RGB)

    def set_color(self, color):
        #self.RGB = color
        self.RGB = to_rgb(to_hex(color))
        self.last_rgb = self.RGB
        #canvas.itemconfigure(self.id, fill=self.RGB)
        #to_hex(color)

    def get_color(self):
        color = canvas.itemcget(self.id, 'fill')
        return to_rgb(color)

    def set_brightness(self, bright):
        if bright >= 100:
            self.RGB = self.last_rgb
        elif bright <= 0:
            self.RGB = (0,0,0)
        else:
            #self.brightness = bright
            r, g, b = to_rgb(to_hex(self.RGB))
            lr, lg, lb = self.last_rgb
            print(lr, lg, lb)
            print(r, g, b)
            rgb = bright*lr/100, bright*lg/100, bright*lb/100
            self.RGB = tuple(map(int, rgb))
            print(self.RGB)

    def on(self):
        if self.get_color() == self.RGB:
            return
        r, g, b = to_rgb(to_hex(self.RGB))
        lr, lg, lb = self.get_color()
        if r > lr:
            lr += 1
        elif r < lr:
            lr -= 1
        if g > lg:
            lg += 1
        elif g < lg:
            lg -= 1
        if b > lb:
            lb += 1
        elif b < lb:
            lb -= 1
        canvas.itemconfigure(self.id, fill = to_hex((lr, lg ,lb)))


class Lamp(RGB):
    def __init__(self, name:str):
        super().__init__()
        self.name = name.lower()
        self.text = canvas.create_text(115, 115, text=self.name.title(), font=(None, 18))


class Sconce(RGB):
    def __init__(self, name):
        super().__init__()
        self.name = name.lower()
        canvas.move(self.id, 200, 0)
        self.text = canvas.create_text(315, 115, text=self.name.title(), font=(None, 18))


def inp():
    data = entry.get()
    commands = data.split(' ')
    if len(commands) < 3:
        return
    name, task, value = list(map(str.lower, commands))
    if name not in dicte:
        return
    if task == "цвет":
        dicte[name].set_color(value)
    if task == "яркость":
        dicte[name].set_brightness(int(value))


def to_hex(rgb):
    if type(rgb) is str:
        color = list(tk.winfo_rgb(rgb))
        for n , c in enumerate(color):
            color[n] = c // 257
        r, g , b = color
    else:
        r, g ,b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'


def to_rgb(hex):
    hex = hex[1:]
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))


dicte = {}


tk = Tk()
tk.geometry("660x400")
tk.title("smart home")
tk['bg'] = ('gray100')

entry = Entry(tk, width=50, font=(None, 16), justify="right")
entry.grid(row=0, column=0, sticky=E)
btn = Button(tk, text="Ввод", command=inp)
btn.grid(row=0, column=1, sticky=W)
canvas = Canvas(width=700, height=600)
canvas.grid(row=1, columnspan=2)


l = Lamp("Лампа")
s = Sconce("Бра")
dicte["лампа"] = l
dicte["бра"] = s
l.set_color("blue")
s.set_color("lime")


while True:
    tk.update()
    tk.update_idletasks()
    for lamp in dicte.values():
        lamp.on()
    time.sleep(0.01)




































































