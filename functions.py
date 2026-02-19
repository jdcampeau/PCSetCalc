from note_names import C, Db, D, Eb, E, F, Gb, G, Ab, A, Bb, B

def find_pitch_classes(notes):
    PCsets = []
    for note in notes:
        if note in C and 0 not in PCsets:
            PCsets.append(0)
        elif note in Db and 1 not in PCsets:
            PCsets.append(1)
        elif note in D and 2 not in PCsets:
            PCsets.append(2)
        elif note in Eb and 3 not in PCsets:
            PCsets.append(3)
        elif note in E and 4 not in PCsets:
            PCsets.append(4)
        elif note in F and 5 not in PCsets:
            PCsets.append(5)
        elif note in Gb and 6 not in PCsets:
            PCsets.append(6)
        elif note in G and 7 not in PCsets:
            PCsets.append(7)
        elif note in Ab and 8 not in PCsets:
            PCsets.append(8)
        elif note in A and 9 not in PCsets:
            PCsets.append(9)
        elif note in Bb and 10 not in PCsets:
            PCsets.append(10)
        elif note in B and 11 not in PCsets:
            PCsets.append(11)
        else:
            continue
    return PCsets


#
