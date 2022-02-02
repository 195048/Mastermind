from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import *
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.base import runTouchApp
from kivy.uix.spinner import Spinner
import random
from kivy.graphics import Color, Rectangle
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.image import Image, AsyncImage
from kivy.uix.widget import Widget 
from kivy.core.audio import SoundLoader
from kivy.core.text import FontContextManager as FCM

Victoire = SoundLoader.load('12. STAND PROUD.mp3')
menu = SoundLoader.load("gt1.mp3")
lose = SoundLoader.load("Super Mario Dies Sound Effect.mp3")


import json
import os 
import sys
import time


print (sys.argv[0])

Window.clearcolor = (0.06,0.19,0.06,1)
Window.size = (960 ,  720)



#Creation d'une liste contenant la reponse du jeu produite aléatoirement

numberList = ["Rouge","Bleu","Vert","Jaune","Noir","Blanc"]
Couleur1 = (random.choice(numberList))
Couleur2 = (random.choice(numberList))
Couleur3 = (random.choice(numberList))
Couleur4 = (random.choice(numberList))
Reponse = [Couleur1, Couleur2, Couleur3, Couleur4]

#print(Reponse)


class Mastermind(App):


    #Variables du screen manager
    
    def build(self):
        self.__manager = ScreenManager()
        self.__manager.add_widget(self.buildScreenX())
        self.__manager.add_widget(self.buildScreen1())
        self.__manager.add_widget(self.buildScreen2())
        self.__manager.add_widget(self.buildScreen3())
        return self.__manager
    

    #screen Intro pour le joeur
    
    def buildScreenX(self):
        menu.play()
        screen = Screen(name="screenX")
        box = BoxLayout(orientation="vertical")
        line19 = BoxLayout(orientation="horizontal")
        line20 = BoxLayout(orientation="horizontal")
        line21 = BoxLayout(orientation="horizontal")

        
        line19.add_widget(Label(font_size=22, text="Bienvenue dans MasterMind"))
        line20.add_widget(Label(text="Insérez votre Pseudo"))
        
        self.joueur=TextInput(font_size=18,size_hint=(0.5,1),multiline=False)
        self.joueur.bind(on_text_validate=self.toScreen1)
        


        line20.add_widget(self.joueur)
        
        bleu = Button(text='Pour continuer cliquez ici ou appuyez sur la touche Enter')
        bleu.bind(on_press=self.toScreen1)
        
        
        line21.add_widget(bleu)

        box.add_widget(line19)
        box.add_widget(line20)
        box.add_widget(line21)
        screen.add_widget(box)
        
        
        return screen


    #Ecran de Jeu

    def buildScreen1(self):
        screen = Screen(name="screen1")
        root = BoxLayout(orientation="vertical")
        line1 = BoxLayout(orientation="horizontal",size_hint=(1,2))
        line2 = BoxLayout(orientation="horizontal")
        line3 = BoxLayout(orientation="horizontal")
        line4 = BoxLayout(orientation="horizontal")
        line5 = BoxLayout(orientation="horizontal")
        line6 = BoxLayout(orientation="horizontal")
        line7 = BoxLayout(orientation="horizontal")
        line8 = BoxLayout(orientation="horizontal")
        line9 = BoxLayout(orientation="horizontal")
        line10 = BoxLayout(orientation="horizontal")
        line11 = BoxLayout(orientation="horizontal")
        line12 = BoxLayout(orientation="horizontal")
        line13 = BoxLayout(orientation="horizontal")

        
        #retour menu
        
        self.Menu = Button(text='Menu')
        
        self.Menu.bind(on_press = self.toScreenX)
        line1.add_widget(self.Menu)
        
        
        #affichage du meilleur score
        self.score = Button(font_size=18,text=self.top()+"\n             Etes vous capable de le battre? ",size_hint=(3,1))
        line1.add_widget(self.score)
        
        
        #Tentative s'ajouter un bouton restart sans succes
        #def restart(self):
        #    python = sys.executable
        #    os.execl(python, python, * sys.argv)
        
        #os.execv(sys.executable, ['python'] + sys.argv)
        #self.Menu.bind(on_press=restart(self))


        #bouton quitter

        self.Quitter = Button(text='Quitter')
        line1.add_widget(self.Quitter)
        self.Quitter.bind(on_press = lambda b: Mastermind.stop(self))
        

    

        
            
        
      
        #Creation des cases du jeu
        #buttons preferes au label car facilité de les colorier sans problemes(bug lors du changement de la taille d'ecran)
        
        self.output152=Button(text="Que la Force soit avec toi", size_hint=(4,1))
        self.output152.background_color = (255, 255, 255, 0.8)
        self.output152.color = (0,0,0,1)
        self.output151 = Label(text="Couleur")
        self.output150 = Label(text="OK")
        line2.add_widget(self.output152)
        line2.add_widget(self.output150)
        line2.add_widget(self.output151)
        
       
       


        self.output1=Button()
        self.output2=Button()
        self.output3=Button()
        self.output4=Button()
        line3.add_widget(self.output1)
        line3.add_widget(self.output2)
        line3.add_widget(self.output3)
        line3.add_widget(self.output4)
        self.output5=Label()
        line3.add_widget(self.output5)
        self.output70=Label()
        line3.add_widget(self.output70)
       

        self.output51=Button()
        self.output6=Button()
        self.output7=Button()
        self.output8=Button()
        line4.add_widget(self.output51)
        line4.add_widget(self.output6)
        line4.add_widget(self.output7)
        line4.add_widget(self.output8)
        self.output9=Label()
        line4.add_widget(self.output9)
        self.output71=Label()
        line4.add_widget(self.output71)
        


        self.output10=Button()
        self.output11=Button()
        self.output12=Button()
        self.output13=Button()
        line5.add_widget(self.output10)
        line5.add_widget(self.output11)
        line5.add_widget(self.output12)
        line5.add_widget(self.output13)
        self.output14 = Label()
        line5.add_widget(self.output14)
        self.output72=Label()
        line5.add_widget(self.output72)

        self.output15=Button()
        self.output16=Button()
        self.output17=Button()
        self.output18=Button()
        line6.add_widget(self.output15)
        line6.add_widget(self.output16)
        line6.add_widget(self.output17)
        line6.add_widget(self.output18)
        self.output19 = Label()
        line6.add_widget(self.output19)
        self.output73=Label()
        line6.add_widget(self.output73)

        self.output20=Button()
        self.output21=Button()
        self.output22=Button()
        self.output23=Button()
        line7.add_widget(self.output20)
        line7.add_widget(self.output21)
        line7.add_widget(self.output22)
        line7.add_widget(self.output23)
        self.output24 = Label()
        line7.add_widget(self.output24)
        self.output74=Label()
        line7.add_widget(self.output74)

        self.output25=Button()
        self.output26=Button()
        self.output27=Button()
        self.output28=Button()
        line8.add_widget(self.output25)
        line8.add_widget(self.output26)
        line8.add_widget(self.output27)
        line8.add_widget(self.output28)
        self.output29 = Label()
        line8.add_widget(self.output29)
        self.output75=Label()
        line8.add_widget(self.output75)

        self.output30=Button()
        self.output31=Button()
        self.output32=Button()
        self.output33=Button()
        line9.add_widget(self.output30)
        line9.add_widget(self.output31)
        line9.add_widget(self.output32)
        line9.add_widget(self.output33)
        self.output34 = Label()
        line9.add_widget(self.output34)
        self.output76=Label()
        line9.add_widget(self.output76)

        

        self.output35=Button()
        self.output36=Button()
        self.output37=Button()
        self.output38=Button()
        line10.add_widget(self.output35)
        line10.add_widget(self.output36)
        line10.add_widget(self.output37)
        line10.add_widget(self.output38)
        self.output39 = Label()
        line10.add_widget(self.output39)
        self.output77=Label()
        line10.add_widget(self.output77)


        self.output40=Button()
        self.output41=Button()
        self.output42=Button()
        self.output43=Button()
        line11.add_widget(self.output40)
        line11.add_widget(self.output41)
        line11.add_widget(self.output42)
        line11.add_widget(self.output43)
        self.output44 = Label()
        line11.add_widget(self.output44)
        self.output78=Label()
        line11.add_widget(self.output78)



        self.output45=Button()
        self.output46=Button()
        self.output47=Button()
        self.output48=Button()
        line12.add_widget(self.output45)
        line12.add_widget(self.output46)
        line12.add_widget(self.output47)
        line12.add_widget(self.output48)
        self.output49 = Label()
        line12.add_widget(self.output49)
        self.output79=Label()
        line12.add_widget(self.output79)

     



        #parametrage des spinners avec valeurs affichees au debut + valeurs selectionnables


        button= Button(size_hint=(2,1),text ="Valider")
        self.spinner1 = Spinner(text = "Couleur", values=["Rouge","Bleu","Vert","Jaune","Noir","Blanc"])
        self.spinner2 = Spinner(text = "Couleur", values=["Rouge","Bleu","Vert","Jaune","Noir","Blanc"])
        self.spinner3 = Spinner(text = "Couleur", values=["Rouge","Bleu","Vert","Jaune","Noir","Blanc"])
        self.spinner4 = Spinner(text = "Couleur", values=["Rouge","Bleu","Vert","Jaune","Noir","Blanc"])
        line13.add_widget(self.spinner1)
        line13.add_widget(self.spinner2)
        line13.add_widget(self.spinner3)
        line13.add_widget(self.spinner4)
        line13.add_widget(button)


        #Bouton valider 

        button.bind(on_press=self.action)
        

        root.add_widget(line1)
        root.add_widget(line2)
        root.add_widget(line3)
        root.add_widget(line4)
        root.add_widget(line5)
        root.add_widget(line6)
        root.add_widget(line7)
        root.add_widget(line8)
        root.add_widget(line9)
        root.add_widget(line10)
        root.add_widget(line11) 
        root.add_widget(line12)
        root.add_widget(line13)
        
        screen.add_widget(root)


        return screen

    





    def action(self,source, *args):

        #print(self.meilleurscore())


        #création d'un compteur permettant de calculer le nombre de tentabtives restantes 

        tour = 0

        #Reaffectation des spinners une fois que ceux ci ont affecte une valeur a la ligne designee 

        #spinner1
        if self.output1.text != "":
            tour = 1
            self.output1 = self.output51
        if self.output51.text != "":
            self.output1 = self.output10
            tour = 2
        if self.output10.text != "":
            self.output1 = self.output15
            tour = 3
        if self.output15.text != "":
            tour = 4
            self.output1 = self.output20
        if self.output20.text != "":
            tour = 5
            self.output1 = self.output25
        if self.output25.text != "":
            tour = 6
            self.output1 = self.output30
        if self.output30.text != "":
            tour = 7
            self.output1 = self.output35
        if self.output35.text != "":
            tour = 8
            self.output1 = self.output40
        if self.output40.text != "":
            self.output1 = self.output45
            tour = 9
        #spinner2
        if self.output2.text != "":
            self.output2 = self.output6
        if self.output6.text != "":
            self.output2 = self.output11
        if self.output11.text != "":
            self.output2 = self.output16
        if self.output16.text != "":
            self.output2 = self.output21
        if self.output21.text != "":
            self.output2 = self.output26
        if self.output26.text != "":
            self.output2 = self.output31
        if self.output31.text != "":
            self.output2 = self.output36
        if self.output36.text != "":
            self.output2 = self.output41
        if self.output41.text != "":
            self.output2 = self.output46
        if self.output46.text != "":
            self.output2 != self.output46
        
        #spinner3
        if self.output3.text != "":
            self.output3 = self.output7
        if self.output7.text != "":
            self.output3 = self.output12
        if self.output12.text != "":
            self.output3 = self.output17
        if self.output17.text != "":
            self.output3 = self.output22
        if self.output22.text != "":
            self.output3 = self.output27
        if self.output27.text != "":
            self.output3 = self.output32
        if self.output32.text != "":
            self.output3 = self.output37
        if self.output37.text != "":
            self.output3 = self.output42
        if self.output42.text != "":
            self.output3 = self.output47
        
        #spinner4
        if self.output4.text != "":
            self.output4 = self.output8
        if self.output8.text != "":
            self.output4 = self.output13
        if self.output13.text != "":
            self.output4 = self.output18
        if self.output18.text != "":
            self.output4 = self.output23
        if self.output23.text != "":
            self.output4 = self.output28
        if self.output28.text != "":
            self.output4 = self.output33
        if self.output33.text != "":
            self.output4 = self.output38
        if self.output38.text != "":
            self.output4 = self.output43
        if self.output43.text != "":
            self.output4 = self.output48


        self.output1.text = "{}".format(self.spinner1.text)
        self.output2.text = "{}".format(self.spinner2.text)
        self.output3.text = "{}".format(self.spinner3.text)
        self.output4.text = "{}".format(self.spinner4.text)

        
        
    
        
        #Couleur spinner 1            
       
        if self.spinner1.text == "Rouge":
            self.output1.color = (1,0,0,0)
            self.output1.background_color = (255,0,0,0.7)
        if self.spinner1.text == "Jaune":
            self.output1.color = (1,0,0,0)
            self.output1.background_color = (255,255,0,0.8)    
        if self.spinner1.text == "Bleu":
            self.output1.color = (1,0,0,0)
            self.output1.background_color = (0,0,255,0.6)
        if self.spinner1.text == "Vert":
            self.output1.color = (0,128,0,0)
            self.output1.background_color = (0,128,0,0.8)
        if self.spinner1.text == "Noir":
            self.output1.color = (0,0,0,1)
            self.output1.background_color = (0,0,0,1)
        if self.spinner1.text == "Blanc":
            self.output1.color = (255,255,255,0)
            self.output1.background_color = (255,255,255,1)
        
         #Couleur spinner 2 

        if self.spinner2.text == "Rouge":
            self.output2.color = (1,0,0,0)
            self.output2.background_color = (255,0,0,0.7)
        if self.spinner2.text == "Jaune":
            self.output2.color = (1,0,0,0)
            self.output2.background_color = (255,255,0,0.8)    
        if self.spinner2.text == "Bleu":
            self.output2.color = (1,0,0,0)
            self.output2.background_color = (0,0,255,0.6)
        if self.spinner2.text == "Vert":
            self.output2.color = (0,128,0,0)
            self.output2.background_color = (0,128,0,0.8)
        if self.spinner2.text == "Noir":
            self.output2.color = (0,0,0,1)
            self.output2.background_color = (0,0,0,1)
        if self.spinner2.text == "Blanc":
            self.output2.color = (255,255,255,0)
            self.output2.background_color = (255,255,255,1)

         #Couleur spinner 3 

        if self.spinner3.text == "Rouge":
            self.output3.color = (1,0,0,0)
            self.output3.background_color = (255,0,0,0.7)
        if self.spinner3.text == "Jaune":
            self.output3.color = (1,0,0,0)
            self.output3.background_color = (255,255,0,0.8)    
        if self.spinner3.text == "Bleu":
            self.output3.color = (1,0,0,0)
            self.output3.background_color = (0,0,255,0.6)
        if self.spinner3.text == "Vert":
            self.output3.color = (0,128,0,0)
            self.output3.background_color = (0,128,0,0.8)
        if self.spinner3.text == "Noir":
            self.output3.color = (0,0,0,1)
            self.output3.background_color = (0,0,0,1)
        if self.spinner3.text == "Blanc":
            self.output3.color = (255,255,255,0)
            self.output3.background_color = (255,255,255,1)

         #Couleur spinner 4


        if self.spinner4.text == "Rouge":
            self.output4.color = (1,0,0,0)
            self.output4.background_color = (255,0,0,0.7)
        if self.spinner4.text == "Jaune":
            self.output4.color = (1,0,0,0)
            self.output4.background_color = (255,255,0,0.8)    
        if self.spinner4.text == "Bleu":
            self.output4.color = (1,0,0,0)
            self.output4.background_color = (0,0,255,0.6)
        if self.spinner4.text == "Vert":
            self.output4.color = (0,128,0,0)
            self.output4.background_color = (0,128,0,0.8)
        if self.spinner4.text == "Noir":
            self.output4.color = (0,0,0,1)
            self.output4.background_color = (0,0,0,1)
        if self.spinner4.text == "Blanc":
            self.output4.color = (255,255,255,0)
            self.output4.background_color = (255,255,255,1)
        

        
        #Liste crée a partir du choix du joueur 

        Choix = []
        Choix.append(self.output1.text)
        Choix.append(self.output2.text)
        Choix.append(self.output3.text)
        Choix.append(self.output4.text)
        
        
        score8 = 9 - tour
        #print(score8)  
        

        #mechanisme du jeu concernant la victoire/defaite

        if Reponse == Choix: 
            Victoire.play()
            menu.stop()
            
            self.toScreen2(source)
            self.output152.text = "N'essayez pas de changer la combinaison bande de tricheurs"
            self.json(score8,self.joueur.text)
            #print(Reponse)
            
            
        

        
        
        if  Reponse != Choix :
            
            self.output152.text = "Ah shit, here we go again"
        if (self.output1 == self.output51) and Reponse != Choix :
            
            self.output152.text = "Vous, vous êtes incroyablement courageux!"
        if (self.output1 == self.output10) and Reponse != Choix :
            
            self.output152.text = "Never give up. Trust your Instincts."
        if (self.output1 == self.output15) and Reponse != Choix :
            
            self.output152.text = "Qui tente rien n'a rien je prends des gros risques j'ai rien"
        if (self.output1 == self.output20) and Reponse != Choix :
            
            self.output152.text = "Frustration : IT'S OVER 9000 "
        if (self.output1 == self.output25) and Reponse != Choix :
            
            self.output152.text = "The case is a lie"
        if (self.output1 == self.output30) and Reponse != Choix :
            
            self.output152.text = "Vous devez réunir vos neurones avant d’aller plus loin"
        if (self.output1 == self.output35) and Reponse != Choix :
            self.output152.text = "Petit Conseil : On ne fait pas d'omelette sans casser des oeufs"
            
        if (self.output1 == self.output40) and Reponse != Choix :
            self.output152.text = "Thank you Mario! But the color is in another case"
            
        if (self.output1 == self.output45) and Reponse != Choix :
            self.output152.text = "N'essayez pas de changer la combinaison cela ne sert a rien"
            self.json(score8,self.joueur.text)
            lose.play()
            menu.stop()
            self.toScreen3(source)
            
            
            
            
            
        
            
            
            
        #print(tour)   

        

        #Mechanisme des indices

        def common(Reponse, Choix):
            intersection = [e for e in Reponse if e in Choix] 
            elemnts_counters = {e: min(Reponse.count(e), Choix.count(e)) for e in intersection} 
            return sum([[e] * c for e, c in elemnts_counters.items()], []) 

        #Couleurs valides
        A = common(Reponse, Choix)
        #print(A)
        #print(len(A))

        #Bonne Couleur et bonne Place
        B = sum(1 if x == y else 0 for x, y in zip(Reponse,Choix))


        #print(Reponse)
        #print(Choix)

        #Bonne couleur et Mauvaise Place

        def correct( Reponse, Choix):
            counter = len(A)
            return counter-B

        D = correct(Reponse,Choix)

        #print(D)

        
        #passage a la ligne des indicateurs


        self.output5.text = "{}".format(B)
        self.output70.text = "{}".format(D)

        
        if self.output5.text != "":
            self.output5 = self.output9
            self.output70= self.output71
        if self.output9.text != "":
            self.output5 = self.output14
            self.output70= self.output72
        if self.output14.text != "":
            self.output5 = self.output19
            self.output70= self.output73
        if self.output19.text != "":
            self.output5 = self.output24
            self.output70= self.output74
        if self.output24.text != "":
            self.output5 = self.output29
            self.output70= self.output75
        if self.output29.text != "":
            self.output5 = self.output34
            self.output70= self.output76
        if self.output34.text != "":
            self.output5 = self.output39
            self.output70= self.output77
        if self.output39.text != "":
            self.output5 = self.output44
            self.output70= self.output78
        if self.output44.text != "":
            self.output5 = self.output49
            self.output70= self.output79


        

    
    #fichier json contenant les scores et les noms du joueur 



    def json(self,score,nom):
        try:
	        with open("res.json") as file:
		        res = json.loads(file.read())
        except FileNotFoundError:
	            # si le fichier n'existe pas, on part d'une liste vide
	        res = []

        name = nom
        score = score

        res.append({
	        "name": name,
	        "score": score
        })

        with open("res.json", 'w') as file:
	        file.write(json.dumps(res, indent='\t'))


    #Affichage du meilleur score 


    def top(self):
        try:
	        with open("res.json") as file:
		        res = json.loads(file.read())
        except FileNotFoundError:
	            # si le fichier n'existe pas, on part d'une liste vide
	        res = []

        bestscore = 0
        namescore = ""
        
        for element in res :
            if element["score"]>(bestscore) :
                bestscore = element["score"]
                namescore = element["name"]
        return "{}{}{}{}".format("Le meilleur score est de ",bestscore," détenu par ",namescore)


    #print(top)
   
    #WIN SCREEN
    def buildScreen2(self, *args):
        screen = Screen(name="screen2")
        box = BoxLayout(orientation="vertical")
        line25 = BoxLayout(orientation="horizontal", size_hint=(1,0.2))
        
        ximg = AsyncImage(source='86170984.jpg')

       
        


        self.retour = Button(text='Retour',size_hint= (1,1))
        line25.add_widget(self.retour)
        self.retour.bind(on_press = self.toScreen1)
        
        
        self.plein =Button(font_size=22,text= "                   Je dois l'avouer petit \n tu m'as impressioné. Profite de ta victoire",size_hint=(4,1))
        line25.add_widget(self.plein)

        self.Quitter = Button(text='Quitter',size_hint= (1,1))
        line25.add_widget(self.Quitter)
        self.Quitter.bind(on_press = lambda b: Mastermind.stop(self))
       
        
       
        screen.add_widget(ximg)
        box.add_widget(line25)
       
        box.add_widget(Label(text=""))       
        
        screen.add_widget(box)



        
        
        return screen

    #LOSE SCREEN

    def buildScreen3(self):
        screen = Screen(name="screen3")
        box = BoxLayout(orientation="vertical")
        
        
        
        line25 = BoxLayout(orientation="horizontal", size_hint=(1,0.2))
        line26 = BoxLayout(orientation="horizontal", size_hint=(1,0.2))
        



        
        
        wimg = AsyncImage(source='bucket.jpg')
        


        

        self.retour = Button(text='Retour',size_hint= (1,1))
        line25.add_widget(self.retour)
        self.retour.bind(on_press = self.toScreen1)
        
        
        self.plein =Button(font_size=22,text = "The only thing that can defeat power, is more power", size_hint=(4,1))
        line25.add_widget(self.plein)

        self.Quitter = Button(text='Quitter',size_hint= (1,1))
        line25.add_widget(self.Quitter)
        self.Quitter.bind(on_press = lambda b: Mastermind.stop(self))

        self.correct =Button(font_size=22,text ="La bonne reponse était :     " + Reponse[0] + "     " + Reponse[1] + "      " + Reponse[2] + "      " + Reponse[3] , size_hint=(4,1))
        line26.add_widget(self.correct)
       
        
       
        screen.add_widget(wimg)
        box.add_widget(line25)
        box.add_widget(Label(text=""))
        box.add_widget(line26)

        screen.add_widget(box)
       
        return screen 
    

    def toScreen3(self, source):
		# Use the name of the destination Screen
        self.__manager.current = "screen3"

    def toScreen2(self, source):
		# Use the name of the destination Screen
        self.__manager.current = "screen2"

    def toScreen1(self, source):
        self.__manager.current = "screen1"

    def toScreenX(self, source):
        self.__manager.current = "screenX"



Mastermind().run()

