def get_lcs(s1, s2):
    n_1, n_2 = len(s1), len(s2)
    lcs = [[0] * (n_2 + 1) for _ in range(n_1 + 1)]
    
    for j in reversed(range(n_2)):
        lcs[n_1 - 1][j] = 0

    for i in reversed(range(n_1)):
        lcs[i][n_2 - 1] = 0
        
    for i in reversed(range(n_1)):
        for j in reversed(range(n_2)):
            if s1[i] == s2[j]:
                lcs[i][j] = 1 + lcs[i + 1][j + 1]
            else:
                lcs[i][j] = max(lcs[i + 1][j], lcs[i][j + 1])
    return lcs, lcs[0][0]

def lcs_string(s1, s2, lcs):
    # TODO: lcs chars to string
    return 0
