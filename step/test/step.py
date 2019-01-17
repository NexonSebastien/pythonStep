from random import randint
#Musique
import pygame
from mutagen.mp3 import MP3

from PIL import ImageTk

from tkinter import *
from threading import Thread



def maMusique(musique):
    switcher = {
            "Call Me Maybe": "data/musique/track1.mp3",
            "Good Time": "data/musique/track2.mp3",
            "I Gotta Feeling": "data/musique/track3.mp3",
            "Play Hard": "data/musique/track4.mp3",
            "Alone": "data/musique/track5.mp3",
            "Hello": "data/musique/track6.mp3",
            "Levels": "data/musique/track7.mp3",
            }
    return switcher.get(musique)

def startGame(fenetreChanson,lb1):
    counter_id = None
    morceau = lb1.get(lb1.curselection())
    lienMusique = maMusique(morceau)
    audio = MP3(lienMusique)
    dureeMusique = audio.info.length
    level = 4000  # 1000
    duree =int(dureeMusique/(level/1000))

    def decompte(count=duree, i=5, vitesse=level):
        global counter_id
        lblTime['text'] = count
        if count > 0:
            counter_id = fenetreGame.after(vitesse, decompte, count - 1, i+1)
            position = randint(1, 4)
            if i%2 != 0:
                #monCanvas.delete(i - 1)
                #monCanvas.delete(i - 2)
                if position == 1:
                    pied = monCanvas.create_image(240, 0, anchor=NW, image=piedGPhoto)
                elif position == 2:
                    pied = monCanvas.create_image(1200, 0, anchor=NW, image=piedDPhoto)
                elif position == 3:
                    pied = monCanvas.create_image(240, 515, anchor=NW, image=piedGPhoto)
                elif position == 4:
                    pied = monCanvas.create_image(1200, 515, anchor=NW, image=piedDPhoto)
            else:
                pied = monCanvas.create_image(840, 455, anchor=NW, image=stepPhoto)
            monCanvas.delete(i - 1)
    def stop():
        if counter_id:
            fenetreGame.after_cancel(counter_id)
            lblTime['text'] = "stop!"

    fenetreChanson.destroy()
    fenetreGame = Tk()
    fm = Frame(fenetreGame)
    fenetreGame.title("Game")
    fenetreGame.attributes("-fullscreen", 1)  # Mettre en plein ecran
    fenetreGame.configure(bg="black")
    lblMusique = Label(fm, text="Musique en cours : "+morceau, font="Arial 30 italic", bg="#00ccff")
    lblMusique.pack(side=LEFT,fill=X, expand=YES)#bleu #00ccff / vert #00ccff/
    lblTime = Label(fm, text="Pas :", font="Arial 30 italic", bg="#00ccff")
    lblTime.pack(side=RIGHT, fill=X, expand=YES,  padx=5, pady=5)

    fm.pack(fill=BOTH, expand=YES)
    monCanvas = Canvas(fenetreGame, width=1920, height=1010, background="#ffcc66")

    sandPhoto = PhotoImage(width=1920, height=1010, file='data/image/sand.png')
    monCanvas.create_image(10, 10, image=sandPhoto, anchor=NW)

    ligne1 = monCanvas.create_line(960, 0, 960, 1030)
    ligne2 = monCanvas.create_line(0, 515, 1920, 515)
    #txtCentre = monCanvas.create_text(960, 515, text="CENTRE", font="Arial 16 italic", fill="blue")

    piedGPhoto = PhotoImage(file='data/image/piedG.png')
    piedDPhoto = PhotoImage(file='data/image/piedD.png')
    stepPhoto = PhotoImage(file='data/image/step.png')

    monCanvas.pack(side=BOTTOM)
    btnBack = Button(fenetreGame, text="Quitter", bg="#00ccff", command=fenetreGame.destroy)
    btnBack.pack(fill=X, side=BOTTOM)
    pygame.mixer.music.load(lienMusique)
    pygame.mixer.music.play(0)
    decompte()
    fenetreGame.mainloop()

def createFenetreChanson(fenParent):
    def Music():
        morceau = lb1.get(lb1.curselection())
        lienMusique = maMusique(morceau)
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
    lb1 = Listbox(fenetreChanson)
    lb1.insert(1, "Call Me Maybe")
    lb1.insert(2, "Good Time")
    lb1.insert(3, "I Gotta Feeling")
    lb1.insert(4, "Play Hard")
    lb1.insert(5, "Alone")
    lb1.insert(6, "Hello")
    lb1.insert(7, "Levels")
    lb1.pack()
    lb1.select_set(0)#Selectionne pas default le premier
    fenetreChanson.attributes("-fullscreen", 1)  # Mettre en plein ecran

    #PYGAME Prévisualisation Musique
    musique = IntVar()
    musique.set(0)  # ON
    btnCheck = Checkbutton(fenetreChanson, text="Play Music", variable=musique, command=Music).pack()

    btnGame = Button(fenetreChanson, text="Start", command=lambda: startGame(fenetreChanson, lb1)).pack()
    btnBack = Button(fenetreChanson, text="Quitter", bg="red", command=fenetreChanson.destroy).pack(fill=X, side=BOTTOM)
    fenetreChanson.mainloop()

#MAIN
pygame.mixer.init()
#Réglage volume
pygame.mixer.music.set_volume(0.9)
fenetreAccueil = Tk()
fenetreAccueil.title("STEP")
fenetreAccueil.attributes("-fullscreen", True)  # Mettre en plein ecran
image = PhotoImage(file="data/image/accueil.png")
w, h = image.width(), image.height()
monCanvas = Canvas(fenetreAccueil, width=w, height=h)
monCanvas.create_image(0, 0, anchor=NW, image=image)
monCanvas.pack(anchor=CENTER)
playPhoto = PhotoImage(file='data/image/play.png')
btnStart = Button(fenetreAccueil, text="Démarrer", image=playPhoto, command=lambda: createFenetreChanson(fenetreAccueil)).pack()
btnExit = Button(fenetreAccueil, text="Quitter", bg="red", command=fenetreAccueil.destroy).pack(fill=X,side=BOTTOM)
fenetreAccueil.mainloop()

#snexon
