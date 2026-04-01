import itertools
from functions import get_intervals, rotate_intervals, get_prime_form

def get_set(idx_list):
    set = []
    for idx in idx_list:


def main():
    print("Checking all arrangements of PC's 1-11 relative to PC 0...")
    total_arrangements = 0
    twelves_dict = {}
    twelves = 0
    c = [0]
    non_c_pcs = [1,2,3,4,5,6,7,8,9,10,11]
    for perm in itertools.permutaions(non_c_pcs):
        total_arrangements += 1
        perm_list = list(perm)
        all_pcs = c.extend(perm_list)
        set_indices = [[0, 1, 3, 4, 5, 9], [1, 0, 3, 6, 7, 9], [2, 3, 5, 7, 10, 11], [3, 0, 1, 2, 5, 7],
                       [4, 0, 5, 8, 9, 10], [5, 0, 2, 3, 4, 10], [6, 1, 7, 8, 9, 11], [7, 1, 2, 3, 6, 11],
                       [8, 4, 6, 9, 10, 11], [9, 0, 1, 4, 6, 8], [10, 2, 4, 5, 8, 11], [11, 2, 6, 7, 8, 10]]
        sets = []
        for indices in set_indices:
            pc_set = []
            for idx in indices:
                pc_set.append(all_pcs[idx])
            sets.append(pc_set)
        unique_prime_forms = []
        for st in sets:
            st.sort()
            int_seq = get_intervals(st)
            if int_seq == [2, 2, 2, 2, 2, 2]:
                continue
            for interval in int_seq:
                #add check for hexachord of all half-steps
            normal_order = rotate_intervals(intervals, st)
            best_normal_order = #add code for inversion check - if conditions for inversion are met:
                                                #prime_form = xyz
                                            #else:
                                                #prime_form = abc
            prime_form = get_prime_form(inversion_checked)
            if prime_form not in unique_prime_forms:
                unique_prime_forms.append(prime_form)
        if len(unique_prime_forms) == 12:
            twelves += 1
            pc_string = ",".join(all_pcs)
            unique_string = ",".join(unique_prime_forms)
            twelves_dict[pc_string] = unique_string
    print(f"Out of {total_arrangements / 5} unique arrangements, there are")
    print(f"{twelves} arrangements that yield twelve unique prime forms.")
