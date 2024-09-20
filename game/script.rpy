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


#characters
define n = Character("Nadine", color="#c7a8fc", image="nadine")
define shadow = Character("Nadine", color="#c7a8fc", image="shadowangel")
define c = Character("Cody", color="#ecce0a")
define mocha = Character("Mocha", color="#A0522D")
define ami = Character("Amia", color="#FF1493")
define familiar = Character("???", color="#FFFFFF")
define cordis = Character("Cordis", color="#f677b2")
define angel = Character("Angel", color="#FF1493")

#images
image nadine:
    "side nadine.png"

image shadow:
    "side shadowangel.png"

define flash = Fade(.25, 0.0, .75, color="#fff")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg cafe

    # These display lines of dialogue.
    "TV" "Welcome to Daybreaker News! I'm your host, Livia Porter! A near-disaster has thankfully been averted thanks to our very own Guardian Angel of Love!"
    
    "TV" "For nearly 10 years, our town's shining angel has been saving this town from constant..."

    "Random Person" "Did you see the Guardian Angel of Love's interview today?"

    "Random Person 2" "She's so cool!"

    "Whoever this Guardian Angel is, she sure is lucky. Bet she never has to deal with job applications."

    "Suddenly, I feel a tap on my shoulder."

    show cody neutral at middling with dissolve

    c "Hey, you."

    n smile "Hey yourself."

    c "How's the job search going?"

    "I groan."

    show cody sympathetic with dissolve

    c "Well at least you have that busing job to pay off those student bills for now." 
    
    "I groan more loudly."  

    "Cody ignores that and continues."

    c "By the way, don't you have that fancy gala tomorrow?"

    "I groan even more loudly."

    n tired "My boss has been crazy all month about it."

    c "Hey, look at the bright side, you might get free food out of it."

    n uncertain "I doubt it. I'll let you know how it went afterwards."

    show cody smile with dissolve

    c "That's my girl. See you around."

    "Alright then, back to work."
    
    scene bg hotel with fade
    
    "Boss" "Bunker! You're late!"

    n "I'm sorry sir."

    "By ten whole seconds."

    "Boss" "I hope this won't be a repeat offense. We have important clientele tomorrow. Do not ruin this for me."

    n "Yes, sir."

    "Miserable sack of greed."

    "Well, might as well get started. The faster I do it, the less angry he'll get."

    scene black with fade

    centered "3 hours later..."

    scene bg hotel_sunset with fade

    "Thank goodness the day's over. I can't wait to go home and watch some-"
    
    "Boss" "BUNKER!"

    n "Yes, sir?"

    "Of-freaking course."

    "Boss" "Some idiot threw up in the bathroom. Here's a mop! I'd clean it myself, but I'm too busy and have better things to do than cleaning up other people's mess."

    n "...Yes, sir."

    "Self-absorbed tool. Hopefully the mess won't be too ba-"

    n shocked "MOTHER OF-{cps=4.5} {/cps}{nw}"

    scene black

    centered "1 hour later..."

    scene bg city with fade

    play sound "audio/sfx/16-sfx_dial.ogg"

    $ renpy.pause(6, hard=False)

    stop sound 

    c "Hello?"

    n tired "Hey, Cody..."

    c "Oh, Nadine! What's up? Your voice is shaky."

    n tired "Vomit clean up."

    c "Oh, yikes. What are you doing now?"
    
    n tired "Right now, I'm going home, and I'm going to get wasted."

    c "What about the important dinner tomorrow?"

    n tired "Cr*p. Do you think I can call in sick if I get hungover?"

    c "Would your boss let you?"

    n tired "Ugh, no. At least I have Mocha."

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

    show amia neutral at middling with dissolve

    n "Oh, hey, Amia, and...friend."

    "I wonder how long this boytoy will last."

    show amia smile at middling with dissolve

    ami "Oh, hi, Nadine!"

    "Amia's Date" "Who's this chick?"

    show amia neutral at middling with dissolve

    ami "Oh, this is my roommate. I told you I had one, remember?"

    "Amia's Date" "You didn't tell me you had a roommate."

    show amia annoyed at middling



    ami "I'm prety sure I did!"

    "Amia's Date" "So do you have, like hot lesbo sex or something?"

    show amia embarrassed at middling

    ami "..."

    n embarassed "...I'm going to my room."

    "This is the last thing I need today."

    play sound "audio/sfx/19-sfx_doorclose.ogg"

    hide all

    scene bg bedroom_night with fade

    n smile "Hi, Mocha. You don't know how happy I am to see your friendly, furry face."

    show mocha at cat_middling with dissolve

    play sound "audio/sfx/20-sfx_meow.ogg"

    mocha "Meow."

    n smile "I had a rough day today, so we're just going to watch some comedy shows and-{nw}hm?"

    n neutral "I had a rough day today, so we're just going to watch some comedy shows and-{fast}hm?"

    "The job listing I took falls out of my pocket."

    "...fine. I'll just get my laptop, and then TV time."

    #draw laptop

    "Same old questions…resume…demographics…and send. Okay, that settles that, now it's relaxation time!"

    scene black with fade

    centered "The next day..."

    scene bg hotel with fade

    "Haven't gotten any answer from Angine Tech yet. I hope they answer soon. I reall need this-"

    "Boss" "Bunker?"

    n "Yes, sir?"

    "Boss" "Thank you for being on time today."

    "Do the other hundreds of days I've been on time not count?"

    "Boss" "After all, you don't want to make me look bad in front of {i}very important clients{/i}, do you?"

    n "No, sir."

    "Boss" "Good, now back to work. And don't forget to smile!"

    "Okay. It's just one dinner. How bad can it be?"

    scene black with fade
    
    centered "Later that evening..."

    scene bg hotel_sunset with fade

    n customerservice "Welcome! We're so glad to have you here at our gala!"

    "Rich Man" "Yes, yes, where's my table, miss?"

    n customerservice "Right this way, sir."

    "This is the first one who actually called me by a title. Maybe he'll remember to say thank you."

    "Boss" "BUNKER! MORE GUESTS ARE WAITING!"

    n customerservice "Coming!"

    "Oh, I better ace that job interview."

    n customerservice "Good evening, gentlemen, we're so glad to have you here at our gala!"

    "Rich Dude" "Good evening to you, toots!"

    "Oh, no."

    n customerservice "...Let me guide you to your seats."

    "Second Rich Dude" "Sure thing, as long as you're leading the way, babe!"

    "Remember your calming strategies, Nadine. You don't have a backup job yet."

    n customerservice  "If there's anything else you need-"

    "Perish the thought."

    n customerservice "Please let me know!"

    "Rich Dude" "Hey waitress!"

    "D*mmit."

    $ _preferences.text_cps = 10

    n tired "...{nw}"

    $ _preferences.text_cps = 80

    n customerservice "...{fast}Yes?"

    "Rich Dude" "Haven't I seen you somewhere before?"

    n customerservice "I don't think so!"

    "I would definitely remember someone like {i}him{/i}."

    "Rich Dude" "No, no, I recognize your face. You remind me of someone. Doesn't she look familiar, Ricky?"

    "Great. Now the two stooges are staring at me. The {i}one time{/i} my boss isn't on my case to do something else…"

    "Ricky" "Oh yeah, I see it! She looks like that exotic dancer you used to date!"

    "Rich Dude" "Yeah, yeah! Man she had such a big-"

    "That's it. That's it. I can't listen to this anymore. I turn to get the heck away from the table, only to bump into someone and hit the ground."

    "Karen" "WATCH IT!" with hpunch

    "Oh, gosh, is this wine?!"

    "Karen" "You ruined my dress! HOW DARE YOU!"

    n sorry winestain "I'm sorry ma'am, it was an-"

    "Karen" "Do you know much this dress costs?! More than your entire salary!"

    "Boss" "What is going on here?!"

    "Oh no."

    n sorry winestain "I-"

    "Karen" "This {i}stupid girl{/i} ruined my dress!"

    "Why is {i}she{/i} crying? Her stain isn't that big!"

    "Boss" "My apologies, madam. I'm sure that we can cover for-"

    "Karen" "This dress cost me a {i}fortune{/i}! All because of her! Don't think I'll ever come to this dump again!"

    "Boss" "Look at what you've done, Bunker!"

    n sorry winestain "Sir, I-"

    "Boss" "We could have lost a valuable client because of your carelessness!"

    n sorry winestain "I didn't-"

    "Boss" "No excuses! Pack whatever stuff you have, because you are FIRED!"

    "Rich Dudes" "Oooooh."

    "Karen" "Hmph!"

    "No, no, no. This can't be happening."

    "I need to get out of here before I completely break down."

    scene bg city with fade

    "Should I call Cody? No, it's too late in the evening for that. I guess I'll just call a taxi."

    play sound "<from 1.0 to 2.0>audio/sfx/21-sfx_ringtone.ogg"

    "What now?!"

    "Angine Tech? What the h*ll, I have nothing else to lose."

    n tired winestain "Hello?"

    familiar "Good evening, Nadine. Did I get your name right?"

    n tired winestain "Yes."

    "First one to call me by my first name in the last 3 hours."

    familiar "Excellent. I will be the one conducting the interview with you. Are you in a good place to talk?"

    n tired winestain "I'm on the street. I…just got out of work."

    "Outside my {i}former{/i} place of work."

    familiar "Yes, yes, I remember on your application that you currently work at Mellow Journey Hotel. Were they not having a gala this evening?"

    n tired winestain "Yes."

    familiar "I suppose you just had to be a glorified cheerleader for all those rich people."

    "Is this a trick to get me to complain about my job?"

    n sorry winestain "No, I…just help clients to their tables and offer them food and drinks. I also do janitorial services sometimes."
 
    familiar "That's all? Doing things that they could easily do themselves? Do they appreciate you? Thank you?"

    "My boss thanked me for 'being on time today.'"

    n tired winestain "...No."

    familiar "It sounds like they're using you to fill their own pockets, Ms. Bunker. Swimming in their wealth, with no concern for the hard-workers who helped get them where they are today. "
    
    familiar "Doesn't it infuriate you? Don't you want to get back at all of them? Take back what is rightfully yours?"

    n uncertain winestain "Well..."

    familiar "Don't you want to start anew?"

    "This interviewer's reading my mind, but I don't even know what their name is. What should I say?"

    menu optional_name:
        "'I guess...'":
            "I don't know. Maybe I was just too tired. Maybe it was the stress of losing my job, but I find myself saying-"

            n uncertain winestain "I guess so..."

            familiar "Don't worry. You're doing the right thing."
        "'Yeah, I do!'":
            $ wickedPoints += 1
            "I think about everything that happened tonight. The backhanded compliment from my boss. Those overgrown frat boys. That horrid woman. It's all too much."

            n angry winestain "Yeah... yeah, I do!"

            familiar "I knew you would see it our way."
    
    familiar "Now, focus and say: 'Shadow Form, Activate!'"

    "'Shadow Form'?"

    "I don't know exactly what I've gotten myself into, but I'm ready to take a new chance."

    n shouting "Sh-shadow form, activate!"

    scene bg transformed with flash

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

    "Boss" "Welcome, Miss! Please, please! Let me lead you to your seat."

    show becky smile at middling with dissolve

    "Rich Woman" "Why, thank you!"

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

    show becky wah at middling

    "Becky" "Ack-!"

    "Tommy" "What is it?"

    "Becky" "Your wallet..."

    "Cr*p. Busted. What should I do? I dive into the girl's shadow, hoping that no one else will notice."

    "Tommy" "Hey, where's my wallet?"

    "Becky" "It-it just went into my shadow!"

    "Tommy" "Is that right? What are you going to tell me next, unicorns are real?"

    show becky angry at middling

    "Becky" "I'm serious!"

    "Tommy"  "Yeah, yeah. I'm sure it just fell on the floor or something."

    "Tommy crouches down to look for his wallet. I'm never going to escape at this rate."

    "Tommy" "Where is it? You didn't take it, did you, Becky?"

    "Becky" "No! I swear!"

    "Maybe I could sneak away while these two are arguing. I sneak out of Becky's shadow and…"

    show becky wah at middling

    "Becky" "THERE IT IS!" with vpunch

    "Tommy" "{i}What the h*ll?{/i}"

    "Oh no. Now all eyes are on me."

    "Karen" "A THIEF!"

    "Boss" "STOP HER!"

    "Everyone's coming towards me, what do I do?!"

    familiar "Smoke Bomb."

    shadow uhoh "what?"

    familiar "You have a smoke bomb on your belt. Use it!"

    menu:
        "No time to second guess myself. I locate the smoke bomb, a small, white ball, and throw it..."
        "On the ground":
            $ wickedPoints -= 1
            "Becky" "I can't see!"

            shadow cautious "Sorry!"
        "At the closest person":
            $ wickedPoints += 1

            "Tommy" "AGH!" with hpunch

            shadow confident "Oops. Sorry."

            "Not really."
        

    "While the room's covered in smoke, I jump out a window into the night."

    scene black with fade

    centered "One Hour Later..."

    scene bg living_room with fade

    show amia worried at middling with dissolve

    ami "Oh my gosh, Nadine! What happened to your-"

    "I rush to my room without a word to her."

    scene bg bedroom_night with fade

    show mocha at cat_middling with dissolve

    play sound "audio/sfx/20-sfx_meow.ogg"

    mocha "Meow?"

    n tired winestain "You don't want to know the day that I had."

    "I dig into my pocket to see if the wallet is still there. It is. I flop on my bed."

    play audio "<from 1.0 to 2.0>audio/sfx/21-sfx_ringtone.ogg"

    n tired winestain "Hello?"

    familiar "You've done well for your first heist. We're pleased to offer you a position at our company."

    "Heist?!"

    n angry winestain "That was the scariest thing I've ever done!"

    "And yet...the most exhilarating."

    familiar "Consider what you took as your first payment."

    "I look at the contents of the wallet. At least five hundred dollars in twenties."

    "What have I gotten myself into?"

    hide all

    scene black with fade

    centered "The next day..."

    scene bg city with fade

    "Clerk" "Alright, thank you for your purchase. Have a nice day."

    show cody neutral at middling with dissolve

    c  "Ooo, are we splurging today? What's the occasion?"

    n casual "Well, I got fired last night."

    show cody sympathetic at middling


    c  "Aw, sorry, 'dine. Did you hear back from other companies?"

    if wickedPoints > 0:
        n smile casual "Something like that."

    else:
        n neutral casual "...Something like that."

    "Cody grins ear to ear and gives me a one-armed hug."

    show cody smile at middling with dissolve

    c "I knew you'd find something!"

    n smile casual  "Yep. Good thing I lost that other job, given what happened last night."

    show cody neutral at middling

    c "What happened?"

    hide all

    scene black with fade

    centered "Meanwhile..."

    scene bg city with fade

    "TV" "...witness claims that the suspect wore something resembling our very own Guardian Angel of Love. Could this 'Shadow Angel' be connected to the town's heroine? Up next…"

    show cordis at leftish with dissolve

    cordis "Angel, what do you make of this?"

    show angel angry at rightish with dissolve

    angel "...Tch."

    hide all

    scene black with fade

    centered "To be continued..."


    return

