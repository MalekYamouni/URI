import tkinter
from tkinter import ttk

def Beenden_click():
    frmMain.destroy()


def Berechnung_R_click():
    U = float(Spannung_U.get())
    I = float(Strom_I.get())

    ergebnis: float = U/I

    Widerstand_R.delete(0, "end")
    Widerstand_R.insert(0, round(ergebnis, 2))

def Berechnung_U_click():
    R = float(Widerstand_R.get())
    I = float(Strom_I.get())

    ergebnis: float = R*I

    Spannung_U.delete(0, "end")
    Spannung_U.insert(0, round(ergebnis, 2))

def Berechnung_I_click():
    U = float(Spannung_U.get())
    R = float(Widerstand_R.get())

    ergebnis: float = U/R

    Strom_I.delete(0, "end")
    Strom_I.insert(0, round(ergebnis, 2))





# Hauptfenster

frmMain = tkinter.Tk()
frmMain.title("Grundstromkreis")
frmMain.wm_geometry("800x500")



# Linien und Kreise
g = tkinter.Canvas(frmMain, width=800, height=500)
g.pack(pady=40)
# waagerecht
g.create_line(200, 100, 150, 100)
g.create_line(175, 100, 175, 50)
g.create_line(175, 50, 430, 50)

g.create_line(470, 50, 580, 50)
g.create_line(580, 50, 580, 100)
g.create_line(580, 150, 580, 200)
g.create_line(580, 200, 175, 200)

g.create_line(175, 200, 175, 120)
g.create_line(185, 120, 165, 120)

g.create_line(520, 50, 520, 100)
g.create_line(520, 140, 520, 200)

# Buttons

R_button = ttk.Button(frmMain, text="R Berechnen", command=Berechnung_R_click)
R_button.place(x=340, y=310)

U_button = ttk.Button(frmMain, text="U Berechnen", command=Berechnung_U_click)
U_button.place(x=340, y=280)

I_Button = ttk.Button(frmMain, text="I Berechnen", command=Berechnung_I_click)
I_Button.place(x=340, y=340)

# Widerstand Rechteck
g.create_line(570, 100, 590, 100)
g.create_line(570, 100, 570, 150)
g.create_line(590, 100, 590, 150)
g.create_line(570, 150, 590, 150)

# Pfeile und dreieck

g.create_line(250, 40, 400, 40, fill="#cd3333")
g.create_polygon(400, 35, 400, 45, 410, 40, fill="#cd3333")

g.create_line(230, 60, 230, 170, fill="#36648b")
g.create_polygon(225, 170, 235, 170, 230, 180, fill="#36648b")

# Kreise für I und U
g.create_oval(430, 70, 470, 30)

g.create_oval(500, 140, 540, 100)


# Labels, Buchstaben
Strom_Label = tkinter.Label(frmMain, text="Strom I in Ampere", fg="#cd3333")
Strom_Label.place(x=250, y=50)

Strom_I_Buchstabe = tkinter.Label(frmMain, text="I", fg="#cd3333")
Strom_I_Buchstabe.place(x=445, y=80)

Spannung_Label = tkinter.Label(frmMain, text="Spannung U in Volt", fg="#36648b")
Spannung_Label.place(x=250, y=170)

Spannung_U_buchstabe = tkinter.Label(frmMain, text="U", fg="#36648b")
Spannung_U_buchstabe.place(x=513, y=150)

Widerstand_label = tkinter.Label(frmMain, text="Widerstand R in Ohm", fg="green")
Widerstand_label.place(x=600, y=180)



# Entrys

Strom_I = tkinter.Entry(frmMain)
Strom_I.place(x=250, y=30)

Spannung_U = tkinter.Entry(frmMain)
Spannung_U.place(x=250, y=200)

Widerstand_R = tkinter.Entry(frmMain)
Widerstand_R.place(x=600, y=160)



# Endlosschleife

frmMain.mainloop()