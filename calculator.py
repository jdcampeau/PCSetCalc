from functions import get_pcs_notes, get_pcs_booleans, get_intervals, get_dyad_interval, get_bno_decachord

def get_no_and_bno(pcs):
    if boolean_input == True:
        pcset = get_pcs_booleans(pcs)
    else:
        pcset = get_pcs_notes(pcs)
    intervals = get_intervals(pcset)
    size = len(intervals)
    if size == 1:
        return "Unison - 0"
    elif size == 2:
        return get_dyad_interval
    elif size == 3:
        return
    elif size == 4:
        return
    elif size == 5:
        return
    elif size == 6:
        return
    elif size == 7:
        return
    elif size == 8:
        return
    elif size == 9:
        return
    elif size == 10:
        return get_bno_decachord(intervals)
    elif size == 11:
        return "0123456789T"
    else:
        return "Tone row - 0123456789TE"
