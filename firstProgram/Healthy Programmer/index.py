import datetime
from time import *
from datetime import *
from pygame import mixer


# Starting the mixer
mixer.init()

# Loading the song
mixer.music.load("Drink Water song.mp3")

# Setting the volume
mixer.music.set_volume(1.0)

total_water = 3.5 * 1000
dranked_water = 0

while True:
    sleep(15*60)
    while True:
        # Start playing the song
        music = True
        # while music:
        mixer.music.play()
        print("you need to drink atleast 200ml water this time ")
        drank_water = int(input("enter how much water have you drink in ml : "))
        x = input("Type 'done' after drink water: ")
        if (x == 'done') or (x == 'Done') or (x == 'DONE'):
            with open("water_logs.txt", "a") as f:
                f.write("at {},  you have drink {}ml water \n".format(datetime.now(), drank_water))
            # total_water - drank_water
            mixer.music.stop()
            music = False
            break
        else:
            continue
        continue
    continue