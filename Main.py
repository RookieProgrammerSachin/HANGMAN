import pygame
import random
from pygame import mixer

pygame.init()

#Setting up window to display the game
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("HANGMAN")
pygame.display.set_icon(pygame.image.load(r"Assets\Images\Logo\logo_beta.png"))
clock = pygame.time.Clock()

#---------------------------------------------------------------------------

    #Loading Background for the game
bg = pygame.image.load(r"Assets\Images\BG\bg7.jpeg")

    #Loading Background music
mixer.music.load(r'Assets\Sounds\bgm_final.wav')
mixer.music.play(-1)

    #Loading clickSound - Sound to play when you click a button
clickSound = mixer.Sound(r'Assets\Sounds\clickSound.wav')

    #Loading lostSound - Sound to play when you lose a game
lostSound = mixer.Sound(r'Assets\Sounds\lostSound.wav')

    #Loading wonSound - Sound to play when you win a game
wonSound = mixer.Sound(r'Assets\Sounds\wonSound.wav')

    #Loading wrongSound - Sound to play when you get wrong answer
wrongSound = mixer.Sound(r'Assets\Sounds\wrongSound.wav')

    #Loading nope - Image to display when sound or BGM is disabled
nope = pygame.image.load(r'Assets\Images\UI\nope.png')

    #Loading image bgm - Image/Button to toggle BGM ON/OFF
bgm = pygame.image.load(r"Assets\Images\UI\music.png")

    #Loading image sfx - Image/Button to toggle SFX ON/OFF
sfx = pygame.image.load(r"Assets\Images\UI\sfx.png")

    #Loading XP close button - To close the game
close_button = pygame.image.load(r"Assets\Images\UI\close.png")

    #Loading XP help button - To get help about game
help_button = pygame.image.load(r"Assets\Images\UI\help.png")

    #Loading XP info button - To get info about game
info_button = pygame.image.load(r"Assets\Images\UI\info.png")

    #Loading help box image
text_box = pygame.image.load(r"Assets\Images\UI\box_beta.png")
text_box = pygame.transform.scale(text_box,(420,220))
info_click = False
cred_click = False
nope_click_bgm = False
nope_click_sfx = False

    #UI font
ui_font = pygame.font.Font('freesansbold.ttf',16)

#Text to render when help/info button is clicked
info_text = ["Welcome! This is the classic HANGMAN",
             "game. Various letters of random words",
             "will be missing and you have to find",
             "out those words. But each wrong",
             "selection progressively leads to our",
             "man being hung. Hope you enjoy :)"]
cred_text = ["HANGMAN Project using pygame by:",
             "      Sachin - Code",
             "      Seetharaman - Audio",
             "      Adarsh - UI"]

#Fucntion Help button text             
def draw_text_box():
    if info_click == True:
        screen.blit(text_box, (260,120))
        screen.blit(close_button,(260+275,130))
        info_text_y = 175
        for x in info_text:
            screen.blit(ui_font.render(x, True, (0,0,0)),(283,info_text_y))
            info_text_y += 22

#Credits text
def draw_info_box():
    if cred_click == True:
        screen.blit(text_box, (260,120))
        screen.blit(close_button,(260+275,130))
        cred_text_y = 180
        for z in cred_text:
            screen.blit(ui_font.render(z, True, (0,0,0)),(283,cred_text_y))
            cred_text_y += 22

#draw bgm? button
def draw_bgm():
    screen.blit(bgm,(20,33))
    if nope_click_bgm == True:
        screen.blit(nope,(20,33))

#draw sfx? button
def draw_sfx():
    screen.blit(sfx,(60,33))
    if nope_click_sfx == True:
        screen.blit(nope,(60,33))

#wonSound play
def wonSound_play():
    if nope_click_sfx != True:
        wonSound.play()

#clickSound play
def clickSound_play():
    if nope_click_sfx != True:
        clickSound.play()

#wrongSound play
def wrongSound_play():
    if nope_click_sfx != True:
        wrongSound.play()

