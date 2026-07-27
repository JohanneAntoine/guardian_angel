# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


init python:
    wickedPoints = 0


transform middling:
    xalign 0.5
    yalign 0.0
    zoom 0.5

transform leftish:
    xalign 0.0
    yalign 0.0
    zoom 0.5

transform rightish:
    xalign 1.0
    yalign 0.0
    zoom 0.5

transform cat_middling:
    xalign 0.5
    yalign 0.5
    zoom 0.3

transform jumper:
    ease .06 yoffset 24
    ease .06 yoffset -24
    ease .05 yoffset 20
    ease .05 yoffset -20
    ease .04 yoffset 16
    ease .04 yoffset -16
    ease .03 yoffset 12
    ease .03 yoffset -12
    ease .02 yoffset 8
    ease .02 yoffset -8
    ease .01 yoffset 4
    ease .01 yoffset -4
    ease .01 yoffset 0

transform farleftish:
    xalign -0.5
    yalign 0.0
    zoom 0.5

transform farrightish:
    xalign 1.5
    yalign 0.0
    zoom 0.5
transform slide_left:
    ease 0.2 xoffset 20

#colors
define amia_color = "#FF1493"

#characters
define n = Character("Nadine", color="#c7a8fc", image="nadine")
define shadow = Character("Nadine", color="#c7a8fc", image="shadowangel")
define c = Character("Cody", color="#ecce0a", callback = name_callback, cb_name = "cody")
define mocha = Character("Mocha", color="#A0522D", callback = name_callback, cb_name = "mocha")
define ami = Character("Amia", color=amia_color, callback = name_callback, cb_name = "amia")
define familiar = Character("???", color="#FFFFFF")
define cordis = Character("Cordis", color="#f677b2", callback = name_callback, cb_name = "cordis")
define angel = Character("Angel", color=amia_color, callback = name_callback, cb_name = "angel")
define xavier = Character("Xavier", color="#950e0e", callback = name_callback, cb_name = "xavier")
define yvette = Character("Yvette", color="#ffaa00", callback = name_callback, cb_name = "yvette")
define zuri = Character("Zuri", color="#3e3ef3", callback = name_callback, cb_name = "zuri")
define liv = Character("Livia", color="#079007", callback = name_callback, cb_name = "livia")


#Images
image transformed = "images/backgrounds/cgs/bg transformed.png"
image newlook = "images/backgrounds/cgs/bg new_look.png"
image thumb_locked = "images/locked-safe.png"
image detectives = "images/backgrounds/cgs/bg xyz.png"
image pink = "#f677b2"


image shadow:
    "side shadowangel.png"



image investigators = ParameterizedText(xalign=0.5, yalign=0.0)

image smokebomb = SnowBlossom("images/smokebomb.png",
    count=30, border=1000,
    xspeed=(-20,20), yspeed=(-300, 400),
    start=0.2, horizontal=False)

define flash = Fade(.25, 0.0, .75, color="#fff")

init:
    call define_sprites from _call_define_sprites


default persistent.unlock_1 = False
default persistent.unlock_2 = False
default persistent.unlock_3 = False


default character1affection = 60 #These are where the bar starts. If you make more bars, you need more of these too!
default character2affection = 50
default character3affection = 40

default maxpoints = 100 #This is the highest points a character can have. Think of the bars like ratios, if you start at 50 then your bar is 50/100 (or 50%) full! This line here changes the 100.

default character1 = "Cody" #Replace the part in quotes with your character's name. If you don't see it update live, restart the game!
default character2= "Amia"
default character3 = "???"
default notevariable= "Note 1"
# The game starts here.


