import itertools
def main():
    print("Checking all arrangements of PC's 1-11 relative to PC 0...")
    total_arrangements = 0
    ones_dict = {}
    ones = 0
    twos_dict = {}
    twos = 0
    threes_dict = {}
    threes = 0
    fours_dict = {}
    fours = 0
    fives = 0
    sixes_dict = {}
    sixes = 0
    sevens = 0
    eights = 0
    nines = 0
    tens = 0
    elevens = 0
    twelves_dict = {}
    twelves = 0
    c = [0]
    non_c_pcs = [1,2,3,4,5,6,7,8,9,10,11]
    for perm in itertools.permutaions(non_c_pcs):
        total_arrangements += 1
        perm_list = list(perm)
        all_pcs = c + perm_list
        set1 = [all_pcs[0], all_pcs[1], all_pcs[3], all_pcs[4], all_pcs[5], all_pcs[9]]
        set2 = 
        set3 = 
        set4 = 
        set5 =
        set6 = 
        set7 = 
        set8 = 
        set9 = 
        set10 = 
        set11 = 
        set12 = 
        list_of_sets = [set1, set2, set3, set4, set5, set6, set7, set8, set9, set10, set11, set12]
        unique_prime_forms = []
        all_prime_forms = []
        for st in list_of_sets:
            st.sort()
            int_seq = f"{st[1] - st[0]}{st[2] - st[1]}{st[3] - st[2]}{st[4] - st[3]}{st[5] - st[4]}{12 - st[5]}"
            #code here: if int_seq matches column imported from hexintseqs: reordered_set = something
            #add code for inversion check - if conditions for inversion are met:
                                                #prime_form = xyz
                                            #else:
                                                #prime_form = abc
            #add code to replace any occurence of "10" with "T"
            #add code to convert prime_form to string (prime_str)
            if prime_str not in unique_prime_forms:
                unique_prime_forms.append(prime_str)
            all_prime_forms.append(prime_str)
        pc_string = ",".join(all_pcs)
        if len(unique_prime_forms) == 12:
            twelves += 1
            twelves_dict[pc_string] = all_prime_forms
        if len(unique_prime_forms) == 11:
            elevens += 1
        #et cetera...
    print(f"Out of {total_arrangements / 5} unique arrangements, there are")
    print(f"
