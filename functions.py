from note_names import C, Db, D, Eb, E, F, Gb, G, Ab, A, Bb, B
from intervalsequences import rotation1, rotation2, rotation3, rotation4, rotation5, rotation6

def find_pcs_notes(notes):
    PCs = []
    for note in notes:
        if note in C and 0 not in PCs:
            PCs.append(0)
        elif note in Db and 1 not in PCs:
            PCs.append(1)
        elif note in D and 2 not in PCs:
            PCs.append(2)
        elif note in Eb and 3 not in PCs:
            PCs.append(3)
        elif note in E and 4 not in PCs:
            PCs.append(4)
        elif note in F and 5 not in PCs:
            PCs.append(5)
        elif note in Gb and 6 not in PCs:
            PCs.append(6)
        elif note in G and 7 not in PCs:
            PCs.append(7)
        elif note in Ab and 8 not in PCs:
            PCs.append(8)
        elif note in A and 9 not in PCs:
            PCs.append(9)
        elif note in Bb and 10 not in PCs:
            PCs.append(10)
        elif note in B and 11 not in PCs:
            PCs.append(11)
    PCs.sort()
    small = min(PCs)
    for i in range(len(PCs)):
        PCs[i] = PCs [i] - small
    return PCs

def find_pcs_booleans(booleans):
    PCs = []
    i = 0
    for boolean in booleans:
        if boolean == True:
            PCs.append(i)
        i += 1
    small = min(PCs)
    for i in range(len(PCs)):
        PCs[i] = PCs[i] - small
    return PCSet

def get_intervals(PCSet):
    PCSet.sort()
    intervals = []
    for i in range(len(PCSet)):
        if i < (len(PCSet) - 1):
            intervals.append(PCSet[i+1] - PCSet[i])
        else:
            intervals.append(12 - PCSet[i])
    return intervals

def rotate_intervals(intervals, st):
    rotated_set = None
    if intervals in rotation1:
        rotated_set = st
    elif intervals in rotation2:
        rotated_set = [st[1], st[2], st[3], st[4], st[5], st[0]]
    elif intervals in rotation3:
        rotated_set = [st[2], st[3], st[4], st[5], st[0], st[1]]
    elif intervals in rotation4:
        rotated_set = [st[3], st[4], st[5], st[0], st[1], st[2]]
    elif intervals in rotation5:
        rotated_set = [st[4], st[5], st[0], st[1], st[2], st[3]]
    else:
        rotated_set = [st[5], st[0], st[1], st[2], st[3], st[4]]
    return rotated_set

def get_best_normal_order(normal_order):
    #takes rotated_set, and returns prime form with all pcs given as numbers

def get_prime_form(numeric_prime_form):
    prime_form = []
    for pc in numeric_prime_form:
        if pc == 10:
            prime_form.append("T")
        elif pc == 11:
            prime_form.append("E")
        else:
            prime_form.append(pc)
    final_prime_form = ''.join(prime_form)
    return final_prime_form


#