label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg newsroom with fade

    show livia happy uniform at middling with dissolve
    
    liv "Welcome to Daybreaker News! I'm your host, Livia Porter! A near-disaster has thankfully been averted thanks to our very own Guardian Angel of Love!"
    
    liv "For nearly 10 years, our town's shining angel has been saving this town from constant..."

    scene bg cafe

    play music "music/CoffeeShopThemeMagicalGirl.wav" fadein 1.0


    "Random Person" "Did you see the Guardian Angel of Love's interview today?"

    "Random Person 2" "She's so cool!"

    "Whoever this Guardian Angel is, she sure is lucky. Bet she never has to deal with job applications."

    "Suddenly, I feel a tap on my shoulder."

    show cody casual at middling with dissolve

    show screen button

    c "Hey, you."

    n happy uniform "Hey yourself."

    c "How's the job search going?"

    "I groan."

    show cody sympathetic with dissolve

    # c "Well at least you have that busing job to pay off those student bills for now." 
    
    # "I groan more loudly."  

    # "Cody ignores that and continues."

    c "Okay then. How's your current job?"

    "I groan again."

    n tired "My boss has been crazy all month about it."

    c "Hey, look at the bright side, you might get free food out of it."

    n uncertain "I doubt it. I'll let you know how it went afterwards."

    show cody happy with dissolve

    c "That's my girl. See you around."

    "Alright then, back to work."

    stop music fadeout 1.0
    
    scene bg hotel with fade

    "Right on time."

    show boss angry at middling with dissolve

    "Mr. Deerg is on his phone, so maybe I can sneak by-"

    "Boss" "I don't give a d*mn if your dad's sick! Get back to work!"
    
    "Boss" "Bunker! You're late!"

    n uniform  "I was here the whole tim-"

    "Boss" "Don't talk back to me!"

    show boss neutral

    "Boss" "I hope this won't be a repeat offense. We have important clientele tomorrow. Do not ruin this for me."

    n uniform "Yes, sir."

    hide boss with dissolve

    "Miserable sack of greed."

    "Well, might as well get started. The faster I do it, the less angry he'll get."

    scene black with fade

    centered "3 hours later..."

    scene bg hotel_sunset with fade

    "Thank goodness the day's over. I can't wait to go home and watch some-"

    show boss angry at middling
    
    "Boss" "BUNKER!"

    n uniform "Yes, sir?"

    "Of-freaking course."

    "Boss" "Some idiot threw up in the bathroom. Here's a mop! I'd clean it myself, but I'm too busy and have better things to do than cleaning up other people's mess."

    n "...Yes, sir."

    hide boss with dissolve

    "Self-absorbed tool. Hopefully the mess won't be too ba-"

    n shocked "MOTHER OF-{cps=4.5} {/cps}{nw}"

    scene black

    centered "1 hour later..."

    scene bg city with fade

    play sound "audio/sfx/16-sfx_dial.ogg"

    $ renpy.pause(6, hard=False)

    stop sound 

    c "Hello?"

    n tired uniform "Hey, Cody..."

    c "Oh, Nadine! What's up? Your voice is shaky."

    n "Vomit clean up."

    c "Oh, yikes. What are you doing now?"
    
    n "Right now, I'm going home, and I'm going to get wasted."

    c "What about the important gala tomorrow?"

    n "Cr*p. Do you think I can call in sick if I get hungover?"

    c "Would your boss let you?"

    n "Ugh, no. At least I have Mocha."

    c "Thank goodness for cats, right? Be safe on your way home."

    n -tired "Bye, Cody."

    play sound "audio/sfx/17-sfx_callend.ogg"

    "What a crummy day."

    n "Hm?"

    "There's this job listing on a telephone poll for a company called Angine Tech. Doesn't look like any experience required. It might be a scam."

    "But still…it wouldn't hurt to try, right? That's what Cody would say."

    play sound "audio/sfx/18-sfx_rip.wav"

    "Now, time to go home."

    scene bg apartment_outside_sunset with fade

    scene bg living_room with fade

    show amia casual at middling with dissolve

    n uniform "Oh, hey, Amia, and...friend."

    "I wonder how long this boytoy will last."

    show amia smile at middling with dissolve

    ami "Oh, hi, Nadine! I didn't see you there!"

    "Amia's Date" "Who's this chick?"

    show amia -smile at middling with dissolve

    ami "Oh, this is my roommate. I told you I had one, remember?"

    "Amia's Date" "You didn't tell me you had a roommate."

    show amia annoyed at middling

    ami "I'm prety sure I did!"

    "Amia's Date" "So are you into, like threeways or something?"

    show amia embarrassed at middling

    ami "..."

    n embarrassed uniform "...I'm going to my room."

    "This is the last thing I need today."

    play sound "audio/sfx/19-sfx_doorclose.ogg"

    hide all


    scene bg bedroom_night with fade

    play music "audio/music/NadineTheme.wav" fadein 1.0

    n happy uniform "Hi, Mocha. You don't know how happy I am to see your friendly, furry face."

    show mocha at cat_middling with dissolve

    play sound "audio/sfx/20-sfx_meow.ogg"

    mocha "Meow."

    n "I had a rough day today, so we're just going to watch some comedy shows and-{nw}hm?"

    n neutral uniform "I had a rough day today, so we're just going to watch some comedy shows and-{fast}hm?"

    "The job listing I took falls out of my pocket."

    "...fine. I'll just get my laptop, and then TV time."

    #draw laptop

    "Same old questions…resume…demographics…and send. Okay, that settles that, now it's relaxation time!"

    stop music fadeout 1.0

    scene black with fade

    centered "The next day..."

    scene bg hotel with fade

    "Haven't gotten any answer from Angine Tech yet. I hope they answer soon. I reall need this-"

    show boss neutral at middling with dissolve

    "Boss" "Bunker?"

    n uniform "Yes, sir?"

    "Boss" "Thank you for being on time today."

    "Do the other hundreds of days I've been on time not count?"

    "Boss" "After all, you don't want to make me-I mean Mellow Journeys-look bad in front of {i}very important clients{/i}, do you?"

    n uniform "No, sir."

    "Boss" "Good, now back to work. And don't forget to smile!"

    "Okay. It's just one dinner. How bad can it be?"

    scene black with fade
    
    centered "Later that evening..."

    scene bg hotel_sunset with fade

    n customerservice uniform "Welcome! We're so glad to have you here at our gala!"

    "Rich Man" "Yes, yes, where's my table, miss?"

    n "Right this way, sir."

    "This is the first one who actually called me by a title. Maybe he'll remember to say thank you."

    "Boss" "BUNKER! MORE GUESTS ARE WAITING!"

    n "Coming!"

    "Oh, I better ace that job interview."

    n "Good evening, gentlemen, we're so glad to have you here at our gala!"

    show thomas smug at leftish
    show ricky smug at rightish
    with dissolve

    "Rich Dude" "Good evening to you, toots!"

    "Oh, no."

    n "...Let me guide you to your seats."

    "Second Rich Dude" "Sure thing, as long as you're leading the way, babe!"

    "Remember your calming strategies, Nadine. You don't have a backup job yet."

    n  "If there's anything else you need-"

    "Perish the thought."

    n "Please let me know!"

    "Rich Dude" "Hey waitress!"

    "D*mmit."

    $ _preferences.text_cps = 10

    n tired uniform "...{nw}"

    $ _preferences.text_cps = 80

    n customerservice uniform "...{fast}Yes?"

    show thomas annoyed with dissolve

    "Rich Dude" "Haven't I seen you somewhere before?"

    n customerservice "I don't think so!"

    "I would definitely remember someone like {i}him{/i}."

    "Rich Dude" "No, no, I recognize your face. You remind me of someone. Doesn't she look familiar, Ricky?"

    show ricky annoyed with dissolve

    "Great. Now the two stooges are staring at me. The {i}one time{/i} my boss isn't on my case to do something else…"

    show ricky laughing with dissolve

    "Ricky" "Oh yeah, I see it! She looks like that exotic dancer you used to date!"

    show thomas smug with dissolve

    "Rich Dude" "Yeah, yeah! Man she had such a big-"

    hide thomas with dissolve

    "That's it. That's it. I can't listen to this anymore. I turn to get the heck away from the table, only to bump into someone and hit the ground."

    show karen angry at middling  with moveinleft

    "Karen" "WATCH IT!" with hpunch

    "Oh, gosh, is this wine?!"

    "Karen" "You ruined my dress! HOW DARE YOU!"

    n sad stained "I'm sorry ma'am, it was an-"

    "Karen" "Do you know much this dress costs?! More than your entire salary!"

    show boss angry at leftish with moveinleft

    "Boss" "What is going on here?!"

    "Oh no."

    n "I-"

    "Karen" "This {i}stupid girl{/i} ruined my dress!"

    "Why is {i}she{/i} crying? Her stain isn't that big!"

    show boss customerservice

    "Boss" "My apologies, madam. I'm sure that we can cover for-"

    "Karen" "This dress cost me a {i}fortune{/i}! All because of her! Don't think I'll ever come to this dump again!"

    show boss angry

    "Boss" "Look at what you've done, Bunker!"

    n "Sir, I-"

    "Boss" "We could have lost a valuable client because of your carelessness!"

    n "I didn't-"

    "Boss" "No excuses! Pack whatever stuff you have, because you are FIRED!"

    "Rich Dudes" "Oooooh."

    show karen humph

    "Karen" "Hmph!"

    "No, no, no. This can't be happening."

    "I need to get out of here before I completely break down."

    scene bg city with fade

    "Should I call Cody? No, it's too late in the evening for that. I guess I'll just call a taxi."

    play sound "<from 1.0 to 2.0>audio/sfx/21-sfx_ringtone.ogg"

    "What now?!"

    "Angine Tech? What the h*ll, I have nothing else to lose."

    n tired stained "Hello?"

    familiar "Good evening, Nadine. Did I get your name right?"

    n "Yes."

    "First one to call me by my first name in the last 3 hours."

    familiar "Excellent. I will be the one conducting the interview with you. Are you in a good place to talk?"

    n "I'm on the street. I…just got out of work."

    "Outside my {i}former{/i} place of work."

    familiar "Yes, yes, I remember on your application that you currently work at Mellow Journey Hotel. Were they not having a gala this evening?"

    n "Yes."

    familiar "I suppose you just had to be a glorified cheerleader for all those rich people."

    "Is this a trick to get me to complain about my job?"

    n sad stained "No, I…just help clients to their tables and offer them food and drinks. I also do janitorial services sometimes."
 
    familiar "That's all? Doing things that they could easily do themselves? Do they appreciate you? Thank you?"

    "My boss thanked me for 'being on time today.'"

    n tired stained "...No."

    familiar "It sounds like they're using you to fill their own pockets, Ms. Bunker. Swimming in their wealth, with no concern for the hard-workers who helped get them where they are today. "
    
    familiar "Doesn't it infuriate you? Don't you want to get back at all of them? Take back what is rightfully yours?"

    n uncertain stained "Well..."

    familiar "Don't you want to start anew?"

    "This interviewer's reading my mind, but I don't even know what their name is. What should I say?"

    menu:
        "'I guess...'":
            "I don't know. Maybe I was just too tired. Maybe it was the stress of losing my job, but I find myself saying-"

            n uncertain stained "I guess so..."

            familiar "Don't worry. You're doing the right thing."
        "'Yeah, I do!'":
            $ wickedPoints += 1
            "I think about everything that happened tonight. The backhanded compliment from my boss. Those overgrown frat boys. That horrid woman. It's all too much."

            n angry stained "Yeah... yeah, I do!"

            familiar "I knew you would see it our way."
    
    familiar "Now, focus and say: 'Shadow Form, Activate!'"

    "'Shadow Form'?"

    "I don't know exactly what I've gotten myself into, but I'm ready to take a new chance."

    n transformation -stained "Sh-shadow form, activate!"

    scene bg transformed with flash

    if persistent.unlock_1 == False:
        $ persistent.unlock_1 = True

    "What is this? Where did this costume come from?! Where's my phone?!"

    shadow shocked "What did you do to me?!"

    "Suddenly, I hear the 'interviewer's' voice in my ear again."

    familiar "Consider this…your work uniform."

    scene bg city
    
    "Work uniform? I look like I'm going to a costume party!"

    "Speaking of party, a younger woman rushes past me to enter the restaurant."

    show becky wah at middling with moveinleft

    "Rich Woman" "Oh, I hate being late!"

    "Something tells me to follow her. I take a step forward…"

    shadow shocked "What the-?!"

    "And find myself falling into her shadow."

    show becky confused at middling

    "Rich Woman" "Hm? I thought I heard someone."

    "She keeps walking. I find myself following her from inside her shadow."

    scene bg hotel_sunset with fade

    show becky smile at leftish with dissolve

    show boss customerservice at rightish with dissolve

    "Boss" "Welcome, Miss! Please, please! Let me lead you to your seat."

    "Rich Woman" "Why, thank you!"

    hide boss with dissolve

    show becky at leftish with move

    show thomas smug at middling with moveinright

    "Rich Dude" "Becky! So nice to see you again! This party was such a bore until you came in!"

    "Oh great. This a$$hole again."

    "Becky" "Oh, Tommy…it's good to see you too."

    "Poor Becky. The idiot decides to make himself comfortable in the chair right next to her."

    "Tommy" "It's too bad you didn't come sooner! Some waitress just got kicked out! You should've seen the stain on her shirt! It looked like-"

    "While this nincompoop is talking, I notice that he left his wallet on the table."

    familiar "That could help you out a lot in the long run, won't it?"

    shadow cautious "are you insane? I'll get caught!"

    familiar "But with your disguise…"

    shadow angry "he'll still see me!"

    familiar "Not while he's still talking about 'some waitress,'"

    menu:
        "Slowly reach for the wallet.":
            "...He won't notice a few bills. I'll just take the wallet, and go."
        "Just take the wallet.":
            "They're right. Besides, he can just buy another one."

            "I reach out of Becky's shadow, and snatch the wallet without a second thought."

    "Now I just have to sneak it in my pocket, and find a way out-"

    show becky wah
    show thomas annoyed

    "Becky" "Ack-!"

    "Tommy" "What is it?"

    "Becky" "Your wallet..."

    "Cr*p. Busted. What should I do? I dive into the girl's shadow, hoping that no one else will notice."

    "Tommy" "Hey, where's my wallet?"

    "Becky" "It-it just went into my shadow!"

    show thomas smug with dissolve

    "Tommy" "Is that right? What are you going to tell me next, unicorns are real?"

    show becky angry

    "Becky" "I'm serious!"

    "Tommy"  "Yeah, yeah. I'm sure it just fell on the floor or something."

    "Tommy crouches down to look for his wallet. I'm never going to escape at this rate."

    show thomas annoyed with dissolve

    "Tommy" "Where is it? You didn't take it, did you, Becky?"

    "Becky" "No! I swear!"

    "Maybe I could sneak away while these two are arguing. I sneak out of Becky's shadow and…"

    show becky wah
    show thomas angry

    "Becky" "THERE IT IS!" with vpunch

    "Tommy" "{i}What the h*ll?{/i}"

    "Oh no. Now all eyes are on me."

    "Boss" "STOP HER!"

    "Everyone's coming towards me, what do I do?!"

    familiar "Smoke Bomb."

    shadow uhoh "what?"

    familiar "You have a smoke bomb on your belt. Use it!"

    menu:
        "No time to second guess myself. I locate the smoke bomb, a small, white ball, and throw it..."
        "On the ground":
            $ wickedPoints -= 1
            show screen smoke_bomb
            "Becky" "I can't see!"

            shadow cautious "Sorry!"
        "At the closest person":
            $ wickedPoints += 1

            show thomas pain

            "Tommy" "AGH!" with hpunch

            shadow confident "Oops. Sorry."

            "Not really."
        

    "While the room's covered in smoke, I jump out a window into the night."

    hide screen smoke_bomb

    scene black with fade

    centered "One Hour Later..."

    scene bg living_room with fade

    show amia worried casual at middling with dissolve

    ami "Oh my gosh, Nadine! What happened to your-"

    "I rush to my room without a word to her."

    scene bg bedroom_night with fade

    show mocha at cat_middling with dissolve

    play sound "audio/sfx/20-sfx_meow.ogg"

    mocha "Meow?"

    n tired stained "You don't want to know the day that I had."

    "I dig into my pocket to see if the wallet is still there. It is. I flop on my bed."

    play audio "<from 1.0 to 2.0>audio/sfx/21-sfx_ringtone.ogg"

    n "Hello?"

    familiar "You've done well for your first heist. We're pleased to offer you a position at our company."

    "Heist?!"

    n angry "That was the scariest thing I've ever done!"

    "And yet...the most exhilarating."

    familiar "Consider what you took as your first payment."

    "I look at the contents of the wallet. At least five hundred dollars in twenties."

    "What have I gotten myself into?"

    hide all

    scene black with fade

    centered "The next day..."

    scene bg city with fade

    play music "music/CoffeeShopThemeMagicalGirl.wav" fadein 1.0

    "Clerk" "Alright, thank you for your purchase. Have a nice day."

    show cody casual at middling with dissolve

    c  "Ooo, are we splurging today? What's the occasion?"

    n -uniform -stain "Well, I got fired last night."

    show cody sympathetic at middling

    c  "Aw, sorry, 'dine. Did you hear back from other companies?"

    if wickedPoints > 0:
        n smile  "Something like that."

    else:
        n "...Something like that."

    "Cody grins ear to ear and gives me a one-armed hug."

    show cody happy at middling with dissolve

    c "I knew you'd find something!"

    n smile casual  "Yep. Good thing I lost that other job, given what happened last night."

    show cody at middling

    c "What happened?"

    stop music fadeout 1.0

    hide all

    scene black with fade

    centered "Meanwhile..."

    scene bg newsroom with fade

    show livia uniform at middling with dissolve

    liv "...witness claims that the suspect wore something resembling our very own Guardian Angel of Love. Could this \"Shadow Angel\" be connected to the town's heroine? Up next…"

    scene bg city with fade

    show cordis at leftish with dissolve

    cordis "Angel, what do you make of this?"

    show angel angry at rightish with dissolve

    angel "...Tch."

    hide all

    scene black with fade

    centered "Meanwhile, at Mellow Journeys..."

    jump episodeTwo