#lostSound play
def lostSound_play():
    if nope_click_sfx != True:
        lostSound.play()

        
#------------------------------------------------------------------
        
#hangman_load - Loading 2D image of the main HANGMAN character = 9 different images involving dying progress
h1 = pygame.image.load(r"Assets\Images\main\final\1.png")
h1 = pygame.transform.scale(h1, (400,300))
h2 = pygame.image.load(r"Assets\Images\main\final\2.png")
h2 = pygame.transform.scale(h2, (400,300))
h3 = pygame.image.load(r"Assets\Images\main\final\3.png")
h3 = pygame.transform.scale(h3, (400,300))
h4 = pygame.image.load(r"Assets\Images\main\final\4.png")
h4 = pygame.transform.scale(h4, (400,300))
h5 = pygame.image.load(r"Assets\Images\main\final\5.png")
h5 = pygame.transform.scale(h5, (400,300))
h6 = pygame.image.load(r"Assets\Images\main\final\6.png")
h6 = pygame.transform.scale(h6, (400,300))
h7 = pygame.image.load(r"Assets\Images\main\final\7.png")
h7 = pygame.transform.scale(h7, (400,300))
h8 = pygame.image.load(r"Assets\Images\main\final\8.png")
h8 = pygame.transform.scale(h8, (400,300))
h9 = pygame.image.load(r"Assets\Images\main\final\9.png")
h9 = pygame.transform.scale(h9, (400,300))

#--------------------------------------------------------------

#Creatign a class Button to draw A-Z in the screen for user to select
class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None): #Call this method to draw the button on the screen
        
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.Font('freesansbold.ttf', 26)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + 2 + (self.height/2 - text.get_height()/2)))


    def isOver(self, mouse_pos):
        if mouse_pos[0] > self.x and mouse_pos[0] < self.x + self.width:
            if mouse_pos[1] > self.y and mouse_pos[1] < self.y + self.height:
                return True
        
        return False

#---------------------------------------------------------------------------
#Main Title - Render the main title "HANGMAN" 
title_font = pygame.font.Font('freesansbold.ttf',32)

def showtitle():
    title = title_font.render("H A N G M A N", True, (255,255,245))
    screen.blit(title,(300,10))

#---------------------------------------------------------------------------
#Line - Render a line below Title
line_font = pygame.font.Font('freesansbold.ttf',32)
    
def showline():
    line = line_font.render("_______________", True, (255,255,245))
    screen.blit(line,(10,-4))

def showline_2():
    line = line_font.render("______________", True, (255,255,245))
    screen.blit(line,(538,-4))

#---------------------------------------------------------------------------

#Script for rendering main word showcase
scrtxt_font = pygame.font.SysFont('algerian',40)

def word_render(wordo):
    main_line = scrtxt_font.render(wordo.upper(),True,(255,255,255))
    screen.blit(main_line,((800/2 - main_line.get_width()/2),435))
    
#---------------------------------------------------------------------------

#This is the collection of words to be selected at random
words_list = ["memorize","belong","label","hammer","pretend","support",\
              "hangman",'acidic','basic','neutral','peptide','halfway',\
              'whatsapp','friends','tenet',\
              'blockbuster','whatever',"images","bottle","pendrive","computer",\
              "science","project","important","circuit","diode","wonder","superman",\
              "batman","ironman","captain","America","black","widow","flash",\
              "witch","clock","headphones","earphones","screen","young","television",\
              "presenting","transparent","glasses","games","laptop","desktop",\
              "mathematics","chemistry","physics","biology","geography","history",\
              "civics","economics","engineering","alarm","earthquake","Rockstar",\
              "movies","actors","directors","matador","Lamborghini","Ferrari",\
              "mustang","youtube","google","perfect","resolution","emitting",\
              "pencils","schools","skyscraper","writer","producer","driver","mental",\
              "institute","excellence","chicken","meeting","leave","holiday"]

