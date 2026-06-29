from functions import *

def main(pcs: list[bool] | str) -> tuple[list:int, list:int, str, str]:
    if boolean_input == True:
        pcset = get_pcs_booleans(pcs)
    else:
        pcset = get_pcs_notes(pcs)
    intervals = get_intervals(pcset)
    if size == 1:
        return pcset, [0], "Unison - 0", "<000000>"
    elif size == 2:
        return [0, min(intervals)], get_bno(intervals), get_dyad_interval, get_icv(pcset)
    elif size == 11:
        return get_normal_order_outer(intervals), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "0123456789T", "<10101010105>"
    elif size == 12:
        return pcset, pcset, "Tone row - 0123456789TE", "<12121212126>"
    else:
        icv = get_icv(pcset)
        n_o = get_normal_order_outer(intervals)
        bno = get_bno(intervals)
        prime_form = get_prime_form(bno)
        return n_o, bno, prime_form, icv
