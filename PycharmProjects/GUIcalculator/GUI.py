def find_last_num(exp):
    n = len(exp)
    i = 1
    b = True
    if exp[-i] == ' ':
        b = False
    while -i >= -n and exp[-i] != ' ' and exp[-i] != '-':
        i += 1
    i -= 1
    return b, i, exp[-i:]


def commb1(event):
    global exp
    exp = ''
    conf = '0'
    entry.config(text=conf)


def commb2(event):
    global exp
    try:
        if exp[-1] == ' ':
            exp = exp[:-3]
        else:
            exp = exp[:-1]
        entry.config(text=exp)
    except:
        return


def commb21(event):
    global exp
    try:
        b, i, x = find_last_num(exp)
        exp = exp[:-i]
        conf = exp + '0'
        entry.config(text=conf)
    except:
        return


def trycomm3(i):
    try:
        if exp[-i] == '-':
            return 1
    except:
        return 0


def commb3(event):
    global exp
    b, i, x = find_last_num(exp)
    i += 1
    if trycomm3(i) == 1:
        exp = exp[:-i] + exp[-i + 1:]
    else:
        i -= 1
        if trycomm3(i) == 1:
            exp = exp[:-i] + exp[-i + 1:]
        else:
            exp = exp[:-i] + '-' + exp[-i:]
    entry.config(text=exp)


def commb4(event):
    global exp
    x = ''
    b, i, x = find_last_num(exp)
    if b:
        exp = exp[:-i]
        if x == '':
            return
        x = int(x)
        x = calc.divison(x)
        exp += str(x)
        entry.config(text=exp)


def commb5(event):
    global exp
    exp += '7'
    entry.config(text=exp)


def commb6(event):
    global exp
    exp += '8'
    entry.config(text=exp)


def commb7(event):
    global exp
    exp += '9'
    entry.config(text=exp)


def commb8(event):
    global exp
    exp += ' * '
    entry.config(text=exp)


def commb9(event):
    global exp
    exp += '4'
    entry.config(text=exp)


def commb10(event):
    global exp
    exp += '5'
    entry.config(text=exp)


def commb11(event):
    global exp
    exp += '6'
    entry.config(text=exp)


def commb12(event):
    global exp
    exp += ' / '
    entry.config(text=exp)


def commb13(event):
    global exp
    exp += '1'
    entry.config(text=exp)


def commb14(event):
    global exp
    exp += '2'
    entry.config(text=exp)


def commb15(event):
    global exp
    exp += '3'
    entry.config(text=exp)


def commb16(event):
    global exp
    exp += ' - '
    entry.config(text=exp)


def commb17(event):
    global exp
    exp += '0'
    entry.config(text=exp)


def commb18(event):
    global exp
    exp += '.'
    entry.config(text=exp)


def commb19(event):
    global exp
    x = calc.calculator(exp)
    exp = str(x)
    entry.config(text=exp)


def commb20(event):
    global exp
    exp += ' + '
    entry.config(text=exp)


def commb28(event):
    global exp
    exp += ' )'
    entry.config(text=exp)


def commb26(event):
    global exp
    exp += ' % '
    entry.config(text=exp)


def commb29(event):
    global exp
    exp += '( '
    entry.config(text=exp)


def commb30(event):
    global exp
    b, i, x = find_last_num(exp)
    if b:
        x = int(x)
        x = calc.muult(x, 3)
        exp = exp[:-i]
        exp += str(x)
        entry.config(text=exp)


def commb27(event):
    global exp
    b, i, x = find_last_num(exp)
    if b:
        x = int(x)
        x = calc.muult(x, 2)
        exp = exp[:-i]
        exp += str(x)
        entry.config(text=exp)


def commb221(event):
    global exp
    b, i, x = find_last_num(exp)
    if b:
        x = float(x)
        x = calc.sqrtx(x)
        exp = exp[:-i]
        intx = int(x)
        if intx == x:
            x = intx
        exp += str(x)
        entry.config(text=exp)


def commb22(event):
    global exp
    b, i, x = find_last_num(exp)
    if b:
        x = float(x)
        x = calc.fact(x)
        exp = exp[:-i]
        intx = int(x)
        if intx == x:
            x = intx
        exp += str(x)
        entry.config(text=exp)


def commb23(event):
    global exp
    exp += ' ^ '
    entry.config(text=exp)


def commb24(event):
    global exp
    b, i, x = find_last_num(exp)
    if b:
        x = float(x)
        x = calc.truncx(x)
        exp = exp[:-i]
        intx = int(x)
        if intx == x:
            x = intx
        exp += str(x)
        entry.config(text=exp)