label episodeTwo:

    scene bg hotel with fade

    show becky wah at leftish
    show thomas angry at middling
    show boss angry at rightish
    with dissolve

    "Boss" "This is an absolute disaster! How will this reflect on me-I mean, the hotel?!"

    "Karen" "I demand to know what gives people the right to barge in here and ruin the nights of decent people!"

    "Becky" "I don't know how it happened or why, but Tommy's shadow just came to life!"

    "Tommy" "Why can't you do anything?! You're the owner of this dump!"

    "Boss" "I TOLD you, Mellow Journeys is not responsible for valuables not kept in safes!"

    "Ricky" "Shouldn't someone call the cops?"

    show becky smile with dissolve

    "Becky" "Actually, I already called someone…"

    "Ricky" "Really? Who?"

    show becky confused

    "???" "SOMEONE RANG?" with vpunch

    show becky at middling with move

    show xavier confident uniform at leftish with moveinleft

    "Man" "Crime afoot!"

    show boss at farrightish 

    show becky confused at rightish 
    
    show xavier at middling 

    with move

    show yvette confident uniform at leftish with moveinleft

    "Stout Woman" "Valuables stolen!"
    
    show becky confused at slide_left

    show zuri confident uniform at farleftish with moveinbottom

    "Skinny Woman" "Who will solve it?"

    "Man" "Xavier!"

    "Stout Woman" "Yvette!"

    "Skinny Woman" "Zuri!"

    xavier "We are..."

    scene bg xyz with flash

    show investigators "{color=#000000}PRIVATE INVESTIGATORS: XYZ!{/color}" 
    with dissolve

    $ renpy.pause(3, hard=False)

    if persistent.unlock_2 == False:
        $ persistent.unlock_2 = True

    scene bg hotel

    show becky confused at leftish

    show boss neutral at rightish

    "..."

    "Boss" "{i}This{/i} is whom you decided to call?"

    "Becky" "they were the first ones to pick up…"

    show becky at middling with move

    show xavier outraged uniform at leftish with moveinleft

    xavier "Justice never rests when thievery's around!"

    "Tommy" "Oh, brother…" 

    show zuri glasses uniform at farleftish with dissolve

    zuri "So tell us the details! Who, what, where, when and why?"

    "Boss" "Well, someone-{nw}"

    "Tommy" "Some ***hole stole my wallet!"
    
    show zuri outraged at farleftish with dissolve

    zuri "Scandalous! What did they look like?"

    "Boss" "That's what we're trying to figure out!"

    "Becky" "They were black all over!"

    show yvette thinking uniform at farrightish with dissolve

    yvette "They wore black?"

    "Becky" "No, they were all black! Like a shadow-"

    "Tommy" "He threw a d*mn smoke bomb at me!"

    "Ricky" "Pretty sure he was a 'she'."

    "Tommy" "No, it was certainly a man! It looked like-"

    "Becky" "I'm not sure what gender they were…"

    "Tommy" "He towered over everyone!"

    "Ricky" "I thought she was your height!"

    hide becky with dissolve

    hide boss with dissolve

    show xavier thinking at middling with move

    show zuri thinking:
        linear 0.5 xoffset 150

    show yvette thinking at rightish with move

    zuri "Seems like a bad case of the blind men describing the elephant! What do you think, X?"

    xavier "Hmm..."

    show xavier confident at middling

    xavier "Excuse me, sir!"

    "Tommy" "What?"

    show xavier thinking at middling

    xavier "Do you know anyone who would hold a grudge against you?"

    "Tommy" "Of course not!"

    yvette "Do you owe anyone money?"

    "Tommy" "No! Well, no one outside this hotel..."

    show zuri glasses with dissolve

    zuri "Do you think they might strike here again?"

    "Tommy" "They'd better not!"

    show xavier confident with dissolve

    xavier "One thing we can conclude is that they're still out there. We won't rest until we find them!"

    scene bg bedroom_day

    n shocked "GASP!" with vpunch

    show mocha at cat_middling with dissolve

    mocha "Meow?"

    play music "audio/music/NadineTheme.wav"

    n relief "Ugh, sorry, Mocha. Just had a bad dream."

    "Hard to believe what happened two nights ago wasn't."

    menu:
        "It's all just so…"
        "Terrifying":
            "...absolutely terrifying! What the h*ll am I going to do? How am I going to explain this to my family? Or Cody?"

            "Okay, calm down, Nadine. Breath in, breath out."

            "Mocha must have sense that I'm nervous, as he bounds over and rubs against my leg."

            mocha "Meow..."

            n "You don't have to worry about money, don't you? Must be easy being a cat."

            mocha "Mrr..."

            "As much as I'd love to stay with Mocha all day, I have to eat."


        "Exciting":
            "...weirdly exciting. I feel like I'm a teenager discovering she's a magical girl for the first time."

            mocha "Meow!"

            n happy "I'd guess you'd be my familiar, wouldn't you?"

            hide mocha with dissolve

            "Mocha leaves without a word."

            n deadpan "Or not."

            "I wonder who else would be on my team. Cody? Amia?"

            "Speaking of which, I hear pots and pans coming from the kitchen. I should get breakfast."

    scene bg living_room with fade

    show amia angry casual at middling with dissolve

    n -tired "Good morning Amia..."

    ami "..."

    n "Amia?"

    show amia shocked at jumper

    ami "Oh!"

    show amia smile at middling

    ami "Good morning, Nadine! I didn't see you there."

    n "Is...everything okay?"

    "She's usually so overly happy. I didn't know she could look mad."

    show amia annoyed at middling

    ami "It's nothing! Just going through a bad breakup."

    "Yep, that figures."

    n "I see{nw}"

    show amia smile at middling

    ami  "Hey, I just got an idea! Since it's Saturday, let's go shopping!" with hpunch

    n shocked "What?"

    "Where the h*ll did {i}that{/i} come from? We barely talk to each other!"

    ami "Well, I mean, shopping cheers me up, plus your shirt got ruined, so we could both use new clothes!"

    n -shocked "...right."

    ami "So what are you waiting for? Let's go!"

    n sad "Can I eat first?"

    scene black with fade

    stop music fadeout 1.0

    centered "30 minutes later..."

    scene bg city_day with fade

    show amia smile casual at middling with dissolve

    ami "Here we are! My favorite shopping place!"

    show amia worried at middling with dissolve

    ami "...Nadine? Is something wrong?"

    n shocked "What?"

    n customerservice "What?{fast} No. Of course not!"

    "Nothing to worry about except the fact that {i}this store is right across Mellow Journeys.{/i}"

    ami "If you want, we could go home…"

    "I quickly point at the first mannequin I see."

    n "No, no! In fact, that outfit's calling my name!"

    show amia smile casual at middling with dissolve

    ami "Really? You have to let me see the result!"

    "I rush inside and take the outfit before Amia can ask any more questions."

    "A white shirt with a black star on it with black jeans and a belt. Thank goodness it's a perfect fit."

    "In the dressing room, I try on the clothes, and check myself in the mirror."

    scene bg new_look with fade

    if persistent.unlock_3 == False:
        $ persistent.unlock_3 = True

    "..."

    "...not bad."

    scene bg city_day with fade

    "I pay for the outfit step out where Amia is waiting for me. Looks like she bought a new dress, too."

    show amia smile dress at middling with dissolve

    ami "Oh my gosh Nadine! You look great! Black and white is definitely your color!"

    n shocked street "What?!"

    show amia worried at middling with dissolve

    ami "I mean, it's a nice contrast."

    n relief "Right, right."

    menu:
        "Great. She looks hurt. I should say something."
        "Apologize":
            n "Sorry. Just feeling a bit jittery."
            
            ami "Oh, I'm sorry! Did I startle you?"

            n customerservice "No, no, it's fine!"

            ami "Oh{cps=10}...{/cps}{nw}"

            show amia smile at middling

            ami "Oh…{fast}okay then! Let's pay for our stuff!"

        "Compliment her back":

            n -relief "Um, thanks. You look nice too."

            $ character2affection += 5

            show amia smile at middling with dissolve

            ami "Aww, thank you!"

            "Thank goodness that cheered her up."



    "After paying for our clothes, we head out and pass by Mellow Journeys."

    "{i}Of course{/i}, one of the trust fund boys barges out right then and there."

    # show ricky annoyed at rightish with dissolve

    "Ricky" "The nerve of those detectives, asking me if I would steal. Ugh, I need a cigarette-"

    "He stops in his tracks when he sees us."

    "Oh sh*t. Oh sh*t. He recognizes me!"

    show amia worried dress at middling with dissolve

    ami "Nadine?"

    "He's coming this way! I can't move!"

    "Ricky" "Say…"

    "I shut my eyes as tight as I can. That's it. My life is over. I'm going to jail."

    # show ricky flirty at rightish with dissolve

    "Ricky" "What's a babe like you doing in a place like this?"

    "Huh?"

    "I open my eyes to see that the dude isn't even looking at me. He's staring straight at Amia."

    "Oh. {i}Oh{/i}. Okay, then."

    ami "Huh?"

    "Ricky" "How about you and me head somewhere nice? My treat."

    ami "Um..."

    "Just say no."

    ami "I dunno. I'm kind of busy today."

    "Ricky" "How about your number then?"

    "Before Amia can answer, I get pushed over."

    show karen angry at rightish with moveinright

    # show ricky annoyed at middling

    show amia shocked at leftish

    with move

    "Karen" "Out of my way!" with hpunch

    "Oh for goodness sake, again?"

    "Karen" "Had to go buy a new dress thanks to that stupid waitress-"

    "Well, at least this witch didn't see me-"

    show amia shouting

    ami "Hey!"

    "Cr*p."

    "Karen" "Excuse me?"

    ami "You just knocked over my friend!"

    n sad street "It's fine! I'm okay!"

    show karen

    "The woman's looking at me. She's going to recognize me and I'm going to go to jail and-"

    show amia angry

    ami "You should apologize."

    show karen humph

    "Karen" "I didn't see her there."

    show amia shouting

    ami "That's not an excuse to push her!"

    "Karen" "She shouldn't have been in my way!"

    n "Amia...let's just go."

    show amia angry

    ami "..."

    # show ricky flirty

    "Ricky" "Woo! I like em fiesty! You know, there's a fancy dinner next week at-"

    ami "P*ss off."

    "Amia storms off. I quickly follow before things get worse."

    scene bg apartment_outside_sunset with fade

    show amia angry dress at middling with dissolve

    ami "The nerve of that b*tch, and her stank attitude!"

    show amia worried

    ami "Are you sure you're okay?"

    menu:
        "It's fine.":

            $ amiaSweet = True

            $ character2affection += 10

            n relief street "Yeah, I'm okay. Um, thanks for sticking up for me."

            show amia smile with dissolve

            ami "Of course! You shouldn't let people like that walk all over you!"

            show amia angry 
            
            ami "Believe me, I've had my fair share of disrespect..."

            show amia smile

            ami "...but I don't want you to think you deserve that!"

            "She gave my shoulder a squeeze, and I can't help but smile. I guess her attitude is contagious."

            n happy "Thanks, Amia."

        "Not really...":

            $ amiaSweet = False

            n relief street "It's fine. I had to deal with people like her all the time."

            ami "...Wait."

            show amia shocked

            ami "Was that where you got fired?!"

            n sad "Yeah."

            show amia embarrassed

            ami "PLEASE TELL ME I DIDN'T SNAP AT YOUR FORMER BOSS."

            n relief "Oh no. She was just a customer."

            "A really b*tchy one."

            show amia smile

            ami "Oh thank goodness!"

    "This was a long day. At least we're at the apartment now."

    scene bg living_room with fade

    scene bg bedroom_day with fade

    play music "audio/music/NadineTheme.wav"

    "As soon as we enter, my phone vibrates."

    "'Florence Fowl, room 102.'"

    show mocha at cat_middling with dissolve

    mocha "Meow?"

    "I check my email. I have rent and electricity bills due in a week."

    "Do I dare?"

    "I get another text."

    "'This is the woman who got you fired. Did you receive a severance pay?'"

    "I didn't. But it might be risky. Then again, I think about the way that woman looked at me like I was a thing."

    n uncertain street "She deserves this, right, Mocha?"

    mocha "Mrr..."

    "I head downstairs."

    scene bg living_room with fade

    show amia worried dress at middling with dissolve

    ami "Oh, are you going to your new night job?"

    n -uncertain street "Yeah."

    ami "Be careful!"

    menu:
        "Thank you.":

            "She has no idea right she is."

            n "I will."

        "Are you worried about me?":

            n "You don't have to be worried."

            ami "Of course I do! I don't want you to get hurt..."

            "She looks so concerned, it's...cute?"

            n embarrassed "Uh, thank you."

    "I head out the door."

    stop music fadeout 0.5

    scene black with fade

    centered "1 hour later..."

    scene bg city with fade

    "Okay, no one's watching. Let's go."

    n transformation "Shadow form, activate!"

    scene bg city with flash

    shadow cautious "Now, I wait." 

    show zuri thinking uniform at middling with moveinleft

    "As luck would have it, a tall lanky woman struts inside. She seems more preocupied with her drink than seeing me."

    "Might as well jump in. Who is this woman, anyway?"

    scene bg hotel_sunset with fade

    show yvette neutral uniform at rightish with dissolve

    show xavier confident uniform at middling with dissolve

    xavier "Ah, Inspector Z!"

    "Inspector?!"

    show zuri thinking uniform at leftish with dissolve

    zuri "Did you find any more clues?"

    show yvette thinking uniform at rightish with dissolve

    yvette "Not yet."

    "Great. There's three of them! How could this get any worse?"

    "Karen" "Have you done anything useful yet?"

    "Spoke too soon."

    xavier "Not to worry, madam! We're on the case. Now there's a possibility the thief might return…"

    "Good things shadows can't sweat."

    show zuri glasses

    zuri "Do you have anything the thief may be interested in stealing…?"

    "Karen" "You better stay out of my suite!"

    "Jeez. While this witch is talking, I take the chance to slip into her shadow. She storms off in a huff."

    scene bg room_102 with fade

    "Karen" "Useless detectives. They probably don't even have a license…"

    "The lady pulls out her key and unlocks the door."

    menu :
        "Set off the alarm.":
            $ fire = True

            play sound "audio/sfx/22-sfx_firealarm.ogg"

            "I pull the nearest fire alarm, and all h*ll breaks loose."

            "Karen" "WHAT IS THIS?!"

            "Becky" "FIRE!"

            xavier "Everyone evacuate!"

            "The Karen runs off in a panic, not noticing me slipping out of her shadow."

            "I sneak into her suite and take all the jewelry I can find."

        "Wait.":

            $ fire = False
            "She enters the room and examines her reflection to reapply her makeup. While she's distracted. I hide behind a lamp."

            "Karen" "Ugh, I need a drink."

            "Good, she's leaving. Now to look for the jewels."

            "I check some of her drawers, and find some necklaces and ruby earrings. Bingo."

    scene bg hotel_sunset with fade

    "Good thing I worked here. I know exactly where the emergency exit is-"

    xavier "STOP RIGHT THERE!" with hpunch

    "Uh oh."

    show xavier outraged uniform at middling with dissolve

    xavier "So you're the thief behind all this!"

    show yvette outraged uniform at leftish  with dissolve

    yvette "You might as well surrender, because you're going down!"

    show zuri outraged uniform at rightish with dissolve

    zuri "In the name of…"

    show xavier confident

    show yvette confident

    show zuri confident

    "Private Investigators: XYZ!"

    "..."

    "Oh, they're {i}that{/i} kind of group. What's with the outfits?"

    show xavier outraged

    xavier "No words, criminal? You have the right to remain silent!"

    menu :
        "What do I do now?"
        "Sweet talk my way out of this.":

            $ xaviersweet = True
            
            "Maybe I can sweet talk my way out of this. Plus, the guy in red is kind of cute..."
            
            shadow confident "Sorry, I guess I was distracted by the…{i}fine man{/i} in front of me."

            $ character3affection += 10

            $ character3 = "Xavier"

            show zuri outraged

            show yvette outraged

            show xavier flustered with dissolve

            $ renpy.pause(0.5, hard=False)

            xavier "{cps=40}I…uh…er…what?{/cps}"

            zuri "Flirting with a man of the law?! Outrageous!"

            yvette "{cps=10}Oh. My. Gosh.{/cps}{nw}"

            show yvette lovesick 

            yvette "Oh. My. Gosh.{fast} It's forbidden love!"

            zuri "Y! Get a hold of yourself!"

            "While they're distracted, I throw another smoke bomb."

            jump escape

        "Use a smoke bomb.":
            $ xaviersweet = False
            jump escape

