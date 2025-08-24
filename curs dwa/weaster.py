from tkinter import *
import requests
import tkintermapview



class WeatherApp:
    def __init__(self):
        self.master = Tk()
        self.master.title('Погода на карте')
        self.master.geometry('1000x700')
        self.api_key = '49db58d1f28a68f7f84dea6c7c6ab942'
        self.menu_bar = Menu(self.master)
        self.master.config(menu=self.menu_bar)
    def run(self):
        self.master.mainloop()








if __name__ == '__main__':
    app = WeatherApp()
    app.run()






















