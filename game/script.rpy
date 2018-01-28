# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Protag")
define c = Character("Clegg")


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
    
    scene bg elevator
    
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
    
    "While it may seem like this is my first time running late, it's actually quite the opposite."
    
    "There is barely a day when I'm NOT running late."
    
    "During those days (ie every day), the combination of the stairs and my seemingly-limitless stamina have always
     been my best friend."
    
    "Today is no different."
    
    p "Time for my morning workout!"
    
    "As I am running (and oftentimes, jumping) down the stairs, I hear the familiar sounds of *clink* and *CLANG*. For some reason,
     these sounds have always calmed me down whenever I'm stressed about my punctuality."
    
    "I make it down to the ground floor in less than a minute, even beating the elevator."
    
    p "Good stuff!"
    
    "I run out the door in a triumphant manner, however there's no time for me to celebrate."
    
    "My class is at 8:45. Currently, it's 8:34. Not too bad, except the distance to the lecture hall from my dorm is around 15 minutes by foot."
    
    "Well, if I walk. If I run, I should just barely make it."
    
    "While I'm running, let me tell you a bit about myself."
    
    jump running
    
    
    
label laundry_schute:
    
    "...Not going to lie, I didn't even know this building even had a laundry schute. Laundry machines are on every floor after all."
    
    p "Well, here goes nothing I guess. GERONIMO!"
    
    "I then proceed to jump down the laundry schute. As I get in, I see the bottom."
    
    "There is no laundry hamper or anything to cushion my fall."
    
    p "...FUUUUUUUUUUUUUUU-"
    
    "*crash*"
    
    "You died."
    
    ".:. Bad End"
    
    return
    
    
    
    

label running:
    
    "I'm currently a sophomore computer science major at DKU."
    
    "Before you ask me what 'DKU' stands for, don't. Nobody I know (including my friends, classmates, and even professors) knows what it stands for. 
     Is it weird? You bet. Do I care? Not really."
    
    "All I know is that its CS program, while not very well known, is good enough that I can easily learn what I need to know, and that's all that really
     matters to me."
    
    "Being a CS major at DKU is a lot like being a CS major at lots of other universities. While school does matter, what you do outside of school matters
     loads more to companies that are thinking about hiring you."
    
    "This could be done in several ways: getting involved in technical clubs, working on open source projects, writing software yourself, volunteering to write code
     , etc."
    
    "Some people love this about the CS industry, mostly those who devote no time to school and just write code for fun anyway."
    
    "Then you have other people who don't necessarily write code in their free time ALL the time, but make up for it with excellent grades, connections to the industry,
     and just sheer brilliance and charisma."
    
    "I, unfortunately, lie in neither of these categories."
    
    "While I do enjoy coding, and am certainly not a slouch when it comes to my academics, something about me just can't sit down and work on my on project simply
     because I don't have a project that I really want to work on."
    
    "I'm the kind of guy where, as long I have a comfy chair, a nice computer filled with anime and games, a few snacks and a working bathroom, can sit for
     a really long time with no complaints whatsoever."
    
    "That being said, I do worry a lot about whether or not I'll get a good internship for the summer, or if i'll even get hired after college."
    
    "Thankfully, I have friends that help me get through my troubles"
    
    "*bzzt bzzt*"
    
    "I whip out my phone while I'm still in full sprint."
    
    "'HEY! Class is about to start! Get your lazy ass over here already!'"
    
    "It's a text from my best friend at DKU, Asher. I refer to him as 'Clegg' cuz that's his last name. Also, it's a much more interesting name than 'Asher.'"
    
    p "Jeez Clegg I'm on my way you impatient SOB!"
    
    "I end up rushing myself even further, almost breaking down in front of the lecture hall."
    
    jump magic1
    

label magic1:
    
    "As I walk in, I immediately see Clegg, who placed his backpack on the seat next to him, , obviously meant for me."
    
    c "Perfect timing. Mark's about to start. Are you okay? You seem winded AF."
    
    p "Really? What gave it away? My sweat-drenched shirt? My red face? Maybe my irregular breathing. Or is it my near inability to speak? Oh waiiiiit it could be -"
    
    c "Yeah yeah I get it. Just get ready quickly, you know he doesn't start class until everyone stops talking."
    
    "Understanding his words to be the truth, I get out my laptop and get ready for lecture."
    
    "I guess I should explain what's going on, huh. I'm currently sitting in my 'Magic, Medicine and Science' class. No, it's not as interesting as you're thinking.
     I know because I had the same thoughts when I enrolled in it."
    
    "It's a history class that basically touches upon the development of 'Magic' into current-day science. It sounds cool, and it probably is, but I haven't
     introduced the main source of misery for this class: Dr. Mark Singh."
    
    "While he himself is probably a really nice guy, he can't lecture to save his life. He just walks in every lecture with LITERAL PRINTOUTS of the textbook, and 
     proceeds to just read off them for an hour and fifteen minutes."
    
    "This is probably where you're asking: 'Why are you even in a history class in the first place?' Long story short, I needed a history gen-ed, and Clegg said 
     he needed a history elective for his major (he's a dual History-Physics major)."
    
    "As you can probably understand by now, I'm not enjoying the class so much. It's at an early time, and the professor can't teach. One other issue that I 
     haven't mentioned, however, is the room that the lecture is held in."
    
    "This is one of several lectures halls at DKU, but this one's special in that it was recently renovated. Over the summer, actually."
    
    "The old rooms were dark, the systems used for hooking a computer up to the project were archaic, and the room had chalkboards instead of whiteboards. 
     By contrast, the new rooms had very new projectors, whiteboards, and one side of the room (depending on which room you were in) had a large window showing 
     the nice, bright outside."
    
    "My issue there though, is that I loved the old rooms. The rooms were dark, making it easy for me to sleep during class. The technology may have been archaic, 
     but lots of experimentation by various professors over the years ensured that they always worked seamlessly. Lastly, I prefer chalkboards over whiteboards."
    
    "This new room, however, was exactly the opposite. Whiteboards were used, which isn't really a big deal, but the technology malfunctions a lot because many professors
     owned older laptops, leading them to gerry-rig solutions that didn't always result in the strongest connection between their laptop and the projector."
    
    "My absolute least favorite part though, is by far the window on the right side of the room."
    
    "It's already bad enough that I only have morning classes here, rendering me unable to sleep because of the bright outdoors, but many couples frequent the
     area on the other side of the window for romantic rendesvous."
    
    "Let me set something straight: I don't have anything against romance."
    
    "I do, however, have things against couples that openly show flaunt their happiness in public. Screw them, they're already happy, why do they have to 
     make us single people feel like losers!??!"
    
    
    "Didn't die. Good job!"
    
    ".:. Placeholder Ending"
    
    return
    

    
    
    
    
    