label escape:
    show screen smoke_bomb

    show yvette outraged uniform

    show zuri outraged

    show xavier outraged

    zuri "ACK-!"

    yvette "Can't see!"

    xavier "Where is she?!"

    familiar "You seem to be getting the hang of this, Ms. Bunker."

    "Oh, it's them again."

    familiar "Shall I teach you a new trick? Go inside one of the detective's shadows."

    "In the middle of the chaos. I leap into the shortest one's (Y…?)"

    familiar "Now focus, and say, 'Shadow Shapeshift!'"

    shadow cautious "'Shadow shapeshift?'"

    "Suddenly, I feel myself lifting out of the darkness."

    scene bg nadineyvette with fade

    "I look down and see that I look just like the detective!"

    xavier "Let's split up! She could be anywhere!"

    hide screen smoke_bomb

    if fire:

        scene bg city with dissolve

        "I dash out of the hotel, and bump into my former boss."

        show boss angry at middling with dissolve

        "Boss" "You! Have you seen the good-for-nothing who set the alarm?"

        "Too nervous to speak, I shake my head."

        show boss neutral with dissolve

        "Boss" "I don't why I kept you three around…"

        "I shrug and quickly leave before he asks any more questions."

    else:

        scene bg hotel_hallway with fade

        "I dash past the hotel guests and bump into the witch again."

        "Karen" "You! Someone stole my jewels! I demand to know who did it!"

        "I point behind myself. Thankfully she falls for it."

        "Karen" "THIEF!!"

        "With no other distractions, I slip away into the night."

    scene bg apartment_outside_sunset with fade

    scene bg living_room with fade

    scene bg bedroom_night with fade

    show mocha at cat_middling with dissolve

    play music "audio/music/NadineTheme.wav"

    play sound "audio/sfx/20-sfx_meow.ogg" 

    mocha "Meow!"

    n relief street "Well, that was a trip."

    play sound "<from 1.0 to 2.0>audio/sfx/21-sfx_ringtone.ogg"

    "Before I can lie down, my phone rings."

    n "Yes, I did what you asked, and-"

    c "Nadine?"

    n shocked "G-gk."

    c "What's going on? You sound out of breath."

    n customerservice "Uh…just finished my shift, and I, uh, missed the bus."

    c "Aw, sorry to hear that, 'dine."

    n customerservice "Anyways, I gotta go to sleep now. Good night!"

    c "Okay...night, Nadine."

    "I look at the jewels I've stolen and sigh."

    mocha "Mrow?"

    n tired "At least I have you to talk to about this."

    mocha "Mrr…"

    "It's fine. It's better that Cody doesn't know. He might get roped into all this. Even best friends keep secrets from each other..."

    "{cps=40}...Right?{/cps}"

    scene black with fade

    stop music fadeout 0.5

    centered "To be continued..."

    # centered "The next day..."