def colorR():
    root.config(bg="Red")


def colorG():
    root.config(bg="Green")


def colorB():
    root.config(bg="Blue")


def colorY():
    root.config(bg="Yellow")


def colorBl():
    root.config(bg="Black")


def colorW():
    root.config(bg="White")


def colorRE():
    entry.config(bg="Red")


def colorGE():
    entry.config(bg="Green")


def colorBE():
    entry.config(bg="Blue")


def colorYE():
    entry.config(bg="Yellow")


def colorBlE():
    entry.config(bg="Black")


def colorWE():
    entry.config(bg="White")


def colorRF():
    entry.config(fg="Red")


def colorGF():
    entry.config(fg="Green")


def colorBF():
    entry.config(fg="Blue")


def colorYF():
    entry.config(fg="Yellow")


def colorBlF():
    entry.config(fg="Black")


def colorWF():
    entry.config(fg="White")


def colR1():
    entry.config(relief="flat")


def colR2():
    entry.config(relief="raised")


def colR3():
    entry.config(relief="sunken")


def colR4():
    entry.config(relief="groove")


def colR5():
    entry.config(relief="ridge")


def colR6():
    entry.config(relief="solid")


def colF1():
    entry.config(font="Tahoma")


def colF2():
    entry.config(font="Verdana")


def colF3():
    entry.config(font="Courier")


def colF4():
    entry.config(font="Times")


def colBR():
    bgconf("Red")


def colBG():
    bgconf("Green")


def colBB():
    bgconf("Blue")


def colBBl():
    bgconf("Black")


def colBY():
    bgconf("Yellow")


def colBW():
    bgconf("White")


def colFR():
    fgconf("Red")


def colFG():
    fgconf("Green")


def colFB():
    fgconf("Blue")


def colFBl():
    fgconf("Black")


def colFY():
    fgconf("Yellow")


def colFW():
    fgconf("White")


def relF():
    relconf("flat")


def relRa():
    relconf("raised")


def relS():
    relconf("sunken")


def relG():
    relconf("groove")


def relR():
    relconf("ridge")


def relSo():
    relconf("solid")


def about():
    global win2
    try:
        win2.destroy()
    except:
        vre = 0
    win2 = Toplevel(root, relief=SUNKEN, bg="lightblue")
    win2.title("About")
    win2.minsize(width=400, height=200)
    win2.maxsize(width=500, height=600)


def help1():
    global win1
    try:
        win1.destroy()
    except:
        vre = 0
    win1 = Toplevel(root, relief=SUNKEN, bg="lightblue")
    win1.title("Help")
    win1.minsize(width=400, height=200)
    win1.maxsize(width=500, height=600)


def exit1():
    root.destroy()
    exit()

    #        fra = Toplevel(root, width=300, height=100, bg="Black")


