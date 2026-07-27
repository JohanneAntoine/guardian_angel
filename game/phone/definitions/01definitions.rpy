# /!\ default
# pc as in phone character :monikk:
default pc_cody  = phone.character.Character("Cody", phone.asset("cody_icon.png"), "c", 21, "#eec35e")
default pc_mc      = phone.character.Character("Nadine", phone.asset("nadine_icon.png"), "n", 35, "#484848")


default pov_key = "n"


init 100 python in phone.application:
    add_app_to_all_characters(message_app)
    add_app_to_all_characters(call_history_app)
    add_app_to_all_characters(calendar_app)

init 100 python in phone.calendar:
    add_calendar_to_all_characters(2023, 6, MONDAY)

init phone register:
    define "Welcome":
        add "c" add "n"
        icon phone.asset("default_icon.png")
        as thanks_for_using_my_framework key "ddu"

label phone_discussion_test:
    phone discussion "ddu":
        time year 2023 month 6 day 5 hour 16 minute 30 delay -1 # exact date and time at which i wrote this. yes i am feeling quite silly and goofy

        "c" "Good luck at work today."

        "n" "Thanks."


    phone end discussion

    jump hangup

label cody_text:
    phone discussion "ddu":
        time year 2023 month 6 day 5 hour 16 minute 30 delay -1 # exact date and time at which i wrote this. yes i am feeling quite silly and goofy

        "c" "Need to talk to you tomorrow."


    phone end discussion

    jump cody_confrontation


label cody_wingman:
    phone discussion "ddu":
        time year 2023 month 7 day 5 hour 16 minute 30 delay -1 

        "n" "Someone just told me they have a crush on me."

        "c" ":O"

        "c" "Who??"

        "n" "You don't know them."

        "n" "What do I do????"

        "c" "Do you like them back?"

        "n" "I don't know."

        "c" "How do you feel about them?"

    phone end discussion

    jump love_epiphany




# label phone_call_test:
#     phone call "s"
#     phone_s "Ohayouuu!!!!!!!!!!!!!!!!"
#     phone_mc "Hey!"
#     "Why is she always this energetic?"
#     phone end call
#     "..."

#     return