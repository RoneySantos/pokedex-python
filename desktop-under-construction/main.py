#Import tkinter to create windows 
from tkinter import *
from tkinter import ttk
#Import Pillow to manipulate images
from PIL import Image, ImageTk


####### Colors #######
co0 = "#444466"  # Black
co1 = "#feffff"  # White
co2 = "#6f9fbd"  # Blue
co3 = "#38576b"  # Navy
co4 = "#403d3d"  # Gray
co5 = "#ef5350"  # Red
co6 = "#FFEC8B"  # Yellow Gold

# Creating window

janela = Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

# Creating frame 1
frame_pkm_1 = Frame(janela, width=550, height=290, relief='flat', bg=co6)
frame_pkm_1.grid(row=1, column=0)

#Pokemon Name
pkm_name = Label(frame_pkm_1, text='Pokemon', relief=FLAT, anchor=CENTER, font=('Fixedsys 20'), bg=co1, fg=co0)
pkm_name.place(x=12, y=15)

#Pokemon Id
pkm_id = Label(frame_pkm_1, text='#001', relief=FLAT, anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co0)
pkm_id.place(x=12, y=50)

#Pokemon img
pkm_category = Label(frame_pkm_1, text='Air', relief=FLAT, anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co0)
pkm_category.place(x=12, y=70)

#Image from Pokemon
image_pkm = Image.open('images/pikachu.png')
image_pkm = image_pkm.resize((238, 238))
image_pkm = ImageTk.PhotoImage(image_pkm)

pkm_img = Label(frame_pkm_1, image=image_pkm, relief=FLAT, anchor=CENTER,bg=co1, fg=co0)
pkm_img.place(x=60, y=50)

#Creating status
pkm_status = Label(janela, text='Status', relief=FLAT, anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pkm_status.place(x=15, y=290)

#Creating hp
pkm_hp = Label(janela, text='hp', relief=FLAT, anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
pkm_hp.place(x=15, y=330)

#Creating attack
pkm_attack = Label(janela, text='attack', relief=FLAT, anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
pkm_attack.place(x=15, y=350)

#Creating defense
pkm_defense = Label(janela, text='defense', relief=FLAT, anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
pkm_defense.place(x=15, y=370)

#Creating Speed
pkm_Speed = Label(janela, text='Speed', relief=FLAT, anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
pkm_Speed.place(x=15, y=390)

#Creating Total
pkm_Total = Label(janela, text='Total', relief=FLAT, anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
pkm_Total.place(x=15, y=410)

#Creating attacks
pkm_attacks = Label(janela, text='Attacks', relief=FLAT, anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pkm_attacks.place(x=150, y=290)

#Creating attacks 1
pkm_attacks = Label(janela, text='Attacks whatever 1', relief=FLAT, anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
pkm_attacks.place(x=150, y=350)

#Creating attacks 2
pkm_attacks = Label(janela, text='Attacks whatever 2', relief=FLAT, anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
pkm_attacks.place(x=150, y=370)

# #Creating hp
# pkm_hp = Label(janela, text='hp', relief=FLAT, anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
# pkm_hp.place(x=15, y=330)

# #Creating attack
# pkm_attack = Label(janela, text='attack', relief=FLAT, anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
# pkm_attack.place(x=15, y=350)

# #Creating defense
# pkm_defense = Label(janela, text='defense', relief=FLAT, anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
# pkm_defense.place(x=15, y=370)

#Overlay text
pkm_category.lift()


# Main Function to run window
janela.mainloop()