def menu():
    m = Menu(root)
    root.config(menu=m)

    Cm = Menu(m, relief='raised', tearoff=0)
    m.add_cascade(label="Custom", menu=Cm)

    cm = Menu(Cm, relief='raised', tearoff=0)
    Cm.add_cascade(label="Root color", menu=cm)

    cm.add_command(label="Red", command=colorR)
    cm.add_command(label="Green", command=colorG)
    cm.add_command(label="Blue", command=colorB)
    cm.add_command(label="Black", command=colorBl)
    cm.add_command(label="Yellow", command=colorY)
    cm.add_command(label="White", command=colorW)

    cm2 = Menu(Cm, relief='raised', tearoff=0)
    Cm.add_cascade(label='Label', menu=cm2)
    Sm1 = Menu(cm2, relief='raised', tearoff=0)
    cm2.add_cascade(label='Label color', menu=Sm1)
    Sm2 = Menu(cm2, relief='raised', tearoff=0)
    cm2.add_cascade(label='Font color', menu=Sm2)
    Sm3 = Menu(cm2, relief='raised', tearoff=0)
    cm2.add_cascade(label='Label relief', menu=Sm3)
    Sm4 = Menu(cm2, relief='raised', tearoff=0)
    cm2.add_cascade(label='Font', menu=Sm4)

    Sm1.add_command(label="Red", command=colorRE)
    Sm1.add_command(label="Green", command=colorGE)
    Sm1.add_command(label="Blue", command=colorBE)
    Sm1.add_command(label="Black", command=colorBlE)
    Sm1.add_command(label="Yellow", command=colorYE)
    Sm1.add_command(label="White", command=colorWE)

    Sm2.add_command(label="Red", command=colorRF)
    Sm2.add_command(label="Green", command=colorGF)
    Sm2.add_command(label="Blue", command=colorBF)
    Sm2.add_command(label="Black", command=colorBlF)
    Sm2.add_command(label="Yellow", command=colorYF)
    Sm2.add_command(label="White", command=colorWF)

    Sm3.add_command(label="Flat", command=colR1)
    Sm3.add_command(label="Raised", command=colR2)
    Sm3.add_command(label="Sunken", command=colR3)
    Sm3.add_command(label="Groove", command=colR4)
    Sm3.add_command(label="Ridge", command=colR5)
    Sm3.add_command(label="Solid", command=colR6)

    Sm4.add_command(label="Tahoma", command=colF1)
    Sm4.add_command(label="Verdana", command=colF2)
    Sm4.add_command(label="Courier", command=colF3)
    Sm4.add_command(label="Times", command=colF4)

    cm3 = Menu(Cm, relief='raised', tearoff=0)

    Cm.add_cascade(label='Buttons', menu=cm3)
    sm1 = Menu(cm3, relief='raised', tearoff=0)
    cm3.add_cascade(label='Buttons color', menu=sm1)
    sm2 = Menu(cm3, relief='raised', tearoff=0)
    cm3.add_cascade(label='Font color', menu=sm2)
    sm3 = Menu(cm3, relief='raised', tearoff=0)
    cm3.add_cascade(label='Buttons relief', menu=sm3)

    sm1.add_command(label="Red", command=colBR)
    sm1.add_command(label="Green", command=colBG)
    sm1.add_command(label="Blue", command=colBB)
    sm1.add_command(label="Black", command=colBBl)
    sm1.add_command(label="Yellow", command=colBY)
    sm1.add_command(label="White", command=colBW)

    sm2.add_command(label="Red", command=colFR)
    sm2.add_command(label="Green", command=colFG)
    sm2.add_command(label="Blue", command=colFB)
    sm2.add_command(label="Black", command=colFBl)
    sm2.add_command(label="Yellow", command=colFY)
    sm2.add_command(label="White", command=colFW)

    sm3.add_command(label="Flat", command=relF)
    sm3.add_command(label="Raised", command=relRa)
    sm3.add_command(label="Sunken", command=relS)
    sm3.add_command(label="Groove", command=relG)
    sm3.add_command(label="Ridge", command=relR)
    sm3.add_command(label="Solid", command=relSo)

    Hm = Menu(m, relief='raised', tearoff=0)
    m.add_cascade(label="Help", menu=Hm)

    Hm.add_command(label="Help               F1", command=help1)
    Hm.add_command(label="About            F2", command=about)
    Hm.add_separator()
    Hm.add_command(label="Exit                ESC", command=exit1)


def butconf(bg, rel, fg):
    b1.config(bg=bg, relief=rel, fg=fg)
    b2.config(bg=bg, relief=rel, fg=fg)
    b3.config(bg=bg, relief=rel, fg=fg)
    b4.config(bg=bg, relief=rel, fg=fg)
    b5.config(bg=bg, relief=rel, fg=fg)
    b6.config(bg=bg, relief=rel, fg=fg)
    b7.config(bg=bg, relief=rel, fg=fg)
    b8.config(bg=bg, relief=rel, fg=fg)
    b9.config(bg=bg, relief=rel, fg=fg)
    b10.config(bg=bg, relief=rel, fg=fg)
    b11.config(bg=bg, relief=rel, fg=fg)
    b12.config(bg=bg, relief=rel, fg=fg)
    b13.config(bg=bg, relief=rel, fg=fg)
    b14.config(bg=bg, relief=rel, fg=fg)
    b15.config(bg=bg, relief=rel, fg=fg)
    b16.config(bg=bg, relief=rel, fg=fg)
    b17.config(bg=bg, relief=rel, fg=fg)
    b18.config(bg=bg, relief=rel, fg=fg)
    b19.config(bg=bg, relief=rel, fg=fg)
    b20.config(bg=bg, relief=rel, fg=fg)