#----------------------------------------------------------------------------

#New style of selcting letters

def main_again():
    global word_mod
    global the_word
    global random_word_picker
    
    random_word_picker = random.randint(0,((len(words_list))-1))
    the_word = words_list[random_word_picker]  #The random word that has been chosen
    
    word_mod = ''

    #The actual algorithm to determine where to put in spaces/blanks with regards to the length of the word
    if len(the_word) in range(5,9):
        for x in range(len(the_word)):
            
            if x == 0:
                word_mod += the_word[x]
                
            elif x == int((int(len(the_word)/2))-(random.randint(0,1))):
                word_mod += the_word[x]
                
            elif x == (len(the_word)-1):
                word_mod += the_word[x]
                
            else:
                word_mod += "_"

                
    elif len(the_word) in range(9,12):
        for x in range(len(the_word)):
            
            if x == 0:
                word_mod += the_word[x]
                
            elif x == int((int(len(the_word)/2))-(random.randint(1,2))):
                word_mod += the_word[x]
                
            elif x == int((int(len(the_word)/2))+(random.randint(1,2))):
                word_mod += the_word[x]
                
            elif x == (len(the_word)-1):
                word_mod += the_word[x]
                
            else:
                word_mod += "_"
                

    elif len(the_word) in range(12,17):
        for x in range(len(the_word)):
            
            if x == 0:
                word_mod += the_word[x]
                
            elif x == int((int(len(the_word)/2))-(random.randint(3,4))):
                word_mod += the_word[x]
                
            elif x == int((int(len(the_word)/2))+(random.randint(3,4))):
                word_mod += the_word[x]
                
            elif x == (len(the_word)-1):
                word_mod += the_word[x]
                
            else:
                word_mod += "_"

main_again()

#----------------------------------------------------------------------------
        
#Creating boolean to check player has won
hasWon =  False

#----------------------------------------------------------------------------

#Loading images and assets to draw "WON" box
playagain_font = pygame.font.Font('freesansbold.ttf',28)
theword_font = pygame.font.SysFont('algerian',34)
theword_font.set_underline(0.9)
theword_render = theword_font.render(the_word.upper(),True,(0,0,0))

win_box = pygame.image.load(r"Assets\Images\UI\won_box_b2.png")
win_box = pygame.transform.scale(win_box,(320,320))
lost_box = pygame.transform.scale(win_box,(110+(theword_render.get_width())+110,400))
wonlost_font = pygame.font.Font('freesansbold.ttf',32)
tick_mark = pygame.image.load(r"Assets\Images\UI\tick_final.png")

def won_box():  
    if hasWon == True:
        screen.blit(win_box, ((800/2 - win_box.get_width()/2),(170)))
        wonlost_render = wonlost_font.render("You WON!",True,(0,0,0))
        playagain_render = playagain_font.render("Play more?",True,(0,0,0))
        screen.blit(wonlost_render,((325,250-20)))
        screen.blit(playagain_render,((325,320-40)))
        screen.blit(tick_mark, (325, 310))
        screen.blit(close_button, (325+64+8,320))

