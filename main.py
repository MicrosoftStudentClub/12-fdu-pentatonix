from module import *
import os
import pandas
import matplotlib.pyplot


def generate_midi_list():
    midi_list = []
    for root, dirs, files in os.walk("./data/train", topdown=False):
        for name in files:
            if name.endswith(".mid"):
                midi_list.append(os.path.join(root, name))
    return midi_list


def generate_music_list(midi_list):
    music_list = []
    for midi in midi_list:
        music_list.append(midi2music(midi))
    music_list.sort(key=lambda music: music.get_total_notes())
    return music_list


def print_music_list(music_list):
    for i, music in enumerate(music_list):
        print('Music {}: Notes {}, Length {}, Name {}'.format(i + 1, music.get_notes(), music.get_lengths(), music.name))


def show_histogram_of_notes(music_list):
    music_notes = []
    for music in music_list[:-10]:
        music_notes.append(int(music.get_total_notes()))
    data = pandas.Series(music_notes)
    data.hist(figsize=(10,6),bins=20)
    matplotlib.pyplot.show()


def show_histogram_of_lengths(music_list, seconds=False):
    music_lengths = []
    for music in music_list[:-10]:
        if seconds:
            music_lengths.append(int(music.get_total_lengths()/1000*0.67))
        else:
            music_lengths.append(int(music.get_total_lengths()))
    data = pandas.Series(music_lengths)
    data.hist(figsize=(10,6),bins=20)
    matplotlib.pyplot.show()
