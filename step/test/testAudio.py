from tkinter import *
import pygame

lienMusique = 'data/musique/track3.mp3'


pygame.mixer.init()
pygame.mixer.music.load(lienMusique)
# réglage volume
pygame.mixer.music.set_volume(0.9)

def Music():
    print(musique.get())
    if musique.get() == 1:
        # 1 (ON)
        # joue en boucle
        pygame.mixer.music.play(-1)
    else:
        # 0 (OFF)
        pygame.mixer.music.stop()

# Création de la fenêtre principale (main window)
Mafenetre = Tk()
Mafenetre.title("Checkbutton widget + Pygame.mixer")


# Création d'un widget Checkbutton
musique = IntVar()
musique.set(1) # ON
Checkbutton(Mafenetre,text="Musique de fond",variable=musique,command=Music).pack(side=LEFT,padx=10,pady=10)

Music()
Mafenetre.mainloop()