#----------------------------------------------------------------------------
#main character drawing :)
def hand_draw(chance):
    
    theword_render = theword_font.render(the_word.upper(),True,(0,0,0))
    lost_box = pygame.transform.scale(win_box,(110+(theword_render.get_width())+110,400))

    if chance == 8:
        screen.blit(h1, (210,90))
    if chance == 7:
        screen.blit(h1, (-500,-500))
        screen.blit(h2, (210,90))
    if chance == 6:
        screen.blit(h2, (-500,-500))
        screen.blit(h3, (210,90))
    if chance == 5:
        screen.blit(h3, (-500,-500))
        screen.blit(h4, (210,90))
    if chance == 4:
        screen.blit(h4, (-500,-500))
        screen.blit(h5, (210,90))
    if chance == 3:
        screen.blit(h5, (-500,-500))
        screen.blit(h6, (210,90))
    if chance == 2:
        screen.blit(h6, (-500,-500))
        screen.blit(h7, (210,90))
    if chance == 1:
        screen.blit(h7, (-500,-500))
        screen.blit(h8, (210,90))                    
    if chance < 1:
        screen.blit(h8, (-500,-500))
        screen.blit(h9, (210,90))

        #Drawing the box for "YOU LOST"       
        screen.blit(lost_box, ((800/2 - lost_box.get_width()/2),(105)))
        wonlost_render = wonlost_font.render("You LOST!",True,(0,0,0))
        playagain_render = playagain_font.render("Try again?",True,(0,0,0))
        screen.blit(theword_render,((800/2 - theword_render.get_width()/2),(220)))
        screen.blit(wonlost_render,((800/2 - wonlost_render.get_width()/2),250-80))
        screen.blit(tick_mark, (325, 300))
        screen.blit(playagain_render,((800/2 - playagain_render.get_width()/2),320-45))
        screen.blit(close_button, (325+64+8,315))

#----------------------------------------------------------------------------

total_chance = 8

#The actual main algo for playing
def letter_check(the_letter):
    global word_mod
    global total_chance
    global hasWon
    
    if total_chance != 0:
        
        if the_word != word_mod:
            
            if the_letter.lower() in the_word:
                
                ind_list = []
                
                for ind,val in enumerate(the_word):
                    if word_mod[ind] == "_":
                        if the_letter.lower() == the_word[ind]:
                            ind_list.append(ind)
                            
                if ind_list != 0:
                    for iterator in ind_list:
                        word_mod = word_mod[:iterator]+the_letter.lower()+word_mod[iterator+1:]
                        print(word_mod)
                    if the_word == word_mod:
                        hasWon = True
                        wonSound_play()
                                    
            else:
                total_chance -= 1
                wrongSound_play()
                
                if total_chance < 1:
                    lostSound_play()
        
            
#----------------------------------------------------------------------------

