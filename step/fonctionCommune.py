from random import randint
from tkinter import *
from serial import *
from threading import *

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

def monChiffre(chiffre):
    switcher = {
            1: "data/image/1.png",
            2: "data/image/2.png",
            3: "data/image/3.png",
            4: "data/image/4.png",
            5: "data/image/5.png",
            }
    return switcher.get(chiffre)

def monImage(image):
    switcher = {
            "step": "data/image/step.png",
            "piedG": "data/image/piedG.png",
            "piedD": "data/image/piedD.png",
            "piedGV": "data/image/piedGV.png",
            "piedDV": "data/image/piedDV.png",
            "sand": 'data/image/sand.png',
            "back": 'data/image/back.png',
            }
    return switcher.get(image)

piedAvantDistance = 0
def piedAvant():
    global piedAvantDistance
    """ser = Serial("COM3", timeout=1)"""
    while 1:
        """donnee = ser.readline().decode('utf-8')
        # donnee = float(donnee)
        # ser.close()
        if (len(donnee)) > 0:
            if donnee[0].isdigit():
                piedAvantDistance = donnee
                #print(donnee)"""
        piedAvantDistance = randint(0,100)
        print(piedAvantDistance)

piedArriereDistance = 0
def piedArriere():
    global piedArriereDistance
    """ser = Serial("COM3", timeout=1)"""
    while 1:
        """donnee = ser.readline().decode('utf-8')
        # donnee = float(donnee)
        # ser.close()
        if (len(donnee)) > 0:
            if donnee[0].isdigit():
                piedArriereDistance = donnee
                #print(donnee)"""
        piedArriereDistance = randint(0,100)



def variableDecompte(duree,level,fenetreGame,lblTime,monCanvas,lblScore):
    global threadPiedAvant
    global threadPiedArriere
    global score
    score = 0
    global scoreMax
    scoreMax = 0
    global position
    position = 0
    global numCanvas
    numCanvas = 5
    piedGPhoto = PhotoImage(file=monImage("piedG"))
    piedDPhoto = PhotoImage(file=monImage("piedD"))
    piedGVPhoto = PhotoImage(file=monImage("piedGV"))
    piedDVPhoto = PhotoImage(file=monImage("piedDV"))
    stepPhoto = PhotoImage(file=monImage("step"))

    def decompte(count=duree, i=0, vitesse=level):
        global counter_id
        global numberPhoto
        global position
        global numCanvas
        lblTime['text'] = "Nombre de pas : "+str(count)
        if count > 0:
            counter_id = fenetreGame.after(vitesse, decompte, count - 1, i+1)
            if i < 5:
                j = 5 - i
                path = monChiffre(j)
                numberPhoto = PhotoImage(file=path)
                monCanvas.create_image(835, 350, anchor=NW, image=numberPhoto)
                numCanvas += 1
            else:
                if i % 2 == 0:
                    position = randint(1, 4)
                    threadPiedAvant = Thread(target=valide)
                    threadPiedArriere = Thread(target=valide)
                    if position == 1:
                        pied = monCanvas.create_image(240, 0, anchor=NW, image=piedGPhoto)
                        threadPiedAvant.start()
                    elif position == 2:
                        pied = monCanvas.create_image(1200, 0, anchor=NW, image=piedDPhoto)
                        threadPiedAvant.start()
                    elif position == 3:
                        pied = monCanvas.create_image(240, 515, anchor=NW, image=piedGPhoto)
                        threadPiedArriere.start()
                    elif position == 4:
                        pied = monCanvas.create_image(1200, 515, anchor=NW, image=piedDPhoto)
                        threadPiedArriere.start()
                    numCanvas += 1
                else:
                    monCanvas.delete(numCanvas - 1)
                    pied = monCanvas.create_image(775, 350, anchor=NW, image=stepPhoto)
                    numCanvas += 1
                    stopValid()
                #monCanvas.delete(numCanvas - 1) #Pour faire disparaitre le step quand on met le pied

    def stopDecompte():
        if counter_id:
            fenetreGame.after_cancel(counter_id)
            lblTime['text'] = "Fin !"


    def valide():
        global piedAvantDistance
        global piedArriereDistance
        global position
        global ok
        global numCanvas
        ok = True
        while ok:
            if position == 1:  # AvantG
                if int(piedAvantDistance)> 0 and int(piedAvantDistance) < 30:#Avec capteur
                    ok = False
                    pied = monCanvas.create_image(240, 0, anchor=NW, image=piedGVPhoto)
                    numCanvas += 1
            if position == 2:  # AvantD
                if int(piedAvantDistance) > 30 and int(piedAvantDistance) < 100:
                    ok = False
                    pied = monCanvas.create_image(1200, 0, anchor=NW, image=piedDVPhoto)
                    numCanvas += 1
            if position == 3:  # ArriereG
                if int(piedArriereDistance)> 0 and int(piedArriereDistance) < 30:#Avec capteur
                    ok = False
                    pied = monCanvas.create_image(240, 515, anchor=NW, image=piedGVPhoto)
                    numCanvas += 1
            if position == 4:  # ArriereD
                if int(piedArriereDistance) > 30 and int(piedArriereDistance) < 100:
                    ok = False
                    pied = monCanvas.create_image(1200, 515, anchor=NW, image=piedDVPhoto)
                    numCanvas += 1
            #print(piedAvantDistance)
            print(piedArriereDistance)
    global ok
    ok = 0
    def stopValid():
        global ok
        global scoreMax
        global score
        if ok == True:
            ok = False
            print('Fail')
        else:
            score += 1
            monCanvas.delete(numCanvas - 3)
        scoreMax += 1
        lblScore['text'] = "Score : " + str(score) + "/" + str(scoreMax)
    decompte()