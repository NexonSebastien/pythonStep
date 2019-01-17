"""from tkinter import *

root = Tk()
c = Canvas(root)
c.pack()

# image
fond = PhotoImage(file="../data/image/chanson.png")
bouton = PhotoImage(file="../data/image/play.png")

# image de fond
c.create_image(0, 0, image=fond)

# bouton cliquable (50, 50)
c.create_image(50, 50, image=bouton)



root.mainloop()"""

from tkinter import *
root = Tk()
background_image = PhotoImage(file='../data/image/chanson.png')

background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
#root.wm_geometry("600x400+20+40")
root.title('Menu')

lblMusique = Label(root, text="Musique : ", font="Arial 20 italic")
lblMusique.pack()

lb1 = Listbox(root)
lb1.insert(1, "Call Me Maybe")
lb1.insert(2, "Good Time")
lb1.insert(3, "I Gotta Feeling")
lb1.insert(4, "Play Hard")
lb1.insert(5, "Alone")
lb1.insert(6, "Hello")
lb1.insert(7, "Levels")
lb1.pack()

lb1.select_set(0)#Selectionne pas default le premier



playButton = Button(root, text='Play', command=root.destroy)
playButton.pack()
root.mainloop()