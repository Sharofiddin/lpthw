from sys import exit

room_desc = {
    'bear_room':'''There is a bear here.
The bear has a bunch of honey.
The fat bear is in front of another door.
How are you going to move the bear?
    ''',
    'gold_room':'''This room is full of gold, How much do you take?
''',
    'cthulhu_room': '''Here you see the great evil Cthulhu.
He, it, whatever stares at you and you go insane.
Do you flee your life or aet your head?
''',
    'start_room': '''You are in a dark room.
There is a door to your right and left.
Which one do you take?
'''
}

def gold_room():
    print(room_desc['gold_room'])
    choice = input("> ")
    try:
        how_much = int(choice)
    except ValueError:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print(room_desc['bear_room'])
    bear_moved = False
    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed of and chews your legs off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I hot no idea what that means.")

def cthulhu_room():
    print(room_desc['cthulhu_room'])
    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print(room_desc['start_room'])
    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()