label episodeThree:

    scene bg cafe with fade

    play music "audio/music/CoffeeShopThemeMagicalGirl.wav" fadein 0.5

    show cody casual at middling with dissolve

    c "Hey, you. How's the new job treating you?"

    n uncertain street "It's alright."

    "Can't tell him. Can't let him be roped in."

    show cody sympathetic with dissolve

    c "What is it that you do, again?"

    n shocked "It's...I...{cps=10}...{/cps}{nw}"

    n sad "It's...I...{fast}{size=*0.5}dress up and...{size=*0.75}do stuff..."

    c "Wait. Don't tell me. You're got a modeling job?"

    n "...Yeeeeees?"

    show cody with dissolve

    c "Wow. Never struck you as the model type."

    menu:
        "What does that mean?":

            $ character1affection += 10

            $ codySweet = True
            n deadpan "Are you saying I'm not model material?"

            "This boy better choose his words wisely-"

            c "Well...in terms of how reserved you can be, sure, but then again..."

            show cody flirty with dissolve

            c "...looking how you do, I'm not surprised an agent noticed you."

            n shocked "..."

            n embarrassed "Oh. Okay. Uh, thanks."


        "There's a first for everything.":

            $ codySweet = False
            
            n uncertain "Well, there's a first for everything, y'know?"

            show cody happy with dissolve

            c "Well, I'm happy for you."

            n "Yeah, uh, thanks."
        
    
    n customerservice "Anyways! What's been going on in your life?"

    show cody with dissolve

    c "Same as usual. Just making deliveries. Kind of dull, though."

    show cody sympathetic

    c "Maybe I should try modeling. Do they have any openings?"

    n shocked "Uh-"

    "Before I could answer that, my phone starts to ding loudly."

    c "Do you need a moment?"

    n customerservice "Yep! It might me my parents."

    "Thankful for the distraction, I open my phone and-"

    "E Celeb" "WHAT IS UP, MOTHERF*CKERS?!" with hpunch

    play sound "audio/sfx/23-sfx_airhorn.ogg"

    "Peace O Cake" "IT'S YA FAVORITE PRANKSTER, PEACE-O-CAKE WITH A BRAND NEW VIDEO!!"

    "Peace O Cake" "TODAY I'M THROWING A CUH-RAAAAZY COSTUME PARTY!"

    c "Everything good?"

    n shocked "Oh, gosh, I'm sorry, I don't know why someone sent me this-"

    "Peace O Cake" "For the ladies, there'll be a cash prize for whoever wears the hottest-"

    "I turn my phone off."

    n sad "Sorry about that!"

    c "It's cool. Was someone pranking you?"

    n relief "...yeah."

    "Thank goodness Cody doesn't press for questions. The rest of the lunch goes well."

    stop music fadeout 1.0

    scene black with fade

    centered "Later that day..."

    scene bg living_room with fade

    n -relief street "I'm heading out."

    show amia dress at middling with dissolve

    ami "Oh, are you going to work?"

    n "Yeah."

    if amiaSweet == True:

        show amia smile 
        
        ami "Oh, I got something for you!"

        "She hands me a fluffy white jacket."

        n sad "What's this for?"

        ami "To keep you warm, silly! It gets chilly at night..."

        show amia winking

        ami "...plus, I think you'd look cute in it!"

        menu :
            "\"It is kinda chilly...\"":

                "It {i}does{/i} get kind of cold, but I'm pretty sure I won't need it after I transform."

                "Even so, I hear my mom's voice reminding me of my manners."

                n happy "Thanks, Amia."

                show amia smile

                ami "You're welcome!"

            "\"Cute?\"":

                $ character2affection += 5

                n embarrassed "You really think so?" 

                if codySweet == True:

                    "That's the second time today someone said I was cute."

                "No one's ever given me something like this before."

                n happy "Thanks, Amia. This is really sweet."

                show amia aww with dissolve

                ami "Aww...you're welcome!"

    else:
        ami "Okay, be careful!"

    scene black with fade

    centered "50 minutes later..."

    scene bg street_sunset with fade

    "Gosh, why are there no buses to this place? But at least the coast is clear."

    "While I stop to catch my breath, my phone starts buzzing."

    jump phone_discussion_test