def bgconf(bg):
    b1.config(bg=bg)
    b2.config(bg=bg)
    b3.config(bg=bg)
    b4.config(bg=bg)
    b5.config(bg=bg)
    b6.config(bg=bg)
    b7.config(bg=bg)
    b8.config(bg=bg)
    b9.config(bg=bg)
    b10.config(bg=bg)
    b11.config(bg=bg)
    b12.config(bg=bg)
    b13.config(bg=bg)
    b14.config(bg=bg)
    b15.config(bg=bg)
    b16.config(bg=bg)
    b17.config(bg=bg)
    b18.config(bg=bg)
    b19.config(bg=bg)
    b20.config(bg=bg)
    b21.config(bg=bg)
    b22.config(bg=bg)
    b23.config(bg=bg)
    b24.config(bg=bg)
    b25.config(bg=bg)
    b26.config(bg=bg)
    b27.config(bg=bg)
    b28.config(bg=bg)
    b29.config(bg=bg)
    b30.config(bg=bg)


def relconf(rel):
    b1.config(relief=rel)
    b2.config(relief=rel)
    b3.config(relief=rel)
    b4.config(relief=rel)
    b5.config(relief=rel)
    b6.config(relief=rel)
    b7.config(relief=rel)
    b8.config(relief=rel)
    b9.config(relief=rel)
    b10.config(relief=rel)
    b11.config(relief=rel)
    b12.config(relief=rel)
    b13.config(relief=rel)
    b14.config(relief=rel)
    b15.config(relief=rel)
    b16.config(relief=rel)
    b17.config(relief=rel)
    b18.config(relief=rel)
    b19.config(relief=rel)
    b20.config(relief=rel)
    b21.config(relief=rel)
    b22.config(relief=rel)
    b23.config(relief=rel)
    b24.config(relief=rel)
    b25.config(relief=rel)
    b26.config(relief=rel)
    b27.config(relief=rel)
    b28.config(relief=rel)
    b29.config(relief=rel)
    b30.config(relief=rel)


def fgconf(fg):
    b1.config(fg=fg)
    b2.config(fg=fg)
    b3.config(fg=fg)
    b4.config(fg=fg)
    b5.config(fg=fg)
    b6.config(fg=fg)
    b7.config(fg=fg)
    b8.config(fg=fg)
    b9.config(fg=fg)
    b10.config(fg=fg)
    b11.config(fg=fg)
    b12.config(fg=fg)
    b13.config(fg=fg)
    b14.config(fg=fg)
    b15.config(fg=fg)
    b16.config(fg=fg)
    b17.config(fg=fg)
    b18.config(fg=fg)
    b19.config(fg=fg)
    b20.config(fg=fg)
    b21.config(fg=fg)
    b22.config(fg=fg)
    b23.config(fg=fg)
    b24.config(fg=fg)
    b25.config(fg=fg)
    b26.config(fg=fg)
    b27.config(fg=fg)
    b28.config(fg=fg)
    b29.config(fg=fg)
    b30.config(fg=fg)


