#MAIN
import fenetreChanson
import pygame
from tkinter import *

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
btnStart = Button(fenetreAccueil, text="Démarrer", image=playPhoto, command=lambda: fenetreChanson.createFenetreChanson(fenetreAccueil)).pack()
btnExit = Button(fenetreAccueil, text="Quitter", bg="red", command=fenetreAccueil.destroy).pack(fill=X,side=BOTTOM)
fenetreAccueil.mainloop()