label hangup:

    "Right, now to transform."

    n transformation "Shadow... *pant* *pant* form...*huff* activate!"

    scene bg street_sunset with flash

    shadow cautious "Alright, where's the dang house?"

    "I strain to hear some music down the street. Bingo."

    "As I walk down the street. I see some bright lights three doors down. When, I get there, I hide behind some bushes."

    shadow "Now how do I get inside...?"

    "When a drunk girl dressed as a honeybee opens the door."

    show bumblebee confused bee at middling with dissolve

    "Tipsy Girl" "Hey-hey you! Are you here for the costume party?"

    shadow uhoh "What? I mean yes!"

    show bumblebee happy bee at middling with dissolve

    "Tipsy Girl" "Oh, come on inside, the party's just gettin' stahted!"

    "The girl then yells to the house."

    "Tipsy Girl" "Hey, Peace-O-Cake! Another guest arrived!"

    "Peace O Cake" "Let her in! Let her in!"

    "Well, {i}that{/i} was easy."

    scene bg fancy_living_room with fade

    "Wow, swanky place he's got here."

    "Peace O Cake" "Welcome to my humble abode! Make yourself reeeeaaal comfortable, babe!"

    "Peace O Cake" "So, you going for the cat burgular type? That's kinda hot."

    "Ew."

    shadow cautious "It's not supposed to be hot-"

    "Peace O Cake" "Yeah, I can sort of see that."

    "For a split second, this guy glances at my chest. Oh h*ll no."

    "When I hear the doorbell ring, I'm quick to move."

    shadow "Hello-?"

    show cody uniform at middling with dissolve

    shadow shocked "URK-!"

    c "Hey, I got 20 pizzas for-"
    
    c "{cps=20}...{/cps}Hey. Nice costume."

    "Why is he here? {i}Why here, tonight, of all nights?!{/i}"

    "Peace O Cake" "Ugh, {i}finally{/i}."

    menu:
        "What do I do? What do I do?!"
        "Make small talk":
            "I try to change the topic, while trying not to look my best friend in the eye."

            shadow uhoh "So, uh, what kind of pizza did you order?"

            "Peace O Cake" "One of everything! Pepperoni on one, mushrooms on another, pineapple on-"

            "Tipsy Girl" "Ewwww, pineapple?!"

            "Peace O Cake" "What's wrong with pineapple?"

            "Tipsy Girl" "It belongs in a fruit bowl, not on pizza."

            shadow angry "{size=*0.5}Exactly.{/size}"

            "Cody glances in my direction."

            c "Hm?"

            shadow uhoh "Mmph!"



        "Keep quiet":
            "I keep my mouth shut. Don't want Cody to hear my voice."

    "Peace O Cake" "So you got everything?"

    c "Got it, that'll be $361.00."

    "Peace O Cake" "$361?! Don't I get a discount, like, buy one, get one free?"

    c "You ordered 20 pizzas."

    "Peace O Cake" "Listen, buddy, I'm a really big deal around here. So if you gave me a discount, I'd really appreciate it."

    "Cody's got a better poker face than I do. Only the left corner of his mouth twitches."

    show cody annoyed with dissolve

    c "$361.00 or you don't get the pizzas."

    "Peace O Cake" "Ugh, {i}fine.{/i} Lemme get my credit card."

    show cody happy with dissolve

    c "Thank you very-"

    play sound "audio/sfx/19-sfx_doorclose.ogg"

    hide cody

    "Peace O Cake takes the pizzas and slams the door without another word."

    "Peace O Cake" "Now this party can get started for real! What's your problem?"

    shadow angry "{i}Nothing...{/i}"

    "Piece of sh*t."

    "Peace O Cake" "Whatever, it's time for the hottest costume contest! All the ladies line up!"

    "A bunch of women huddle in the center of the room. I follow them, then I notice a light switch nearby."

    shadow confident "Hmm..."

    "Peace O Cake" "Alright, alright, looking good, but if I had to pick one..."

    scene black

    "Suddenly the lights go out."

    "Tipsy Girl" "What the h*ll?!"

    "Peace O Cake" "Who turned off the lights?!"

    "Other Girl" "Hold on a moment! I think the light switch is this way-"

    "Tipsy Girl" "OW!"

    "Other Girl" "Sorry! Wait! Here it is!"

    scene bg fancy_living_room

    "Peace O Cake" "Thank goodness! Now I can-"

    "Peace O Cake" "..."

    "Peace O Cake" "WHERE'S MY WALLET?!"

    scene bg street_sunset with fade

    "That was too stressful. Does Cody have to deal with people like {i}that{/i} every day?"

    "...he didn't even get a tip."


    menu:
        "I think about what happened, and..."
        "Give him the loot":
            $ cody_rich = True
            "Cody deserves this more than I do. I hope that wasn't his delivery."

            scene black with fade

            centered "Later that night..."

            show cody neutral at middling with dissolve

            c "Phew. What a long night-"

            "Colleague" "Yo, Cody! Someone left you a big tip!"

            c "Hm?"

            "Colleague" "She must really like pizza to come all the way here!"

            c "...Well, well."

            jump homeAgain

        "Best to keep it":
            $ cody_rich = False
            "I can't give him this money. It's dirty. I'll just walk home."

            jump homeAgain



label homeAgain:
    scene bg bedroom_night with fade

    "Finally. Now to turn in-"

    "What now?"

    jump cody_text


