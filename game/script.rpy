# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Protag")
define n = Character("Narrator")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.
    
    "*BEEP* *BEEP* *BEEP*"
    
    "My eyes slowly open, and I realize that I was only dreaming. I then proceed to aggressively smash
     the power button on the alarm clock as if it had eaten my favorite pudding."
     
    p "Ugh. I really shouldn't have watched that much anime last night."

    "In actuality, I probably didn't even watch that much. The only issue is that I started at 2 AM, then ended at 3:30."
    
    "As I get out of bed, heading to the kitchen to make breakfast, I quickly glance at the clock that I just brutalized."
    
    p "Crud, it's already 8:30...I'm going to be super late!"
    
    "I skip my routine morning shower, throw on some clothes I picked at random from my closet, then bolt out the door."
    
    "I guess I should mention that I live on the 6th floor of my building, not really convenient when you, and just about everyone
     else in the dang dorm is running late to their first class."
    
    "I arrive at the elevator, and I notice that I just missed it."
    
    "Crap. I'll be late if I wait, so screw that. I'll just ..."
    
    menu:
        
        "run down the stairs":
            jump stairs
        
        "take the laundry schute":
            jump laundry_schute
    
    
    # This ends the game.

    return
    
label stairs:
    
    "Didn't die. Good job!"
    
    ".:. End"
    
    return
    
label laundry_schute:
    
    "...Not going to lie, I didn't even know this building even had a laundry schute. Laundry machines are on every floor after all."
    
    p "Well, here goes nothing I guess. GERONIMO!"
    
    "I then proceed to jump down the laundry schute. As I get in, I see the bottom."
    
    "There is no laundry hamper or anything to cushion my fall."
    
    p "FUUUUUUUUUUUUUUU-"
    
    "*crash*"
    
    "You died."
    
    ".:. Bad End"
    
    return
    
    
    
    
    
    
