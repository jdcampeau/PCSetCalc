from note_names import C, Db, D, Eb, E, F, Gb, G, Ab, A, Bb, B

def string_to_list(user_input: str) -> list[int]:
    new_list = user_input.split(",")
    for i in range(len(new_list)):
        new_list[i] = new_list[i].strip()
    return new_list

def find_pcs_notes(user_input: str) -> list[int]:
    PCs = []
    notes = string_to_list(user_input)
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

def find_pcs_booleans(booleans: list[bool]) -> list[int]:
    PCs = []
    i = 0
    for boolean in booleans:
        if boolean == True:
            PCs.append(i)
        i += 1
    return PCs

def get_dyad_name(intervals: list[int]) -> str:
    big = max(intervals)
    if big == 6:
        return "Tritone (augmented 4th/diminished 5th) - (06)"
    elif big == 7:
        return "Perfect 4th - (05)"
    elif big == 8:
        return "Major 3rd - (04)"
    elif big == 9:
        return "Minor 3rd - (03)"
    elif big == 10:
        return "Whole-tone (major 2nd) - (02)"
    else:
        return "Semitone (minor 2nd) - (01)"

def get_pf_decachord(intervals: list[int]) -> str:
    biggest = max(intervals)
    if biggest == 3:
        return "(0123456789)"
    else:
        start = 0
        idx1 = 0
        idx2 = 0
        for i in range(len(intervals)):
            if intervals[i] == 2 and start == 0:
                idx1 = i
                start = 1
            if intervals[i] == 2 and start == 1:
                idx2 = i
        gap = idx2 - idx1
        if gap == 1 or gap == 11:
            return "(012345678T)"
        elif gap == 2 or gap == 10:
            return "(012345679T)"
        elif gap == 3 or gap == 9:
            return "(012345689T)"
        elif gap == 4 or gap == 8:
            return "(012345789T)"
        elif gap == 5 or gap == 7:
            return "(012346789T)"
        elif gap == 6:
            return "(012356789T)"

def get_intervals(PCSet : list[int]) -> list[int]:
    if len(PCSet) == 1:
        return [None]
    PCs = PCSet.copy()
    PCs.sort()
    small = min(PCs)
    for i in range(len(PCs)):
        PCs[i] = PCs[i] - small
    intervals = []
    for i in range(len(PCs)):
        if i < (len(PCs) - 1):
            intervals.append(PCs[i+1] - PCs[i])
        else:
            intervals.append(12 - PCs[i])
    return intervals

def get_normal_order_outer(intervals: list[int]) -> list[int]:
    intervals_copy = intervals[:]
    all_orders = []
    for i in range(len(intervals)):
        pc = 0
        order = [0]
        for i in intervals_copy:
            pc += i
            order.append(pc)
        order.pop(-1)
        all_orders.append(order)
        popped = intervals_copy.pop(0)
        intervals_copy.append(popped)
    return get_normal_order_inner(all_orders, -1)

def get_normal_order_inner(list_of_orders: list[int], idx: int) -> list[int]:
    if len(list_of_orders) == 1:
        return list_of_orders[0]
    min_val = min(order[idx] for order in list_of_orders)
    narrowed_list = [order for order in list_of_orders if order[idx] == min_val]
    return get_normal_order_inner(narrowed_list, idx-1)

def get_bno(intervals: list[int]) -> list[int]:
    n_order1 = get_normal_order_outer(intervals)
    reversed_intervals = intervals[::-1]
    n_order2 = get_normal_order_outer(reversed_intervals)
    return get_normal_order_inner([n_order1, n_order2], -1)


def get_prime_form(bno: list[int]) -> str:
    prime_form = []
    for pc in bno:
        if pc == 10:
            prime_form.append("T")
            continue
        if pc == 11:
            prime_form.append("E")
            continue
        else:
            string_pc = f"{pc}"
            prime_form.append(string_pc)
    final_pf = ''.join(prime_form)
    return f"({final_pf})"

def get_icv(pcset: list[int]) -> str:
    icv = [0, 0, 0, 0, 0, 0]
    for i in range(len(pcset)):
        for j in range(i+1, len(pcset)):
            interval = pcset[j] - pcset[i]
            if interval > 6:
                interval = (12 + pcset[i]) - pcset[j]
            if interval == 1:
                icv[0] += 1
            elif interval == 2:
                icv[1] += 1
            elif interval == 3:
                icv[2] += 1
            elif interval == 4:
                icv[3] += 1
            elif interval == 5:
                icv[4] += 1
            else:
                icv[5] += 1
    joined = "".join(str(num) for num in icv)
    return f"<{joined}>"

#def get_name(pform: str) -> str:
