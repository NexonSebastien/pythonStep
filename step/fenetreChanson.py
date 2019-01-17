#FENETRE CHANSON
import pygame
from tkinter import *
import fenetreGame
import fonctionCommune

def createFenetreChanson(fenParent):
    def Music():
        morceau = lb1.get(lb1.curselection())
        lienMusique = fonctionCommune.maMusique(morceau)
        pygame.mixer.music.load(lienMusique)
        if musique.get() == 1:
            # 1 (ON)
            pygame.mixer.music.play(0)
        else:
            # 0 (OFF)
            pygame.mixer.music.stop()

    fenParent.destroy()
    fenetreChanson = Tk()
    fenetreChanson.title("Chansons")
    fenetreChanson.attributes("-fullscreen", 1)  # Mettre en plein ecran

    backgroundImage = PhotoImage(file="data/image/chanson.png")
    quitterPhoto = PhotoImage(file=fonctionCommune.monImage("back"))
    startButtonPhoto = PhotoImage(file='data/image/startButton.png')

    backgroundLabel = Label(fenetreChanson, image=backgroundImage)
    backgroundLabel.place(x=0, y=0, relwidth=1, relheight=1)

    btnBack = Button(fenetreChanson, text="Quitter", image=quitterPhoto, bg='black',
                     command=fenetreChanson.destroy).pack(side=TOP, anchor=NE)

    lblMusique = Label(fenetreChanson, text="Musique : ", bg='black',
                     fg="white", font="Arial 20 italic").pack(side=TOP, anchor=NW)

    lb1 = Listbox(fenetreChanson, bg='black', fg="white")
    lb1.insert(1, "Call Me Maybe")
    lb1.insert(2, "Good Time")
    lb1.insert(3, "I Gotta Feeling")
    lb1.insert(4, "Play Hard")
    lb1.insert(5, "Alone")
    lb1.insert(6, "Hello")
    lb1.insert(7, "Levels")
    lb1.pack(side=TOP, anchor=NW)
    lb1.select_set(0)#Selectionne pas default le premier

    #PYGAME Prévisualisation Musique
    musique = IntVar()
    musique.set(0)  # ON
    btnCheck = Checkbutton(fenetreChanson, text="Play Music", bg='black', fg='white', selectcolor='black',
                     variable=musique, command=Music).pack(side=TOP, anchor=NW)

    # LEVELS
    lblLevel = Label(fenetreChanson, text="Level : ", bg='black', fg="white",
                     font="Arial 20 italic").pack(side=TOP, anchor=NE)
    levels = [
        ("EXPERT", 750),
        ("NORMAL", 1000),
        ("FACILE", 1250),
    ]

    v = IntVar()
    v.set(1000)  # initialize la valeur par default
    for text, level in levels:
        rB = Radiobutton(fenetreChanson, text=text, bg='black', fg="white", selectcolor='black',variable=v, value=level)
        rB.pack(side=TOP, anchor=NE)

    btnGame = Button(fenetreChanson, text="Start", image=startButtonPhoto, bg='black',
                     command=lambda: fenetreGame.startGame(fenetreChanson, lb1, v.get())).pack(anchor=SW)

    fenetreChanson.mainloop()

