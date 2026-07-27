#
# Code by: Revierr
# Date: 2/4/2025
# Filename: relationshipmenu.rpy
#
# This is a code asset for an easy plug in and play relationship menu for a Renpy visual novel!
#
# You may use this code for free, within any commercial or noncommercial projects, with or without credit! Thanks!
# If you credit me, please link it to my itch.io (https://revierr.itch.io/)

#YOUR TASKS ARE:
#1. Fill in the character names at line 20 and beyond
#2. Paste code starting at line 20 into script.rpy at the very top! (It works if you don't do this, but you want to make sure the game loads the variables first so it knows they exist.)
#3. Add a line in your script.rpy after the start label that says "show screen button" (If you're fancy, try "show screen button with dissolve")
#4. Have fun micromanaging your relationship points!

#THIS DOCUMENT IS AN EDIT OF THE ORIGINAL SCRIPT TO ADD MORE COLUMNS FOR MORE CHARACTERS! THIS HAS 8 BUILT IN BUT IT CAN BE EDITED FOR MORE OR LESS!
#I copied around a lot of the code so the comments may not be as coherent as the original script, so if you're confused please download the other one and take a peek. It may make more sense sequentially.


#Cut and paste the following code into the top of your script.rpy file. V


#Above code needs to go into script.rpy. ^

#Now, whenever you want to change the bar you change the variable character1affection.
#For example, to make the bar increase you put "$ character1affection += 10"


#This code defines the button that appears while the game is playing regularly.
screen button:
    # xalign and yalign are the positions on screen if you'd like to move it around.
    vbox xalign 0.95 yalign 0:

        imagebutton:
        #These are the visuals for the button. You can use the same image, or have it change when hovered!
        #The game looks for the button in "game/images" if you remove the "gui/"
        #Make the actual file of the button image larger if you'd like a bigger button!!!
            idle "gui/button.png"
            hover "gui/hoverbutton.png"
            action ui.callsinnewcontext("relationshipmenu")

#This chunk of code defines the range the variable needs to be within to show an emotion!
#You can add more or take some away. Please keep the numbers in descending order, like 80, 50, 20, 10.

init python:
    def emotions(points):
        if points >= 80:
            return "Really Likes"
        elif points >= 60:
            return "Friends"
        elif points >= 40:
            return "Neutral"
        #elif points >= 30:
            #return "Different Emotion"   -Example of a new one!
        else:
            return "Doesn't care for"
init python:

    def notes(points):

        if points >= 80:

            return "note 1This character is babababababababa and abababifeifuneifune and boom!!!"

        elif points >= 40:

            return "note 2 GAAAAAH NOOOO THE ALIENS INVADED!!!! RUNNNNNNN!!!!"

        #elif points >= 30:

            #return "note 2.5 man this is just a sample of whats to come!"   -Example of a new one!

        else:

            return "note 3 Well that's just no fun!"

#If you want different characters to have different sets of emotions, you can copy the above code starting at "init python:"
#then paste it below. Then, change the emotion ranges and names! Lastly, on the line "def emotions(points)" you need to change "emotions" to a new word,
#I suggest the character's name followed by emotions so you remember it better!

#This code defines the shape of the menu!
style relationmenustyles:
    padding (60, 60)
    background Frame("gui/affs.png") #If you rename the background picture, change this code too.
    #These following two lines center the menu! If you want it to stick to the side, you can change xalign to 0.0, or 1.0. Do whatever really.
    xalign 0.5
    yalign 0.5

#This is the data that shows inside the menu.
screen relationmenu:
    window:
        style "relationmenustyles"

        vbox:
            hbox:
                xalign 0.5
                label "{b}{color=#fff}{size=+5}Relationships{/b}{/color}" #Swap out #fff for any hexcode to change the color, and size adds to the base text size of your VN so it will be bigger!!!

            hbox:

                spacing 60 # this is how far apart the bars are

                xalign 0.5 # centering :3

                vbox: #each of these vboxes represents a row. copy and paste everything inside of this for more, but make sure it stays within the hbox and stays outside of the vbox of the previous column

                    xsize 0.5 #should make the row take up half of the container horizontally. Making this larger will make it wider. 

                    #this is the start of a character's bar

                    hbox:

                        xalign 0.5

                        add "gui/cody_relationship_icon.png" yalign 0.5 # Erase this line if you don't have icons

                        label " {b}{color=#ecce0a}[character1] is {/b}{/color}[emotions(character1affection)]" yalign 0.5

                    hbox:

                        xalign 0.5

                        bar range maxpoints value character1affection xmaximum 500
               
                    #this is the start of a character's bar

                    hbox:

                        xalign 0.5

                        add "gui/amia_relationship_icon.png" yalign 0.5 # Erase this line if you don't have icons

                        label " {b}{color=#FF1493}[character2] is {/b}{/color}[emotions(character2affection)]" yalign 0.5

                    hbox:

                        xalign 0.5

                        bar range maxpoints value character2affection xmaximum 500
                

                    #this is the start of a character's bar

                    hbox:

                        xalign 0.5

                        if character3 == "Xavier":
                            add "gui/xavier_relationship_icon.png" yalign 0.5

                        #add "gui/icon2.png" yalign 0.5 # Erase this line if you don't have icons

                        label " {b}{color=#950e0e}[character3] is {/b}{/color}[emotions(character3affection)]" yalign 0.5

                    hbox:

                        xalign 0.5

                        bar range maxpoints value character3affection xmaximum 500

            vbox:
                #This button closes the menu
                xalign 0.5
                textbutton "Return" action Return() xalign 0.5 #You can uncenter the return button by removing "xalign 0.5"

#Simplifying the process of showing the menu, so you can just say "show screen relationmenu"
label relationshipmenu:
    call screen relationmenu
    return