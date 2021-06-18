from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

win = Tk()
win.title("Yeet Shop")
geoX = 504
geoY = 500
win.geometry(str(geoX)+'x'+str(geoY))

class makeitem():
    def __init__(self, name, price):
        self.name = name
        self.price = int(price)

    def makecheckbox(self, var):
        var.set(False)
        self.name = Checkbutton(win, text=self.name+" - "+str(self.price)+"$", var=var)

    def place(self, posx, posy):
        self.name.place(x=posx, y=posy)

    def getprice(self, var):
        if var.get() == True:
            return self.price
        else:
            return 0

def ResetOrder():
    global chk_mb1, chk_mb2, chk_mb3, chk_kb1, chk_kb2, chk_kb3, chk_ms1, chk_ms2, chk_ms3, chk_mt1, chk_mt2, chk_mt3
    chk_mb1.set(False)
    chk_mb2.set(False)
    chk_mb3.set(False)
    chk_kb1.set(False)
    chk_kb2.set(False)
    chk_kb3.set(False)
    chk_ms1.set(False)
    chk_ms2.set(False)
    chk_ms3.set(False)
    chk_mt1.set(False)
    chk_mt2.set(False)
    chk_mt3.set(False)

def Order():
    global mb1, mb2, mb3, kb1, kb2, kb3, mt1, mt2, mt3, ms1, ms2, ms3, chk_mb1, chk_mb2, chk_mb3, chk_kb1, chk_kb2, chk_kb3, chk_ms1, chk_ms2, chk_ms3, chk_mt1, chk_mt2, chk_mt3
    cost = 0
    cost += mb1.getprice(chk_mb1)
    cost += mb2.getprice(chk_mb2)
    cost += mb3.getprice(chk_mb3)
    cost += kb1.getprice(chk_kb1)
    cost += kb2.getprice(chk_kb2)
    cost += kb3.getprice(chk_kb3)
    cost += mt1.getprice(chk_mt1)
    cost += mt2.getprice(chk_mt2)
    cost += mt3.getprice(chk_mt3)
    cost += ms1.getprice(chk_ms1)
    cost += ms2.getprice(chk_ms2)
    cost += ms3.getprice(chk_ms3)
    messagebox.showinfo("Complete!", "Your order has been completed!\nThe total price is "+str(cost)+"$")


def setup(f):
    global categories, reset, order, mb1, chk_mb1, mb2, chk_mb2, mb3, chk_mb3, kb1, chk_kb1, kb2, chk_kb2, kb3, chk_kb3, ms1, chk_ms1, ms2, chk_ms2, ms3, chk_ms3, mt1, chk_mt1, mt2, chk_mt2, mt3, chk_mt3
    if f == 0:
        categories = Combobox(win, font=("Comic Sans", 32))
        categories['values'] = ("Motherboards", "Keyboards", "Mouses", "Monitors")
        categories.current(0)
        reset = Button(win, text="Reset Order", command=ResetOrder)
        order = Button(win, text="Order", command=Order)
    elif f == 1:
        categories.place(x=0, y=0)
        reset.place(x=geoX-175, y=geoY-35)
        order.place(x=geoX-90, y=geoY-35)
    elif f == 2:
        mb1 = makeitem("Motherboard_1", 50)
        chk_mb1 = BooleanVar()
        mb1.makecheckbox(chk_mb1)
        mb2 = makeitem("Motherboard_2", 69)
        chk_mb2 = BooleanVar()
        mb2.makecheckbox(chk_mb2)
        mb3 = makeitem("Motherboard_3", 75)
        chk_mb3 = BooleanVar()
        mb3.makecheckbox(chk_mb3)
        kb1 = makeitem("Keyboards_1", 13)
        chk_kb1 = BooleanVar()
        kb1.makecheckbox(chk_kb1)
        kb2 = makeitem("Keyboards_2", 29)
        chk_kb2 = BooleanVar()
        kb2.makecheckbox(chk_kb2)
        kb3 = makeitem("Keyboards_3", 50)
        chk_kb3 = BooleanVar()
        kb3.makecheckbox(chk_kb3)
        ms1 = makeitem("Mouse_1", 6)
        chk_ms1 = BooleanVar()
        ms1.makecheckbox(chk_ms1)
        ms2 = makeitem("Mouse_2", 20)
        chk_ms2 = BooleanVar()
        ms2.makecheckbox(chk_ms2)
        ms3 = makeitem("Mouse_3", 49)
        chk_ms3 = BooleanVar()
        ms3.makecheckbox(chk_ms3)
        mt1 = makeitem("Monitor_1", 40)
        chk_mt1 = BooleanVar()
        mt1.makecheckbox(chk_mt1)
        mt2 = makeitem("Monitor_2", 60)
        chk_mt2 = BooleanVar()
        mt2.makecheckbox(chk_mt2)
        mt3 = makeitem("Monitor_3", 99)
        chk_mt3 = BooleanVar()
        mt3.makecheckbox(chk_mt3)

setup(0)
setup(1)
setup(2)

def ResetCheckButton():
    global mb1, mb2, mb3, kb1, kb2, kb3, mt1, mt2, mt3, ms1, ms2, ms3
    mb1.place(-100, -100)
    mb2.place(-100, -100)
    mb3.place(-100, -100)
    kb1.place(-100, -100)
    kb2.place(-100, -100)
    kb3.place(-100, -100)
    ms1.place(-100, -100)
    ms2.place(-100, -100)
    ms3.place(-100, -100)
    mt1.place(-100, -100)
    mt2.place(-100, -100)
    mt3.place(-100, -100)

def Select():
    global categories
    cat = categories.get()
    ResetCheckButton()
    if cat == "Motherboards":
        mb1.place(0*100+25, 0*20+70)
        mb2.place(0*100+25, 1*20+70)
        mb3.place(0*100+25, 2*20+70)
    elif cat == "Keyboards":
        kb1.place(0*100+25, 0*20+70)
        kb2.place(0*100+25, 1*20+70)
        kb3.place(0*100+25, 2*20+70)
    elif cat == "Mouses":
        ms1.place(0*100+25, 0*20+70)
        ms2.place(0*100+25, 1*20+70)
        ms3.place(0*100+25, 2*20+70)
    elif cat == "Monitors":
        mt1.place(0*100+25, 0*20+70)
        mt2.place(0*100+25, 1*20+70)
        mt3.place(0*100+25, 2*20+70)

def Mainloop():
    Select()
    win.after(100, Mainloop)

Mainloop()
win.mainloop()