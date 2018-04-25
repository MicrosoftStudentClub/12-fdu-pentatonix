from main import generate_midi_list, generate_music_list, print_music_list
import random
import os
def divide(midi_list):
    cnt = 0
    for i in range(200):
        t = random.randint(0,4)
        for j in range(5):
            s = i * 5 + j
            name = midi_list[s].split("\\")[1]
            if j == t:
                os.system("cp melody/%s data/test"%(name))
                os.system("mv data/test/%s data/test/data%d.mid"%(name,cnt))
                cnt+=1
            else:
                os.system("cp melody/%s data/train"%(name))
                os.system("mv data/train/%s data/train/data%d.mid"%(name,s-cnt))


if __name__ == "__main__":
    midi_list = generate_midi_list()
    divide(midi_list)