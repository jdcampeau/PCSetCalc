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
    return PCs

def find_pcs_booleans(booleans):
    PCs = []
    i = 0
    for boolean in booleans:
        if boolean == True:
            PCs.append(i)
        i += 1
    return PCSet

def get_intervals(PCSet):
    PCs = PCSet.copy()
    PCs.sort()
    small = min(PCs)
    for i in range(len(PCs)):
        PCs[1] = PCs[1] - small
    intervals = []
    for i in range(len(PCs)):
        if i < (len(PCs) - 1):
            intervals.append(PCs[i+1] - PCs[i])
        else:
            intervals.append(12 - PCs[i])
    return intervals

def get_normal_order(intervals):
    max = max(intervals)
    idx = 0
    for int in intervals:
        if int != max:
            idx += 1
        else:
            idx += 1
            break
    if idx != len(intervals): #This reliably handles only cases where there is only one of the largest interval within the set/chord.
        sect_a = intervals[idx:]
        sect_b = intervals[0:idx]
        sect_a.extend(sect_b)
        new_intervals = sect_a #Further study is needed to determine the most efficient code for handling all possible cases.
    else:
        new_intervals = intervals
    n_o = [0]
    pc = 0
    for int in new_intervals:
        pc += int
        n_o.append(pc)
    if n_o[-1] != 12:
        raise ValueError("Intervals passed in do not equal exactly one octave.")
    del n_o[-1]
    return n_o, new_intervals

def get_best_normal_order_hex(n_o, new_intervals): #An additional get_bno func will be needed for each set type trichord-decachord
    if any ([                                      #These will be helper funcs called within a main get_bno func based on set type
        (n_o[1] - n_o[0]) > (n_o[5] - n_o[4]),     #No get_bno func needed for unisons, dyads, undecachords, or duodecachords
        (n_o[1] - n_o[0]) == (n_o[5] - n_o[4]) and (n_o[2] - n_o[1]) > (n_o[4] - n_o[3])
    ]):
        max = new_intervals.pop()
        new_intervals.reverse
        new_intervals.append(max)
        bno = [0]
        pc = 0
        for in in new_intervals:
            pc += int
            bno.append(pc)
        del bno [-1]
    else:
        bno = n_o
    return bno

def get_prime_form(numeric_prime_form): #Does this return a list with one item or a string?
    prime_form = []
    for pc in numeric_prime_form:
        if pc == 10:
            prime_form.append("T")
        elif pc == 11:
            prime_form.append("E")
        else:
            prime_form.append(pc)
    final_pf = ''.join(prime_form)
    return final_pf


#
