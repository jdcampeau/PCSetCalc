from functions import find_pcs_notes, find_pcs_booleans, get_intervals, get_dyad_interval, get_bno_decachord, get_normal_order_outer, get_normal_order_inner, get_bno, get_prime_form

def get_no_and_bno(pcs: list[bool] | str) -> tuple[list:int, list:int, str]:
    if boolean_input == True:
        pcset = get_pcs_booleans(pcs)
    else:
        pcset = get_pcs_notes(pcs)
    intervals = get_intervals(pcset)
    if size == 1:
        return pcset, [0], "Unison - 0"
    elif size == 2:
        return [0, min(intervals)], get_bno(intervals), get_dyad_interval
    elif size == 10:
        return get_normal_order_outer(intervals), get_bno_decachord(intervals)
    elif size == 11:
        return get_normal_order_outer(intervals), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "0123456789T"
    elif size == 12:
        return pcset, pcset, "Tone row - 0123456789TE"
    else:
        n_o = get_normal_order_outer(intervals)
        bno = get_bno(intervals)
        prime_form = get_prime_form(bno)
        return n_o, bno, prime_form
