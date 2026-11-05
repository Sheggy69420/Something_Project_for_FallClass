def truth_table_biconditional():
    print("p", "q", "r", "p AND q", "Result", sep="\t")

    for p in [True, False]:
        for q in [True, False]:
            for r in [True, False]:
                p_and_q = p and q
                result = p_and_q == r
                print(p, q, r, p_and_q, result, sep="\t")


 
def truth_table_implication():
    print("p", "q", "r", "q OR r", "Result", sep="\t")

    for p in [True, False]:
        for q in [True, False]:
            for r in [True, False]:
                q_or_r = q or r
                result = (not p) or q_or_r
                print(p, q, r, q_or_r, result, sep="\t")


truth_table_biconditional()
print()
truth_table_implication()