label cody_confrontation:

    "I have a bad feeling about this."

    scene black with fade

    centered "The next day..."

    scene bg cafe with fade

    play music "audio/music/CoffeeShopThemeMagicalGirl.wav"

    show cody casual at middling with dissolve

    "Play it cool, Nadine."

    n street "Hi."

    c "Hey. How was work last night?
    "

    n uncertain "Oh, it was fine...lots of posing. How was yours?"

    if cody_rich:
        show cody smile

        c "It was pretty good! I got a pretty big tip!"

        n happy "Oh, congrats!"

    else:
        c "It was alright, had some rude customers, though."

        n "Oh, sorry about that."

    show cody 

    c "This one guy thought he deserved free pizzas because he's some big shot online."

    n sad "Um, yikes."

    show cody sympathetic with dissolve

    c "But you already knew that, didn't you, {b}Shadow Angel?{/b}"

    stop music

    n shocked "{cps=2}...{/cps}"

    n sad "W-w-what are you talking about?"

    c "You were at that guy's party, weren't you? He posted a video about it."

    n sad "The {i}Shadow Angel{/i} might have been there, but {i}I{/i} wasn't!"

    c "I saw her, too. And she's exactly your height, and has the exact skin color."

    n sad "Lots of people are my height!"

    c "...Yeah, I guess you're right. I don't think you could steal his gold necklace."

    n uncertain "He didn't have a gold neckla-"

    n shocked "..."

    "I grab his arm and pull him outside the cafe."

    scene bg city_day with fade

    show cody casual at middling with dissolve

    n tired street "How long."

    c "Hm?"

    n "How long have you known?"

    show cody sympathetic

    c "Well, I had my suspicions when you-when the {i}Shadow Angel{/i} robbed the same place you got fired from, but when I saw y-{i}her{/i} at that party, that's when I knew for sure."

    n "What will it take for you to not call the police?"

    c "'Dine, do you really think so little of our friendship that I would turn you in?"

    n shocked "What?"

    c "You're my best friend, I don't want to see you rot in a cell."

    c "That being said, there is something you could do for me."

    n sad "W-what?"

    show cody flirty with dissolve

    c "I want in on the action."

    n shocked "WHAT?!"

    c "Think about it. You need a getaway driver, don't you?"

    c "Well, here I am, offering my services for free."

    n sad "Really?"

    c "Actually, I was thinking 50-50 of the loot."

    "Despite everything, I laugh."

    show cody sympathetic

    c "...60-40?"

    n sad "Wait, what about your job?"

    "It {i}is{/i} hard running from place to place."

    c "It'll be a perfect cover. I'll do my \"deliveries\" while you go do your stuff. Plus, pizza delivery doesn't pay that well."

    c "Speaking of...when's the next heist?"

    

    # c "So...what's the next plan, chief?"

    n "Well, I usually get messaged from-"

    play sound "<from 1.0 to 2.0>audio/sfx/21-sfx_ringtone.ogg"

    n shocked "!"

    "I check my phone. Sure enough, it's them. I glance around if there is anyone listening."

    c "Nadine?"

    n tired "You're about to find out."

    "I pick up the phone."

    n "Hello?"

    familiar "May I speak to the gentleman next to you?"

    "Oh no."

    n "It's for you."

    "Cody takes my cellphone and chats."

    c "Hey, the name's Cody...Cody Metullus...M-E-T-U-L-L-U-S...Before you start, I wanna know..."

    show cody annoyed

    c "Hey, the name's Cody...Cody Metullus...M-E-T-U-L-L-U-S...Before you start, I wanna know...{fast}are you blackmailing her?"

    show cody -annoyed

    c "Hey, the name's Cody...Cody Metullus...M-E-T-U-L-L-U-S...Before you start, I wanna know...are you blackmailing her?{fast} Good to know..."

    c "...Hm? I promise I won't blab..."

    show cody shocked

    c "..."

    show cody annoyed

    c "...{fast}No need to go {i}that{/i} far...Yes I can drive and pretend to do deliveries..."

    show cody happy

    c "...No need to go {i}that{/i} far...Yes I can drive and pretend to do deliveries...{fast}Glad to see we can come to an agreement!"

    "Cody hangs up."

    n sad "Well?"

    c "Well they told be that I could be your getaway driver..."

    show cody annoyed

    c "Well they told be that I could be your getaway driver...{fast}and that they'll kill me if I tell anyone else."

    n shocked "WHAT?!"

    c "Hey, I wasn't going to tell anyone else anyways."

    show cody happy

    c "But on the bright side, you now have a getaway driver!"

    n relief "You're really okay with this?"

    show cody sympathetic with dissolve

    c "Nadine, I will {i}always{/i} be by your side. One hundred percent."

    # show cody with dissolve

    # c "I gotta head out now, but I'll see you soon, alright?"

    # n happy "Sure."

    menu :
        "Thank him":

            n happy "Thanks, Cody. This means a lot to me."

            c "Hey, don't sweat it."

        "Hug him":
            scene bg nadine_cody_hug with fade 

            "I give him a big squeeze."

            $character1affection += 2

            n happy "Thanks, Cody. This means a lot to me."

            c "Aww, don't sweat it."


    scene black with fade

    centered "That evening..."

    scene bg living_room with fade

    show amia angry casual at middling with dissolve

    n street "Hi, Amia."

    "She barely registers me, her eyes glued to the TV."

    "TV" "This is Livia Porter, reporting on a theft of several priceless artifacts at the Museum of Historical Art. Already, citizens are suggesting that the Shadow Angel is behind all this."

    "Well, she wasn't, that I can tell."

    n "Amia?"

    ami "I don't know who this fake angel thinks she is..."

    n sad "..."

    "I...should probably head to my room."

    scene bg bedroom_night with fade

    show mocha at cat_middling with dissolve

    play sound "audio/sfx/20-sfx_meow.ogg"

    mocha "Meow!"

    n happy street "Hi, Mocha. Did you have a good day?"

    mocha "Mrr..."

    # play sound "<from 1.0 to 2.0>audio/sfx/21-sfx_ringtone.ogg"

    # n -happy "Huh?"

    # n "Hello?"

    # familiar "Hello Nadine. How did last night's heist go?"

    # "I look down at Mocha for strength."

    # hide mocha with dissolve

    # "Mocha prompty leaves the room."

    # "Traitor."

    # n uncertain "It went fine. I got the mark's wallet..."

    # familiar "Did you remember to cover your tracks?"

    # n sad "..."

    # familiar "Nadine?"

    # n uncertain "{i}Hypothetically{/i}, what would happen if someone were to find me out?"

    # familiar "Well, I would suggest checking if they told anyone else."

    # n uncertain "Right."

    # familiar "And then eliminate them."

    # n shocked "WHAT?!"

    # familiar "But we're speaking in {i}hypotethicals{/i}, so there's no need."

    # "Play it cool, Nadine. They don't know yet."

    # n uncertain "Uh, what if they said they're willing to keep quiet and also help out?"

    # familiar "Is this truly a hypothetical scenario, Nadine?"

    # "F*ck."

    # n tired "No."

    # familiar "{i}Nadine...{/i}"

    # n sad "They can still help! They promised me that they wouldn't tell anyone!"

    # familiar "You're a lot more trusting then I thought, Nadine."

    # "Think, Nadine! How do I get them not to hurt Cody?"

    # n customerservice "What if I introduced you?"

    # familiar "...Fine, but if they try to expose us, it won't end well."

    # n customerservice "How about tomorrow afternoon?"

    # familiar "Very well. Tell them to meet at 6pm, sharp. I will send you the address."

    # play sound "audio/sfx/17-sfx_callend.ogg"

    # "Oh, mercy. I feel sick."

    # #jump meeting_the_familiar

    # "Suddenly, I hear a knocking on the door."

    # ami "Nadine?"

    # n shocked "!"

    # "Act natural, Nadine."

    # n customerservice "Come in!"




    

    



    centered "Elsewhere..."

    scene bg hotel_sunset with fade 

    show boss neutral at leftish

    show xavier uniform at middling

    show yvette uniform at rightish

    show zuri uniform at farrightish
    with dissolve

    xavier "We can tell you now that the thief was of middling height, had light brown skin, and black hair."

    zuri "Also, they were wearing a black and white top, a domino mask, a black skirt, and black boots."

    if xaviersweet == True:

        show yvette confident with dissolve

        yvette "And her voice was smooth and soft when she said X was-"

        show xavier flustered

        show zuri outraged

        xavier "Y!"

        zuri "Shut your mouth!"

        show yvette thinking with dissolve

        yvette "Fine! I guess you don't want to see the sketch I made!"

        show screen facial_sketch with dissolve

        yvette "See?"

        hide screen facial_sketch

    "Boss" "Okay, that leaves me with one question-"

    show xavier thinking

    show zuri thinking

    show boss angry with vpunch

    "Boss" "HOW did you let the thief escape?!"

    show yvette thinking with dissolve

    yvette "Well, she threw a smoke bomb!"

    "Boss" "And you didn't catch her? You detectives are all useless!"

    show zuri outraged uniform 

    show xavier outraged
     
    show yvette sad uniform with dissolve

    yvette "..."

    xavier "Excuse me, but we're all doing our best!"

    zuri "Especially with what {i}little{/i} info you gave us!"

    "Boss" "I told you everything you needed to know!"

    xavier "All you said was, \"Someone stole from my hotel\". You didn't even say what they looked like. {i}We{/i} figured that out."

    "Boss" "Well, how was I supposed to know?"

    show xavier confident with dissolve

    xavier "Okay, what we can agree on is that this \"Shadow Angel\" has robbed your hotel twice, so they probably have a grudge against you. Do you know anyone who would have it out for you?"

    "Boss" "Of course not!" 

    yvette "Have you fired anyone recently?"

    show boss neutral with dissolve

    "Boss" "I'm constantly firing idiots. Like this one girl who had a klutz attack and nearly cost me a customer at the gala!"

    show xavier thinking

    show yvette thinking

    show zuri thinking
    with dissolve

    xavier "The gala? Would that happen to be right before the Shadow Angel attacked?"

    "Boss" "Yes. What's your point?"

    show xavier annoyed
    show yvette annoyed
    show zuri annoyed
    with dissolve

    "..."

    show xavier thinking

    xavier "Do you know the name of that employee?"

    "Boss" "Let me think. I think it was..."

    jump interrogation

    # scene bg city_day

    # show cody neutral at middling

    # c "Nadine? You okay?"

    # n uncertain street "Y-yeah, just a little nervous."

    # show cody sympathetic with dissolve

    # c "Don't be. It's not like you're introducing me to your parents."

    # n embarrassed "That's not funny."

    # c "So...where is this guy?"

    label interrogation:

        scene bg living_room with fade

        play sound "audio/sfx/doorbell.wav"

        "Who could that be?"

        n street "Who is it?"

        xavier "Private Investigators XYZ!"

        n shocked "!!!"

        "How did they find me here?!"

        yvette "May we come inside?"

        zuri "We have a warrant!"

        n shocked "Uh..."

        "Just open the door. They don't have anything on you yet."

        show xavier confident uniform at middling
        show yvette uniform at leftish
        show zuri uniform at rightish

        with dissolve

        n customerservice "What can I do for you?"

        xavier "Are you Nadine Bunker?"

        n customerservice "Yes..."

        show yvette confident with dissolve

        yvette "Great! We were hoping to speak with you."

        show yvette -confident

        show xavier thinking 
        with dissolve

        xavier "We understand that you work at Mellow Journeys, is that right?"

        n uncertain "Used to work."

        yvette "Were you laid off or did you quit?"

        n relief "I was fired."

        show yvette sad 

        yvette "I'm so sorry to hear that!"

        zuri "Anyway! You must've been p*ssed off after they fired you, {i}right{/i}?"

        n uncertain "...I was upset."

        show zuri glasses

        zuri "Upset enough for revenge?"

        n "Excuse me?"

        show xavier confident with dissolve

        xavier "What my colleague is saying is that sometimes people can do...impulsive things in the face of reject-"

        show xavier thinking

        show yvette thinking

        show zuri thinking

        ami "Nadine? Who's at the door?"

        "Oh, {i}great.{/i}"

        n "Just some workers!"

        ami "Oh, are they here to fix the radiator in the bathroom? Thank goodness!"

        n "Wait-"

        xavier "Ah, is there someone else who lives{nw}"

        show xavier flustered

        xavier "Ah, is there someone else who lives{fast}{cps=20} with...you...{/cps}"

        hide yvette
        hide zuri
        with dissolve
        
        show amia smile casual at rightish with dissolve:
            zoom 0.9

        ami "Hi! The bathroom's in-"

        show amia worried

        ami "You're not plumbers, are you?"

        show yvette confident uniform at leftish with dissolve

        yvette "Nope! We're private investigators, XYZ! Yvette!"

        xavier "..."

        show yvette thinking with dissolve

        yvette "Psst. X! That's your cue!"

        xavier "What? Q? T-there's no Q in XYZ!"

        show amia aww with dissolve

        ami "Pfft!"

        "And yet another man has fallen for Amia's charm."

        yvette "X, there's a serious issue we need to-"

        show yvette surprised 

        mocha "Meow?"

        "Right then, I feel Mocha rubbing against my knees."

        n relief "Hi, Mocha-"

        show yvette lovesick

        show amia shocked

        yvette "YOU HAVE A KITTY!!" with hpunch

        n sad "He's actually 3 years old-"

        show zuri annoyed uniform at farrightish with dissolve

        yvette "Hi, kitty! Hi kitty! Kitty kitty!"

        zuri "Oh {i}great{/i}."

        "I need a diversion."

        n "Amia, I think your rice might be burning!"

        show amia worried with dissolve

        ami "I didn't cook any rice-"

        n customerservice "I {i}really{/i} think we should check on the rice!"

        "Take the hint, already."

        ami "...Oooookaaay?"

        jump girlTalk

    label girlTalk:

        scene bg bedroom_day with fade

        # show amia sleepy pajamas at middling with dissolve

        # ami "I've had him since I was 10..."

        show amia worried casual at middling with dissolve

        ami "So that detective, the one with the sunglasses."

        n sad street "Yeah?"

        show amia aww

        ami "He's a total hunk, right?"

        menu is_xavier_hot:
            n uncertain "Um..."
            "For sure!":

                $character3affection += 5

                n embarrassed "I guess so..."

                show amia winking 

                ami "Oh, Nadine, you don't have to be embarassed!"

                "She's being way too loud!"

                n sad "He could hear us!"
            "Not really.":
                n "Not really."

                ami "Aw, you're no fun!"


        n "Anyways, we need to get them out of here."

        show amia worried with dissolve

        ami "Why are they even here, anyway? Did something happen?"

        menu detective_reasons:
            "Tell the truth":
                n "You know Mellow Journeys, where I used to work? There was a robbery a few days ago."

                show amia angry

                ami "By the Shadow Angel?"

                "How does she know that?"

                n "Ye...n...I don't know."

                ami "I can talk to them for you if you want."

                n shocked "Don't!"

                show amia worried 

                ami "How come? Why do they want to talk to you?"

                show amia angry
                
                ami "How come? Why do they want to talk to you?{fast} Unless..."

                n "!!!!!!"

                "No no no no no no no no no no..."

                ami "...They think you were a witness.{nw}"

                show amia worried 

                ami "...They think you were a witness.{fast} But you were fired before, right?"

                "{i}Phew.{/i}"

                n customerservice "Yes! That's right!"

                ami "Well, you should tell them that you weren't there!"

                "Now that I think about it, Amia gave me an idea."

                n "Actually, I think the rice could use some onions."

                scene bg living_room with fade

                show xavier thinking uniform at middling
                show yvette lovesick uniform at leftish
                show zuri annoyed uniform at rightish
                with dissolve

                yvette "Who's a good kitty? You are!"

                zuri "Y, need I remind you that we are here on {i}business{/i}?"

                show yvette surprised

                n street "Um, excuse me."

                show xavier flustered

                xavier "Y-yes, miss...{nw}"

                show xavier sad 
                show yvette thinking

                xavier "Y-yes, miss...{fast}ah, you're not...{nw}"

                show xavier confident

                xavier "Y-yes, miss...ah, you're not...{fast}well, then, Miss Bunker, about Mellow Journeys, there was a robbery recently."

                "Time to put some acting skills to use."

                n fakesurprise "{i}Oh, really?{/i}"

                show yvette neutral with dissolve

                yvette "Yes, at around 7:15pm. What time were you...laid off, exactly?"

                n uncertain "I don't remember."

                show zuri glasses

                zuri "Was it before or after the robbery?"

                n relief "...before."

                zuri "Reaaaaly? So going back to how you felt when you got fired..."

                n "Yes, I was angry. Yes, I felt vengeful."

                n -relief "Yes, I was angry. Yes, I felt vengeful.{fast} But I didn't rob from the hotel."

                "Specifically."

                show xavier thinking with dissolve

                xavier "But it does seem a bit suspicious about you getting fired minutes before a robbery."

                n "...I saw someone arrive shortly after I left the hotel."

                n "They asked me which way Mellow Journeys was, and I pointed it out."

                show yvette thinking with dissolve

                yvette "Interesting. What did they look like?"

                n sad "I don't remember, I was too upset to notice."

                "I cover my face and pretend to sniffle."

                show yvette sad
                show xavier sad
                show zuri thinking

                n crying "But the idea that I unwittingly helped someone commit such a horrible crime..."

                zuri "Did you know this person might want to steal from the hotel?"

                n relief "No."

                xavier "Then we can all assure you, you did nothing wrong."

                "Hook, line, and sinker."

                n relief "Thank you."

                yvette "Do you have any questions for us?"

                n "No."

                "The one with the sunglasses hands me a card."

                xavier "If you have any other information for us, just call."

                "With that, the detectives finally leave."

                hide xavier
                hide yvette
                hide zuri
                with dissolve

                "{i}Phew.{/i}"

                n "Hopefully they'll never come here again-"

                show amia crying casual at middling with dissolve

                n sad "Amia?"

                "Before I can answer say anything else, she pulls me in for a hug."

                ami "Aw, Nadine, I'm so, so sorry!"

                n "Mmhm."

                "Jeez, she's a lot stronger than she looks."
         

            "Lie":
                n "I don't know."

                ami "Well, we should go ask them!"

                n "Wait-"

                hide amia with dissolve

                "And she's gone."

                n "Amia, wait!"

                scene bg living_room with fade


                show xavier thinking uniform at middling
                show yvette lovesick uniform at leftish
                show zuri annoyed uniform at rightish
                with dissolve

                yvette "Who's a good kitty? You are!"

                zuri "Y, need I remind you that we are here on {i}business{/i}?"

                show amia casual worried at farleftish with dissolve:
                    zoom 0.9

                ami "Hello?"

                n relief casual "Excuse me."

                show xavier flustered 
                show zuri thinking
                with dissolve

                xavier "U-uh, yes, Miss Bunker and, uh..."

                ami "It's Amia."

                xavier "Of course. About Mellow Journeys, there was a robbery recently..."

                show amia angry 

                ami "We're aware of that."

                zuri "So if you don't mind, we were hoping to ask Miss Bunker some questions."

                ami "Where's your warrant?"

                show yvette thinking with dissolve

                "The taller detectives (X and Z?) pull their warrants out. The shortest one has to be nudged to get hers."


