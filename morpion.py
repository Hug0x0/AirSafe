##########################
# -*- coding:Latin-1 -*- #
#                        #
#   Morpion by SaMuRiZe  #
##########################

from Tkinter import *
from random import randrange

class Application(Tk):
    """Application principale"""
    def __init__(self, boss = None):
        Tk.__init__(self)
        #Definition du premier joueur
        self.joueura = 'on'
        self.title(""".SaM!'s Morpion""")
        self.l1 = Label(self, text='Score : \n Vous 0 -  Ordi 0')
        self.l1.pack(pady = 1)
        #Definition du Canvas principal
        self.can1 = Canvas(self, width = 300, height = 300, bg = 'white')
        self.can1.pack(padx = 5, pady = 5)
        self.tracer_plateau()
        self.bind("<Button-1>", self.analyser_pos_click)
        self.bind("<Escape>", self.quitter)
        self.b1 = Button(self, text='Recommencer', command=self.recommancer2)
        self.b1.pack(side = 'left', padx = 5)
        self.b2 = Button(self, text='Quitter', command=self.destroy)
        self.b2.pack(side = 'right', padx = 5)
        self.pos = [0] * 10
        self.ai = Intel_Art(boss = self)
        self.ai_enabled = 'on'
        self.ja_score = 0
        self.jb_score = 0

    def tracer_plateau(self):
        #Trace du plateau
        self.can1.create_line(105, 10, 105, 290, width = 10)
        self.can1.create_line(205, 10, 205, 290, width = 10)
        self.can1.create_line(10, 105, 290, 105, width = 10)
        self.can1.create_line(10, 205, 290, 205, width = 10)

    def recommancer(self):
        #Pas besoin de grand discours...
        self.title(""".SaM!'s Morpion""")
        self.can1.delete(ALL)
        self.tracer_plateau()
        self.pos = [0] * 10

    def recommancer2(self):
        self.recommancer()
        self.score('r')

    def quitter(self, event):
        self.destroy()

    def tracer_croix(self, x, y):
        #Trace une croix dans le Canvas principal
        self.can1.create_line(x-35, y-35, x+35, y+35, width = 5, fill = 'blue')
        self.can1.create_line(x-35, y+35, x+35, y-35, width = 5, fill = 'blue')

    def tracer_rond(self, x, y):
        #Trace un rond dans la Canvas principal
        self.can1.create_oval(x - 35, y - 35, x + 35, y + 35, fill = 'red')
        self.can1.create_oval(x - 30, y - 30, x+30, y+30, fill = 'white')

    def analyser_pos_click(self, event):
        #Detection de la position de la souris dans le Canvas en fonction des cases
        # 1 | 2 | 3
        # - + - + -
        # 4 | 5 | 6
        # - + - + -
        # 7 | 8 | 9
        if self.pos[0] == 0:
            if event.x > 0 and event.x < 100:
                if event.y > 0 and event.y < 100:
                    i = 1
                    self.xtrace = 55
                    self.ytrace = 55
                if event.y > 100 and event.y < 200:
                    i = 4
                    self.xtrace = 55
                    self.ytrace = 155
                if event.y > 200 and event.y < 300:
                    i = 7
                    self.xtrace = 55
                    self.ytrace = 255
            elif event.x > 100 and event.x < 200:
                if event.y > 0 and event.y < 100:
                    i = 2
                    self.xtrace = 155
                    self.ytrace = 55
                if event.y > 100 and event.y < 200:
                    i = 5
                    self.xtrace = 155
                    self.ytrace = 155
                if event.y > 200 and event.y < 300:
                    i = 8
                    self.xtrace = 155
                    self.ytrace = 255
            elif event.x > 200 and event.x < 300:
                if event.y > 0 and event.y < 100:
                    i = 3
                    self.xtrace = 255
                    self.ytrace = 55
                if event.y > 100 and event.y < 200:
                    i = 6
                    self.xtrace = 255
                    self.ytrace = 155
                if event.y > 200 and event.y < 300:
                    i = 9
                    self.xtrace = 255
                    self.ytrace = 255

            if self.joueura == 'on' and self.pos[i] == 0:
                self.pos[i] = 'a'
                self.tracer_croix(self.xtrace, self.ytrace)
                if self.ai_enabled != 'on':
                    self.joueura = 'off'
                    self.joueurb = 'on'
                if self.ai_enabled == 'on':
                    self.verif_gagner()
                    if self.pos[0] != 0:
                        return 1
                    self.ai.ai_a_toi_de_jouer()
                    return 1
            elif (self.joueurb == 'on' and self.pos[i] == 0 and self.ai_enabled != 'on'):
                if self.ai_enabled != 1:
                    self.pos[i] = 'b'
                    self.tracer_rond(self.xtrace, self.ytrace)
                    self.joueura = 'on'
                    self.joueurb = 'off'
            else:
                print "Coup impossible"
                return 1

            self.verif_gagner()
        else:
            self.recommancer()

    def verif_gagner(self):
        #Definition des 8 possibilites de gagner et tracer d'une grand ligne si gagner
        if self.pos[1] == self.pos[2] == self.pos[3] and self.pos[1] != 0:
            self.can1.create_line(10, 55, 290, 55, width = 10, fill = 'green')
            self.pos[0] =  self.pos[1]
        elif self.pos[4] == self.pos[5] == self.pos[6] and self.pos[4] != 0:
            self.can1.create_line(10, 155, 290, 155, width = 10, fill = 'green')
            self.pos[0] =  self.pos[4]
        elif self.pos[7] == self.pos[8] == self.pos[9] and self.pos[7] != 0:
            self.can1.create_line(10, 255, 290, 255, width = 10, fill = 'green')
            self.pos[0] =  self.pos[7]
        elif self.pos[1] == self.pos[4] == self.pos[7] and self.pos[1] != 0:
            self.can1.create_line(55, 10, 55, 290, width = 10, fill = 'green')
            self.pos[0] =  self.pos[1]
        elif self.pos[2] == self.pos[5] == self.pos[8] and self.pos[2] != 0:
            self.can1.create_line(155, 10, 155, 290, width = 10, fill = 'green')
            self.pos[0] =  self.pos[2]
        elif self.pos[3] == self.pos[6] == self.pos[9] and self.pos[3] != 0:
            self.can1.create_line(255, 10, 255, 290, width = 10, fill = 'green')
            self.pos[0] =  self.pos[3]
        elif self.pos[1] == self.pos[5] == self.pos[9] and self.pos[1] != 0:
            self.can1.create_line(10, 10, 290, 290, width = 10, fill = 'green')
            self.pos[0] =  self.pos[1]
        elif self.pos[7] == self.pos[5] == self.pos[3] and self.pos[7] != 0:
            self.can1.create_line(10, 290, 290, 10, width = 10, fill = 'green')
            self.pos[0] =  self.pos[7]
        elif self.pos[1] != 0 and self.pos[2] != 0 and self.pos[3] != 0 and self.pos[4] != 0 and self.pos[5] != 0 and self.pos[6] != 0 and self.pos[7] != 0 and self.pos[8] != 0 and self.pos[9] != 0:
            self.pos[0] = 'c'

        if self.pos[0] != 0:
            if self.pos[0] == 'a':
                self.title('Joueur A Win !!')
                self.score('a')
            elif self.pos[0] == 'b':
                self.title('Joueur B Win !!')
                self.score('b')
            elif self.pos[0] == 'c':
                self.title('Match Nul')

    def lire_tableau(self):
        print " " + str(self.pos[1]) + " | " + str(self.pos[2]) + " | " + str(self.pos[3])
        print " - + - + -"
        print " " + str(self.pos[4]) + " | " + str(self.pos[5]) + " | " + str(self.pos[6])
        print " - + - + -"
        print " " + str(self.pos[7]) + " | " + str(self.pos[8]) + " | " + str(self.pos[9])

    def score(self, joueur):
        if joueur == 'a':
            self.ja_score = self.ja_score + 1
        elif joueur == 'b':
            self.jb_score = self.jb_score + 1
        elif joueur == 'r':
            self.jb_score = 0
            self.ja_score = 0
        self.l1.configure(text='Score : \n Vous ' + str(self.ja_score) + ' -  Ordi ' + str(self.jb_score))