#Main while loop for drawing stuff in window for 60 times a second using Clock.Tick method
over = False
while not over:

    #BG
    screen.blit(bg,(0,0))

    #Title
    showtitle()

    #line
    showline()
    showline_2()

    #close button
    screen.blit(close_button,(760-5,33))

    #info button
    screen.blit(info_button,(720-5,37))

    #help button
    screen.blit(help_button,(676-5,35))
    
    #Draw every single letter
    A = button((245,245,245),50,500,35,35,'A')
    A.draw(screen, (0,0,0))

    B = button((245,245,245),50+45,500,35,35,'B')
    B.draw(screen, (0,0,0))

    C = button((245,245,245),50+45+45,500,35,35,'C')
    C.draw(screen, (0,0,0))

    D = button((245,245,245),50+45+45+45,500,35,35,'D')
    D.draw(screen, (0,0,0))

    E = button((245,245,245),50+45+45+45+45,500,35,35,'E')
    E.draw(screen, (0,0,0))

    F = button((245,245,245),50+45+45+45+45+45,500,35,35,'F')
    F.draw(screen, (0,0,0))

    G = button((245,245,245),50+(45*6),500,35,35,'G')
    G.draw(screen, (0,0,0))

    H = button((245,245,245),50+(45*7),500,35,35,'H')
    H.draw(screen, (0,0,0))

    I = button((245,245,245),50+(45*8),500,35,35,'I')
    I.draw(screen, (0,0,0))

    J = button((245,245,245),50+(45*9),500,35,35,'J')
    J.draw(screen, (0,0,0))

    K = button((245,245,245),50+(45*10),500,35,35,'K')
    K.draw(screen, (0,0,0))

    L = button((245,245,245),50+(45*11),500,35,35,'L')
    L.draw(screen, (0,0,0))

    M = button((245,245,245),50+(45*12),500,35,35,'M')
    M.draw(screen, (0,0,0))

    N = button((245,245,245),50+(45*13),500,35,35,'N')
    N.draw(screen, (0,0,0))

    O = button((245,245,245),50+(45*14),500,35,35,'O')
    O.draw(screen, (0,0,0))

    P = button((245,245,245),50+(45*15),500,35,35,'P')
    P.draw(screen, (0,0,0))

    Q = button((245,245,245),50+(45*3),545,35,35,'Q')
    Q.draw(screen, (0,0,0))

    R = button((245,245,245),50+(45*4),545,35,35,'R')
    R.draw(screen, (0,0,0))

    S = button((245,245,245),50+(45*5),545,35,35,'S')
    S.draw(screen, (0,0,0))

    T = button((245,245,245),50+(45*6),545,35,35,'T')
    T.draw(screen, (0,0,0))

    U = button((245,245,245),50+(45*7),545,35,35,'U')
    U.draw(screen, (0,0,0))

    V = button((245,245,245),50+(45*8),545,35,35,'V')
    V.draw(screen, (0,0,0))

    W = button((245,245,245),50+(45*9),545,35,35,'W')
    W.draw(screen, (0,0,0))

    X = button((245,245,245),50+(45*10),545,35,35,'X')
    X.draw(screen, (0,0,0))

    Y = button((245,245,245),50+(45*11),545,35,35,'Y')
    Y.draw(screen, (0,0,0))

    Z = button((245,245,245),50+(45*12),545,35,35,'Z')
    Z.draw(screen, (0,0,0))
    
    #draw hangman
    hand_draw(total_chance)

    #main Word
    word_render(word_mod)

    #draw won box
    won_box()

    #draw text
    draw_text_box()

    #draw cred_box
    draw_info_box()


    #draw bgm?
    draw_bgm()

    #draw sfx?
    draw_sfx()

    
    #main
    for event in pygame.event.get():

       #close click
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            
            #close button click check
            if mouse_pos[0] in range (755,756+32) and mouse_pos[1] in range(33,34+32):
                print("[info] Game closed")
                clickSound_play()
                over = True

            #info button click check
            elif mouse_pos[0] in range (715,716+32) and mouse_pos[1] in range(37,38+32):
                print("[info] Credits shown")
                clickSound_play()
                cred_click = True
                info_click = False

            #help button click check
            elif mouse_pos[0] in range(671,672+32) and mouse_pos[1] in range(35,36+32):
                print("[info] Game help shown")
                clickSound_play()
                info_click = True
                cred_click = False

            #close dialog click check
            elif mouse_pos[0] in range(260+275,260+275+33) and mouse_pos[1] in range(130,131+32):
                print("[info] Dialog box closed")
                clickSound_play()
                info_click = False
                cred_click = False

            #bgm click check
            elif mouse_pos[0] in range(20,20+33) and mouse_pos[1] in range(33,33+33):
                                
                if nope_click_bgm == False:
                    nope_click_bgm = True
                    pygame.mixer.music.pause()
                    print("[info] BGM disabled")
                    clickSound_play()
                else:
                    nope_click_bgm = False
                    pygame.mixer.music.unpause()
                    print("[info] BGM enabled")
                    clickSound_play()

            #sfx click check
            elif mouse_pos[0] in range(60,60+33) and mouse_pos[1] in range(33,33+33):
                               
                if nope_click_sfx == False:
                    nope_click_sfx = True
                    print("[info] SFX disabled") 
                else:
                    nope_click_sfx = False
                    print("[info] SFX enabled")


            #A-Z ---------------------------
            elif A.isOver(mouse_pos):
                print("[info] selected A")
                letter_check(A.text)
                clickSound_play()

            elif B.isOver(mouse_pos):
                print("[info] selected B")
                letter_check(B.text)
                clickSound_play()
                
            elif C.isOver(mouse_pos):
                print("[info] selected C")
                letter_check(C.text)
                clickSound_play()

            elif D.isOver(mouse_pos):
                print("[info] selected D")
                letter_check(D.text)
                clickSound_play()

            elif E.isOver(mouse_pos):
                print("[info] selected E")
                letter_check(E.text)
                clickSound_play()

            elif F.isOver(mouse_pos):
                print("[info] selected F")
                letter_check(F.text)
                clickSound_play()

            elif G.isOver(mouse_pos):
                print("[info] selected G")
                letter_check(G.text)
                clickSound_play()
                
            elif H.isOver(mouse_pos):
                print("[info] selected H")
                letter_check(H.text)
                clickSound_play()
                
            elif I.isOver(mouse_pos):
                print("[info] selected I")
                letter_check(I.text)
                clickSound_play()

            elif J.isOver(mouse_pos):
                print("[info] selected J")
                letter_check(J.text)
                clickSound_play()

            elif K.isOver(mouse_pos):
                print("[info] selected K")
                letter_check(K.text)
                clickSound_play()

            elif L.isOver(mouse_pos):
                print("[info] selected L")
                letter_check(L.text)
                clickSound_play()

            elif M.isOver(mouse_pos):
                print("[info] selected M")
                letter_check(M.text)
                clickSound_play()

            elif N.isOver(mouse_pos):
                print("[info] selected N")
                letter_check(N.text)
                clickSound_play()

            elif O.isOver(mouse_pos):
                print("[info] selected O")
                letter_check(O.text)
                clickSound_play()

            elif P.isOver(mouse_pos):
                print("[info] selected P")
                letter_check(P.text)
                clickSound_play()

            elif Q.isOver(mouse_pos):
                print("[info] selected Q")
                letter_check(Q.text)
                clickSound_play()

            elif R.isOver(mouse_pos):
                letter_check(R.text)
                print("[info] selected R")
                clickSound_play()

            elif S.isOver(mouse_pos):
                print("[info] selected S")
                letter_check(S.text)
                clickSound_play()

            elif T.isOver(mouse_pos):
                print("[info] selected T")
                letter_check(T.text)
                clickSound_play()

            elif U.isOver(mouse_pos):
                print("[info] selected U")
                letter_check(U.text)
                clickSound_play()

            elif V.isOver(mouse_pos):
                print("[info] selected V")
                letter_check(V.text)
                clickSound_play()

            elif W.isOver(mouse_pos):
                print("[info] selected W")
                letter_check(W.text)
                clickSound_play()

            elif X.isOver(mouse_pos):
                print("[info] selected X")
                letter_check(X.text)
                clickSound_play()

            elif Y.isOver(mouse_pos):
                print("[info] selected Y")
                letter_check(Y.text)
                clickSound_play()

            elif Z.isOver(mouse_pos):
                print("[info] selected Z")
                letter_check(Z.text)
                clickSound_play()
                
            #------------------------ A-Z --------------------------

            elif (hasWon == True) and mouse_pos[0] in range(325,325+65) and mouse_pos[1] in range(310,310+65):
                total_chance = 8
                hasWon = False
                main_again()
                clickSound_play()

            elif (hasWon == True) and mouse_pos[0] in range(325+64+8,325+64+8+33) and mouse_pos[1] in range(320,320+33):
                hasWon = False
                clickSound_play()

            elif ((total_chance == 0) or (total_chance < 0)) and mouse_pos[0] in range(325,325+65) and mouse_pos[1] in range(310,310+65):
                total_chance = 8
                hasWon = False
                main_again()
                clickSound_play()

            elif ((total_chance == 0) or (total_chance < 0)) and mouse_pos[0] in range(325+64+8,325+64+8+33) and mouse_pos[1] in range(320,320+33):
                over = True
                clickSound_play()

                
        #game quit            
        if event.type == pygame.QUIT:
            over = True


    pygame.display.update() #To refresh the display for feeding in new input
    clock.tick(60)

#----------------------------------------------------------------------------
    
pygame.quit() #Last line to close the game when the while loop is terminated

#----------------------------------------------------------------------------

#Made by Sree Sachin. E, XII-B, started, 5-12-2020; ended, 10-12-2020. ;)