label mom:
    scene bg apartment_outside_sunset with fade

    show mama worried casual at middling with dissolve

    "Mom" "Is everything alright, Nadine?"

    n relief "Everything's fine, mom..."


                

    





    #jump amia_love

    
    # scene bg cafe_evening with fade

    # show cody sad winter at middling
    # with dissolve


    # c "Getting colder than usual, don't you think?"

    # n "I need to buy winter clothes."

    # scene bg apartment_outside_sunset with fade

    # show amia shocked winter at middling with dissolve

    # ami "Is the year over already?!"

    # n sad winter "Yeah."

    # show amia worried with dissolve

    # ami "A lot of people have been acting weird, lately."

    # n "Cody hasn't been returning my calls, either."

    # ami "Oh, I've been wondering..."

    # n "?"

    # ami "Are you and Cody...together?"

    # n shocked "What?"

    # menu:
    #     "No way":
    #         n customerservice "No no no no!"

    #         n deadpan "No no no no!{fast} No."

    #         show amia aww with dissolve

    #         ami "Oh, what a relief!"

    #         show amia shocked

    #         n -deadpan "Why do you ask?"

    #         show amia embarrassed

    #         ami "N-no reason!"

    #         "She's blushing a lot for some reason..."
    #     "Um...":
    #         n embarrassed "We're not {i}together{/i} together, but..."

    #         ami "He means a lot to you?"

    #         n embarrassed "...Yeah."

    #         show amia tired with dissolve

    #         ami "Oh...okay..."

    #         "She seems so sad."

    # "Oh. I get it. She likes Cody."

        



    # label glasses:

    #     scene bg hotel_hallway with fade

    #     show zuri cantsee uniform at leftish with dissolve

    #     zuri "Where are my glasses?! I can't see without them!"

    #     show xavier cantbeseen uniform at rightish with dissolve

    #     xavier "My glasses! I can't be seen without them!"

    #     scene black with fade

    #     centered "Six seconds later..."

    #     scene bg hotel_hallway with fade

    #     show zuri xaviersglasses uniform at leftish with dissolve

    #     show xavier wrongglasses uniform at rightish with dissolve

    #     "..."

    # label amiaWork:
        
    #     scene bg cafe with fade

    #     show amia smile uniform at middling with dissolve

    #     ami "Welcome, welcome! How can I help you?"

    #     show amia tired

    #     ami "(I can't afford to quit now...)"
            

label dad:
    scene bg apartment_outside_sunset with fade

    show dad happy casual at middling with dissolve

    "Dad" "Aren't you happy to see your old man?"

    n relief "Sure, Dad..."


label newsScoop:

    scene bg city_day

    "Okay, the coast is clear."

    "???" "Excuse me~!"

    n shocked street "Huh?"

    show livia happy uniform at middling with moveinleft

    liv "I'm Livia Porter from Daybreak News!"

    show livia trouble uniform with dissolve:
        zoom 0.6

    liv "Could I ask you a few questions?"

    




        

        






        

        












    










   

    




        

# # label amiaInLove:

# #     scene bg living_room with fade

# #     show amia worried casual at middling with dissolve

# #     n street "Hey, Amia."

# #     ami "Hi, Nadine..."

# #     "Hm…Amia seems distracted lately. She only gets like that when she's…"

# #     n "New crush?"

# #     show amia embarrassed

# #     ami "What? No!"

# #     n "..."

# #     ami "..."

# #     show amia worried

# #     ami "Am I really that predictable?"

# #     n deadpan "We've been roommates for a year."

# #     ami "I don't know what to do!"

# #     n -deadpan "What's he like?"

# #     ami "{size=*0.75}...she.{/size}"

# #     n "Pardon?"

# #     ami "It's a she!"

# #     "Oh. I didn't know Amia even…she always brought men over."

# #     n "Okay, what's she like?"

# #     show amia aww at middling with dissolve

# #     ami "She's {i}wonderful{/i}! She seems a bit cold at first, but she's super sweet once you get to know her! She's also really smart, and cool, and so, so {i}cute{/i}!"

# #     show amia worried with dissolve

# #     ami "But...I don't know if she feels the same way..."


    
        

    



  
    

    




    
        

    



        

    








    return