def butset():
    global b1
    global b2
    global b3
    global b4
    global b5
    global b6
    global b7
    global b8
    global b9
    global b10
    global b11
    global b12
    global b13
    global b14
    global b15
    global b16
    global b17
    global b18
    global b19
    global b20
    global b21
    global b22
    global b23
    global b24
    global b25
    global b26
    global b27
    global b28
    global b29
    global b30

    rel = 'raised'
    b1 = Button(root, text='C', width=5, relief=rel)
    b1.grid(row=1, column=0)
    b2 = Button(root, text='CE', width=5, relief=rel)
    b2.grid(row=1, column=1)
    b3 = Button(root, text='+-', width=5, relief=rel)
    b3.grid(row=1, column=2)
    b4 = Button(root, text='1/x', width=5, relief=rel)
    b4.grid(row=1, column=3)

    b5 = Button(root, text='7', width=5, relief=rel)
    b5.grid(row=2, column=0)
    b6 = Button(root, text='8', width=5, relief=rel)
    b6.grid(row=2, column=1)
    b7 = Button(root, text='9', width=5, relief=rel)
    b7.grid(row=2, column=2)
    b8 = Button(root, text='*', width=5, relief=rel)
    b8.grid(row=2, column=3)

    b9 = Button(root, text='4', width=5, relief=rel)
    b9.grid(row=3, column=0)
    b10 = Button(root, text='5', width=5, relief=rel)
    b10.grid(row=3, column=1)
    b11 = Button(root, text='6', width=5, relief=rel)
    b11.grid(row=3, column=2)
    b12 = Button(root, text='/', width=5, relief=rel)
    b12.grid(row=3, column=3)

    b13 = Button(root, text='1', width=5, relief=rel)
    b13.grid(row=4, column=0)
    b14 = Button(root, text='2', width=5, relief=rel)
    b14.grid(row=4, column=1)
    b15 = Button(root, text='3', width=5, relief=rel)
    b15.grid(row=4, column=2)
    b16 = Button(root, text='-', width=5, relief=rel)
    b16.grid(row=4, column=3)

    b17 = Button(root, text='0', width=5, relief=rel)
    b17.grid(row=5, column=0)
    b18 = Button(root, text='.', width=5, relief=rel)
    b18.grid(row=5, column=1)
    b19 = Button(root, text='=', width=5, relief=rel)
    b19.grid(row=5, column=2)
    b20 = Button(root, text='+', width=5, relief=rel)
    b20.grid(row=5, column=3)

    b21 = Button(root, text='sqrt', width=5, relief=rel)
    b21.grid(row=6, column=0)
    b22 = Button(root, text='!', width=5, relief=rel)
    b22.grid(row=6, column=1)
    b23 = Button(root, text='^', width=5, relief=rel)
    b23.grid(row=6, column=2)
    b24 = Button(root, text='trunc', width=5, relief=rel)
    b24.grid(row=6, column=3)

    b30 = Button(root, text='x^3', width=5, relief=rel)
    b30.grid(row=1, column=4)
    b25 = Button(root, text='<-', width=5, relief=rel)
    b25.grid(row=2, column=4)
    b26 = Button(root, text='%', width=5, relief=rel)
    b26.grid(row=3, column=4)
    b27 = Button(root, text='x^2', width=5, relief=rel)
    b27.grid(row=4, column=4)
    b28 = Button(root, text=')', width=5, relief=rel)
    b28.grid(row=5, column=4)
    b29 = Button(root, text='(', width=5, relief=rel)
    b29.grid(row=6, column=4)

    b1.bind("<Button-1>", commb1)
    b2.bind("<Button-1>", commb21)
    b3.bind("<Button-1>", commb3)
    b4.bind("<Button-1>", commb4)
    b5.bind("<Button-1>", commb5)
    b6.bind("<Button-1>", commb6)
    b7.bind("<Button-1>", commb7)
    b8.bind("<Button-1>", commb8)
    b9.bind("<Button-1>", commb9)
    b10.bind("<Button-1>", commb10)
    b11.bind("<Button-1>", commb11)
    b12.bind("<Button-1>", commb12)
    b13.bind("<Button-1>", commb13)
    b14.bind("<Button-1>", commb14)
    b15.bind("<Button-1>", commb15)
    b16.bind("<Button-1>", commb16)
    b17.bind("<Button-1>", commb17)
    b18.bind("<Button-1>", commb18)
    b19.bind("<Button-1>", commb19)
    b20.bind("<Button-1>", commb20)
    b21.bind("<Button-1>", commb221)
    b22.bind("<Button-1>", commb22)
    b23.bind("<Button-1>", commb23)
    b24.bind("<Button-1>", commb24)
    b25.bind("<Button-1>", commb2)
    b26.bind("<Button-1>", commb26)
    b27.bind("<Button-1>", commb27)
    b28.bind("<Button-1>", commb28)
    b29.bind("<Button-1>", commb29)
    b30.bind("<Button-1>", commb30)


def roothelp(event):
    help1()


def rootabout(event):
    about()


def rootexit(event):
    exit1()


def rootbind():
    root.bind("<F1>", roothelp)
    root.bind("<F2>", rootabout)
#    root.bind("<1>", commb13)
# root.bind("<ESC>", rootexit)


#        sm = Menu(m)
#        m.add_cascade(label="Size", menu=sm)
#        sm.add_command(label="500x500", command=square)
#        sm.add_command(label="700x400", command=rectangle)


from tkinter import *
import calculator as calc

root = Tk()
root.title("Calculator")
BG = ''
REL = ''
FG = ''
global exp
exp = ''
# EC = 'yellow'
# RC = ''
butset()
menu()
rootbind()
# btn_list = [
#     m+    M-   MS    MC   x3
#    'C', 'CE', '+-', '1/x', <-
#    '7', '8', '9', '*', %
#    '4', '5', '6', '/', x2
#    '1', '2', '3', '-', )
#    '0', '.', '=', '+', (]
# r = 1
# c = 0
# for b in btn_list:
#    Button(root, text=b, width=5, relief=rel).grid(row=r, column=c)
#    c += 1
#    if c > 3:
#        c = 0
#        r += 1
entry = Label(root, width=23, bg="yellow", text=exp, anchor=SE)
entry.grid(row=0, column=0, columnspan=5)
root.mainloop()
