from tkinter import *
from tkinter import font
def fdgvdgf():
    root.destroy()
def hell0():
    print('здраствуй')
    btm.configure(font=('Script',10,'bold'))

root = Tk()
list_fonts = list(font.families())
print(list_fonts)
root.title('re')
root.geometry('50x50')
root['bg'] = 'white'
btn = Button(root, bg ='black', text='hi656derfgdgrfgdfgdtrfgcvd5rg6v45bevctrddv5cd',fg='white',font=('Fixedsys',100,'bold'),command = fdgvdgf)
btn.place(width = 250,height = 55, x = 5,y = 150)
btm = Button(root,bg="yellow", text= 'привет!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!',font=('Script',10),command = hell0)
btm.pack(expand = True, fill = X)
root.mainloop()
