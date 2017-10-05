from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey ")
    print("The fat bear is in front of another door")
    print("How are you going to move the bear? ")
    bear_moved = False

#This is an infinte while loop
    while True:
        next = input("> ")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")

        elif next == "taunt bear" and not bear_moved:
            print(" The bear has moved through the door. You can go through it now")
            bear_moved = True
            #if this part is satisfied, it runs the loop again since it's an infinite loop
            #It then asks for your input again

        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")

        elif next == "open door" and bear_moved:
            gold_room()

        else:
            print("I got not idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    next = input("> ")

    if "flee" in next:
        start()
        #if you flee from the room, you go back to the main room
    elif "head" in next:
        dead("Well that was tasty!")
        #if you eat your head you exit from the game
    else:
        cthulhu_room()
        #if none of the above then you enter into the cthulhu room again

def dead(why):
    print(why," Good job!")
    exit(0)
    # exit(0) aborts a program

#two doors and they call two functions for the bear room and the cthulhu room
def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    next = input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

#invokes the function start and starts the game
start()