class Intel_Art(Application):
    """Definition de l'intelligence artificelle"""
    def __init__(self, boss):
        self.boss = boss

    def ai_a_toi_de_jouer(self):
        print "AI init"
        self.copier_liste_a()
        self.ai_analyser()
        print "AI finished"

    def copier_liste_a(self):
        self.pos2 = []
        for i in self.boss.pos:
            self.pos2.append(i)
        print self.pos2

    def copier_liste_b(self):
        self.boss.pos = []
        for i in self.pos2:
            self.boss.pos.append(i)

    def ai_analyser(self):
        self.varj = 0
        #Analyse si AI peut gagner au prochain coup
        #Le joueur B est toujours l'AI
        while (self.varj<9):
            self.varj = self.varj + 1
            if (self.boss.pos[self.varj] == 0):
                self.copier_liste_b()
                self.boss.pos[self.varj] = 'b'
                self.ai_analyser_possibilitees()
                if self.boss.pos[0] == 'b':
                    #self.copier_liste_b()
                    self.boss.pos[self.varj] = 'b'
                    #print self.boss.pos
                    self.boss.lire_tableau()
                    self.tracer(self.varj)
                    self.boss.verif_gagner()
                    return 1

        self.varj = 0
        #Analyse du jeu de l'adversaire
        while (self.varj<9):
            self.varj = self.varj + 1
            if (self.boss.pos[self.varj] == 0):
                self.copier_liste_b()
                self.boss.pos[self.varj] = 'a'
                self.ai_analyser_possibilitees()
                if self.boss.pos[0] == 'a':
                    #self.copier_liste_b()
                    self.boss.pos[0] = 0
                    self.boss.pos[self.varj] = 'b'
                    #print self.boss.pos
                    self.boss.lire_tableau()
                    self.tracer(self.varj)
                    self.boss.verif_gagner()
                    return 1

        #S'il ne peut pas gagner:
        self.tirer_au_hasard()

    def tirer_au_hasard(self):
        if self.boss.pos[0] == 0:
            self.varj = randrange(1, 9)
            if self.boss.pos[self.varj] == 0:
                self.copier_liste_b()
                self.boss.pos[self.varj] = 'b'
                print self.boss.pos
                self.tracer(self.varj)
            else:
                self.tirer_au_hasard()



    def ai_analyser_possibilitees(self):
        if self.boss.pos[1] == self.boss.pos[2] == self.boss.pos[3] and self.boss.pos[1] != 0:
            self.boss.pos[0] =  self.boss.pos[1]
        elif self.boss.pos[4] == self.boss.pos[5] == self.boss.pos[6] and self.boss.pos[4] != 0:
            self.boss.pos[0] =  self.boss.pos[4]
        elif self.boss.pos[7] == self.boss.pos[8] == self.boss.pos[9] and self.boss.pos[7] != 0:
            self.boss.pos[0] =  self.boss.pos[7]
        elif self.boss.pos[1] == self.boss.pos[4] == self.boss.pos[7] and self.boss.pos[1] != 0:
            self.boss.pos[0] =  self.boss.pos[1]
        elif self.boss.pos[2] == self.boss.pos[5] == self.boss.pos[8] and self.boss.pos[2] != 0:
            self.boss.pos[0] =  self.boss.pos[2]
        elif self.boss.pos[3] == self.boss.pos[6] == self.boss.pos[9] and self.boss.pos[3] != 0:
            self.boss.pos[0] =  self.boss.pos[3]
        elif self.boss.pos[1] == self.boss.pos[5] == self.boss.pos[9] and self.boss.pos[1] != 0:
            self.boss.pos[0] =  self.boss.pos[1]
        elif self.boss.pos[7] == self.boss.pos[5] == self.boss.pos[3] and self.boss.pos[7] != 0:
            self.boss.pos[0] =  self.boss.pos[7]

    def tracer(self, case):
        if case == 1:
            self.boss.tracer_rond(55, 55)
        elif case == 2:
            self.boss.tracer_rond(155, 55)
        elif case == 3:
            self.boss.tracer_rond(255, 55)
        elif case == 4:
            self.boss.tracer_rond(55, 155)
        elif case == 5:
            self.boss.tracer_rond(155, 155)
        elif case == 6:
            self.boss.tracer_rond(255, 155)
        elif case == 7:
            self.boss.tracer_rond(55, 255)
        elif case == 8:
            self.boss.tracer_rond(155, 255)
        elif case == 9:
            self.boss.tracer_rond(255, 255)
        
if __name__ == '__main__':
    fen = Application()
    fen.mainloop()

