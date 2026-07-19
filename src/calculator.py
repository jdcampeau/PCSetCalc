from functions import *

def full_calc(boolean_input: bool, pcs: list[bool] | str) -> tuple[list:int, list:int, str, str]:
    if boolean_input == True:
        if pcs == [False, False, False, False, False, False, False, False, False, False, False, False]:
            return [0, 0, "No input detected", "error"]
        pcset = find_pcs_booleans(pcs)
    else:
        if pcs == "":
            return [0, 0, "No input detected", "error"]
        pcset = find_pcs_notes(pcs)
    intervals = get_intervals(pcset)
    size = len(pcset)
    if size == 1:
        return pcset, [0], "(0) - Unison", "<000000>"
    elif size == 2:
        return [0, min(intervals)], get_pf_numeric(intervals), get_dyad_name(intervals), get_icv(pcset)
    elif size == 11:
        return get_pfn_helper_a(intervals), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "0123456789T", "<10101010105>"
    elif size == 12:
        return pcset, pcset, "Tone row - 0123456789TE", "<12121212126>"
    else:
        icv = get_icv(pcset)
        n_o = get_pfn_helper_a(intervals)
        bno = get_pf_numeric(intervals)
        prime_form = get_prime_form(bno)
        return [n_o, bno, prime_form, icv]
