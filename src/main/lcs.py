def get_lcs(s1, s2) -> tuple[list[list[int]], int]:
    """
    This function calculates the length and matrix of the Longest Common
    Subsequence (LCS) between two strings using dynamic programming.
    This function runs in O(n_1 * n_2) time.

    Args:
        s1 (string): The first input string.
        s2 (string): The second input string.

    Returns:
        Tuple: 
        - lcs (2D Array): A 2D array (matrix) that contains integer  
          values representing the length of the LCS at each cell.
        - lcs[0][0] (int): Length of the LCS
    """
    n_1, n_2 = len(s1), len(s2)
    lcs = [[0]*(n_2+1) for _ in range(n_1+1)]

    # Base case: If s2 is empty, LCS with any substring of s1 is 0
    for i in reversed(range(n_1)):
        lcs[i][n_2-1] = 0
    # Base case: If s1 is empty, LCS with any substring of s2 is 0
    for j in reversed(range(n_2)):
        lcs[n_1-1][j] = 0

    # Traverse backwards to fill LCS matrix
    for i in reversed(range(n_1)):
        for j in reversed(range(n_2)):
            if s1[i] == s2[j]:
                # If characters match, add 1
                lcs[i][j] = 1 + lcs[i+1][j+1]
            else:
                # If characters don't match, take the max LCS value
                lcs[i][j] = max(lcs[i+1][j], lcs[i][j+1])
    return lcs, lcs[0][0] # Return the LCS matrix and the LCS length

def lcs_string(s1, s2, lcs):
    """
    This function traverses through the LCS matrix to return 
    the LCS as a string.
    This function runs in O(n_1 + n_2) time.

    Args:
        s1 (string): The first input string.
        s2 (string): The second input string.
        lcs (2D Array): A 2D array (matrix) that contains integer values.

    Returns:
        string: The LCS of s1 and s2 as a string.
    """
    n_1, n_2 = len(s1), len(s2)
    i, j = 0, 0
    lcs_string = []
    # Traverse through LCS
    while i < n_1 and j < n_2:
        if s1[i] == s2[j]:  # Characters match
            lcs_string.append(s1[i])  # Add character to the LCS
            i += 1
            j += 1  # Move diagonally
        elif lcs[i+1][j] >= lcs[i][j+1]:
            i += 1  # Move down
        else:
            j += 1  # Move right
    return ''.join(lcs_string) # Return lcs into a string
