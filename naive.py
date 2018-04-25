from main import generate_midi_list, generate_music_list
from module import Music, Track, music2midi
import pickle
import random

def get_freq_dict(pitch=True,length=False):
    midi_list = generate_midi_list()
    music_list = generate_music_list(midi_list)
    mat = {}
    fq = {}

    for music in music_list:
        if pitch and length:
            previous = 128,0
        elif pitch and not length:
            previous = 128

        track = music.get_single_track()
        note_count = track.get_note_count()
        for i in range(0, note_count):
            try:
                if pitch and length:
                    current = track.get_pitch_with_index(i), track.get_lengths_with_index(i)
                elif pitch and not length:
                    current = track.get_pitch_with_index(i)
                if previous not in mat:
                    mat[previous]= {}
                if current not in mat[previous]:
                    mat[previous][current] = 0
                mat[previous][current] += 1
                previous = current
            except:
                pass

    for previous in mat:
        sum_row = sum(mat[previous][current] for current in mat[previous])
        for current in mat[previous]:
            mat[previous][current] /= sum_row
        fq[previous] = sorted(mat[previous],key=lambda x:-mat[previous][x])
        #print(mat[previous])
        print(previous, fq[previous])

    return mat,fq


def naive_short_music(mat,fq):
    return mat,fq

def generate_random_number(a, b):
    return int(random.random() * (b - a) + a)

def naive_generation():
    mat, fq = get_freq_dict()
    generate_music = Music()
    track = Track()
    generate_music.add_track(track)

    current_note = 128
    max_len = len(fq[128])
    next_note = fq[128][generate_random_number(0, 5)]
    for i in range(0, 30):
        track.add_note(next_note, generate_random_number(1, 5) * 512)
        current_note = next_note
        max_len = len(fq[current_note])
        next_note = fq[current_note][generate_random_number(0, min(max_len, 3))]

    music2midi(generate_music, "new_music.mid")

def naive_generation_with_time(fq, file_name, length):

    generate_music = Music()
    track = Track()
    generate_music.add_track(track)

    random_range = generate_random_number(4,8)
    current_note = 128, 0
    max_len = len(fq[128, 0])
    next_note = fq[128, 0][generate_random_number(0, 5)]
    for i in range(0, length):
        track.add_note(next_note[0], next_note[1])
        current_note = next_note
        max_len = len(fq[current_note])
        next_note = fq[current_note][generate_random_number(0, min(max_len, random_range))]

    music2midi(generate_music, file_name)

if __name__ == "__main__":
    mat, fq = get_freq_dict(pitch=True, length=True)
    for i in range(0,30):
        name = "./argument2to6len8/naive_" + str(i + 1) + ".mid"
        naive_generation_with_time(fq, name, 8)