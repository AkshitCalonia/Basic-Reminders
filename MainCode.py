import time
import datetime
from pygame import mixer


initial2 = time.time()
for i in range(15):
    # 15 times loop will repeat bcz its 9 to 5 job and the reminder will come in every 30 minutes between 9 a.m. and 5 p.m. in 16 segments

    time.sleep(1800)
    #its 1800 actually

    # Starting the mixer
    mixer.init()

    # Loading the song
    mixer.music.load("physical.mp3")

    # Start playing the song
    mixer.music.play(-1)

    initial_time = time.time()

    print("Please do some exercise for atleast 1 min and then Type 'ExDone' to Stop this shitting sound")
    inp = input(" : ")

    if inp == "ExDone":
        # Stoping the music
        mixer.music.stop()
        EX = time.time() - initial_time
        print(f"You relaxed your FiT body by doing exercise for {EX} second(s)! ")


    time.sleep(900)
#its 900 actually


    # -----------------------------------------------------------------------------------------------------------------------------------------------



    # Starting the mixer
    mixer.init()
    # Loading the song
    mixer.music.load("water.mp3")

    # Start playing the song
    mixer.music.play(-1)

    initial_time = time.time()

    print("Please Drink 200 ml water and then Type 'Drank' to Stop this shit sound")
    inp = input(" : ")

    if inp == "Drank":
        # Stoping the music
        mixer.music.stop()
        WR = time.time() - initial_time
        print(f"You Drank the water in {WR} seconds! ")

    time.sleep(5)
    #its  5 actually
    # -----------------------------------------------------------------------------------------------------------------------------------------------

    # Starting the mixer
    mixer.init()

    # Loading the song
    mixer.music.load("eyes.mp3")

    # Start playing the song
    mixer.music.play(-1)

    initial_time = time.time()

    print("Please rest your eyes and then Type 'EyDone' to Stop this shitting sound")
    inp = input(" : ")

    if inp == "EyDone":
        # Stoping the music
        mixer.music.stop()
        EY = time.time() - initial_time
        print(f"You relaxed your BEAUTIFUL eyes in {EY} seconds! ")



x = datetime.datetime.now()

Total_time = (time.time()-initial2)-2*(5+900+1800)
print(f"Hey!, Today ({x}), You had kept your body fit during the whole 9to5 job ! "
      f"And doing this all (including drinking, relaxing eyes and your body), had collectively taken {Total_time} seconds")

f = open("Records_Of_Activities_By_Akshit.txt", "a")
a = f.write(f" \nActivity done on {x} and collectively taken {Total_time} in all \nDoing Ex"
            f"ercise on this day had taken {EX} seconds \nDrinking Water on this day had t"
            f"aken {WR} seconds \nRelaxing Eyes on this day had taken {EY} seconds\n ")
print(a)
f.close()

#.......
#......
#.....
#....
#...
#..
#.

