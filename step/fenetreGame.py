#FENETRE GAME
import pygame
from tkinter import *
from mutagen.mp3 import MP3
import fonctionCommune
from threading import Thread

def startGame(fenetreChanson,lb1,level):
    morceau = lb1.get(lb1.curselection())
    lienMusique = fonctionCommune.maMusique(morceau)
    audio = MP3(lienMusique)
    dureeMusique = audio.info.length
    duree =int(dureeMusique/(level/1000))

    #THREAD PIED
    threadPiedAvantLecture = Thread(target=fonctionCommune.piedAvant)
    threadPiedArriereLecture = Thread(target=fonctionCommune.piedArriere)

    fenetreChanson.destroy()
    fenetreGame = Tk()
    fm = Frame(fenetreGame)
    fenetreGame.title("Game")
    fenetreGame.attributes("-fullscreen", 1)  # Mettre en plein ecran
    fenetreGame.configure(bg="black")

    quitterPhoto = PhotoImage(file=fonctionCommune.monImage("back"))

    lblMusique = Label(fm, text="Musique en cours : " + morceau, font="Arial 30 italic", bg="#ffcc66")#00ccff
    btnBack = Button(fm, image=quitterPhoto, bg="#ffcc66", command=fenetreGame.destroy)
    lblTime = Label(fm, text="Nombre de pas : ", font="Arial 30 italic", bg="#ffcc66")
    lblScore = Label(fm, text="Score : 0", font="Arial 30 italic", bg="#ffcc66")


    lblMusique.pack(side=LEFT, fill=BOTH, expand=YES)  # bleu #00ccff / vert #00ccff/
    btnBack.pack(side=RIGHT, fill=BOTH)
    lblTime.pack(side=RIGHT, fill=BOTH, expand=YES)#padx=5, pady=5
    lblScore.pack(side=RIGHT, fill=BOTH,expand=YES)


    fm.pack(fill=BOTH, expand=YES)
    monCanvas = Canvas(fenetreGame, width=1920, height=1010, background="#ffcc66")#E8CB69

    sandPhoto = PhotoImage(file=fonctionCommune.monImage("sand"))
    monCanvas.create_image(0, 0, image=sandPhoto, anchor=NW)

    ligne1 = monCanvas.create_line(960, 0, 960, 1030)
    ligne2 = monCanvas.create_line(0, 515, 1920, 515)
    debugCanvas = monCanvas.create_text(960, 515, text="")
    #txtCentre = monCanvas.create_text(960, 515, text="CENTRE", font="Arial 16 italic", fill="blue")

    monCanvas.pack(side=BOTTOM)

    pygame.mixer.music.load(lienMusique)
    pygame.mixer.music.play(0)

    fonctionCommune.variableDecompte(duree, level, fenetreGame, lblTime, monCanvas,lblScore)

    threadPiedAvantLecture.start()
    threadPiedArriereLecture.start()

    fenetreGame.mainloop()

